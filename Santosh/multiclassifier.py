# Get baseline results here with logisic regression and random forest
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

SEED = 42
np.random.seed(SEED)
import pandas as pd
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.tree import DecisionTreeClassifier as Tree
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Models
def dummy_classifier():
    return DummyClassifier(strategy='stratified', random_state=SEED)

def tree_classifier():
    return Tree(max_depth=5, random_state=SEED)

def knn_classifier():
    return KNN(n_neighbors=5)

def lr_classifier():
    return LogisticRegression(random_state=SEED, max_iter=2000)

def rf_classifier():
    # chaning max depth since it takes to long to compute default 100
    return RandomForestClassifier(max_depth=5, random_state=SEED)

def svc_classifier():
    return SVC()

# Performance Plotter
def performanceplot(classifiers, X_train, y_train, X_test, y_test):
    allperf = {}
    for (title, key, classifier) in classifiers:
        classifier.fit(X_train, y_train)
        predict = classifier.predict(X_test)
        report = classification_report(y_test, predict, target_names=['blueLose', 'blueWins'])
        perf = [accuracy_score(y_test, predict), f1_score(y_test, predict),
               precision_score(y_test, predict), recall_score(y_test, predict)]
        perflabels = ('accuracy', 'f1score', 'precision', 'recall')
        labelrange = np.arange(len(perflabels))
        plt.bar(labelrange, perf)
        plt.xticks(labelrange, perflabels)
        plt.title(title, size=14)
        plt.ylim(0,1)
        plt.show()
        print(report)
        objdict = dict(zip(perflabels, perf))
        print(objdict)
        objdict['title'] = title
        allperf[key] = objdict
    return allperf

def main():
    df = pd.read_csv('../datasets/train.csv')
    y = df['blueWins']
    target = y.unique()
    X = df.drop(['blueWins'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, stratify=y, random_state=SEED)
    titles = ['Dummy Classifier', 'Logistic', 'KNN', 'Decision Tree', 'SVC', 'Random Forest']
    keys = ['dummy', 'logistic', 'knn', 'tree', 'svc', 'rf']
    classifier_funcs = [dummy_classifier(), lr_classifier(), knn_classifier(), tree_classifier(), svc_classifier(), rf_classifier()]
    classifiers = zip(titles, keys, classifier_funcs)
    allperf = performanceplot(classifiers, X_train, y_train, X_test, y_test)
    crossValidation(X_train, y_train)
    regularized = regularization(X_train, y_train, X_test, y_test)
    return (allperf, regularized)

def crossValidation(X_train, y_train):
    from sklearn.model_selection import cross_val_score
    titles = ['Dummy Classifier', 'Logistic', 'KNN', 'Decision Tree', 'SVC', 'Random Forest']
    keys = ['dummy', 'logistic', 'knn', 'tree', 'svc', 'rf']
    classifier_funcs = [dummy_classifier(), lr_classifier(), knn_classifier(), tree_classifier(), svc_classifier(), rf_classifier()]
    classifiers = zip(titles, keys, classifier_funcs)

    for title, key, classifier in classifiers:
        scores = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=5)
        print("[{}] >> Accuracy: {} (+/- {})".format(title, scores.mean(), scores.std()))


def regularization(X_train, y_train, X_test, y_test):
    titles = ['L1 Regularization', 'L2 Regularization']
    keys = ['l1', 'l2']
    classifier_funcs = [
        LogisticRegression(penalty='l1', random_state=SEED, max_iter=500, solver='liblinear'),
        LogisticRegression(penalty='l2', random_state=SEED, max_iter=500)
    ]
    classifiers = zip(titles, keys, classifier_funcs)
    reg = performanceplot(classifiers, X_test, y_test, X_train, y_train)
    return reg



if __name__ == '__main__':
    print('Cannot run main function')