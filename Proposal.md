# League of Legends Diamond Ranked Games (10 min)

[Link to Data Source](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min)

### Group Members
- Santosh Suwal
- HaoNan Ou
- Zhiqiang Wang

## Data overview:
League of Legends is a MOBA (multiplayer online battle arena) where 2 teams (blue and red) face off. There are 3 lanes, a jungle, and 5 roles. The goal is to take down the enemy Nexus to win the game.

This dataset contains the first 10min. stats of approx. 10k ranked games (SOLO QUEUE) from a high ELO (DIAMOND I to MASTER). Players have roughly the same level.

Each game is unique. The gameId can help you to fetch more attributes from the Riot API.

There are 19 features per team (38 in total) collected after 10min in-game. This includes kills, deaths, gold, experience, level… It's up to you to do some feature engineering to get more insights.

The column blueWins is the target value (the value we are trying to predict). A value of 1 means the blue team has won. 0 otherwise.

## Attributes
- Warding totem: An item that a player can put on the map to reveal the nearby area. Very useful for map/objectives control.
- Minions: NPC that belong to both teams. They give gold when killed by players.
- Jungle minions: NPC that belong to NO TEAM. They give gold and buffs when killed by players.
- Elite monsters: Monsters with high hp/damage that give a massive bonus (gold/XP/stats) when killed by a team.
- Dragons: Elite monster which gives team bonus when killed. The 4th dragon killed by a team gives a massive stats bonus. The 5th dragon (Elder Dragon) offers a huge advantage to the team.
- Herald: Elite monster which gives stats bonus when killed by the player. It helps to push a lane and destroys structures.
- Towers: Structures you have to destroy to reach the enemy Nexus. They give gold.
- Level: Champion level. Start at 1. Max is 18.

## What problem are you tackling?
- Classify LOL ranked games outcome by looking at the first 10 min worth of data.
- Since warding totem is use for player can put on the map, it useful for map control, it can make hypothesis test, does team put more wards will have higher probabilty can win the game.
- we can test on each attributes, to figure out which arttributes have main impact to win the game.
- Also base on map design, blue team is close to Elite monster place, and red team have easy control in dragons, we can make hypothesis test to see is red team always get more dragons and blue team always get more elite monster. 
- does team get more elite monster have higher win rate than the team get the dragons. and to slove one issues why blue team have higher winrate than red team.


## Exploratory Data Analysis:
- Identification of variables and data types

## Data Preprocessing:
- Dealing with missing values
- Adding dummy variables for features with a lot of zeros to improve model fits.
- Encoding categorical variables
- Standardising / normalizing 
- Matrix plot and exploratory data Viz.

## Feature Selection and/or Extraction:
- Use Random forest to do feature selection to remove least important features.
- Use PCA to compare results

# Is this an application or a theoretical result? 
- It is an Application result.

# What machine learning techniques are you planning to apply or improve upon? 
- Linear regression and Logistic regression
- Knn classifier
- Random forest
- Tree classifier
- Support Vector Machines

# Intended experiments: What experiments are you planning to run? 
- Trying different algorithms to predict same clustering or grouping
- Fitting linear regression on to the baseline salary
- Logistic regression to classify
- Evaluation the model with accuray

# How do you plan to evaluate your machine learning algorithm? 
- Use Dummy Classifier for baseline metric for evaluation
- Use different types of classifiers to compare results and find the one with best performance
