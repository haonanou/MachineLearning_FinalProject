League of Legends Diamond Ranked Games (10 min)

Data Source: https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min

League of Legends is a MOBA (multiplayer online battle arena) where 2 (blue and red) teams face off. 
There are 3 lanes, a jungle, and 5 roles. 
The goal is to take down the enemy Nexus to win the game.

This dataset contains the first 10min. stats of approx. 
10k ranked games (SOLO QUEUE) from a high elo (DIAMOND I to MASTER). 
Players have roughly the same level.

Each game is unique. The game can help you to fetch more attributes from the Riot API.

There are 19 features per team (38 in total) collected after 10min in-game. 

The column blueWins is the target value (the value we are trying to predict). 
A value of 1 means the blue team has won. 0 otherwise.

Motivation:  Classify LOL ranked games outcome by looking at the first 10 min worth of data. It is an Application result.

Method: we can apply classification machine learning techniques such as SVM classifier, decision tree classifier,
random forest, neighbors classifiers, linear classifiers.

Intended experiments: we can use train test split, bootstrap, k-fold cross-validation, confusion matrix to evaluating the performance of the models.

the final thing we do is can develop one algorithms search for data, and apply to see what are the outcomes
or the probability which side can win the game.



