# Predicting Game Result

## Group Members
- Santosh Suwal
- HaoNan Ou
- Zhiqiang Wang

## Abstract
This paper focuses on predicting game outcomes using different machine learning algorithms based on the first 10 min states from LOL game. This helps players get edge in the game, since, we can predict which features are important to win in the first 10 min of the game. The metrics chosen to assess the performance of the model is the accuracy, hence, the problem utilized several machine learning predictive models. One finding was that the accuracy of models ranges from 68-74%, in particular, Logistics Regression showed the best performance. Also, the train and test sets showed similar accuracy. PCA and LDA didn't help much since their results were not perfectly linearly separable. Furthermore, standardizing and normalizing dataset only affect models' accuracy slightly. Another finding was that we can be roughly 70% sure whether a blue team or red team is going to win based on first 10mins of gameplay stats by considering the result from Tensorflow Keras's classification and GridSearchCV.

## Introduction
The data includes first 10 min stats from League of Legends Game including the target value whether the blue team won or not. The goal is to analyse features to predict winning team and also get statistical output of which features are more important in winning the game in the first 10 min. This is important because it helps gamers to better strategize the game. Then, the process was to apply several machine learning techniques such as Decision Tree, Logistic Regression, and so on. Interestingly, Logistic Regression had the highest accuracy. We also conducted methods such as cross validation and GridSearchCV to find the best parameters for each model. Additionally, Roc Auc curve was used to improve our model accuracy and to look for model overfitting or underfitting.

## Background
Similarly, a data scientist named Shayaan Jagtap(2018) wrote about predicting game outcomes by looking at key features such as kills, gold differences, etc. Jagtap conducted several predictive models, particularly, a Logistics Regression with a 75.78% accuracy, one of the best models of the highest accuracy, in the first 15 mins of the game, which is very close to our result. Interestingly, Jagtap found out that the chance of correctly predicting the winning team in the early game(about first 5 minutes) was not very high since ‘Your enemy could always turn the tide.' However, the prediction become more accurate as the game went on.

## Data
The data is found on Kaggle. The data set contained 9879 observations with 40 features. there are 19 features per team except gameid and the target variable as indicated above.

[Data Source](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min)
    
## Method
   - EDA
        - Data Cleaning
        - Check correlation between features
        - Identify Missing Data
        - Dectect outliers
        - Split Data
   - Features scaling
   - Classfications
        - LogisticRegression 
        - K-Nearest Neighbors
        - DecisionTree 
        - RandomForest
        - SVM
        - Tensorflow Keras

## Evaluation
   - Feature Importance with random Forests
   - PCA
   - LDA
   - Grid Serach CV
   - ROC & AUC
   - learning and validation curves
    

## Concluson
The accuracy of models ranges from 68-74%. Logisitic Regression does better in classifying. Keras/Tensorflow with single layer using softmax activation worked better on raw, standard scaled and min max scaled data. So, using the models we can be ~70% sure whether a blue team or red team is going to win based on first 10mins of game play stats.

### Contents
- [Final Report](./final_report.ipynb)
- [Final PPT](./slides/Final_Powerpoint.pptx)





