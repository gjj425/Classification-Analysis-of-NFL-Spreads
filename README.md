# Metis_Project_3
Classification Project Repository


**Project Title:** 

Classification Analysis of NFL Spreads 

**Description:**

Las Vegas bookmakers use point spreads to insentivise bettors to bet on the underdog. In an effort to use spreads to adjust public sentiment
and establish a 50/50 split on bets for and against a particular team, it is theoretically possible to take advantage of the difference in public 
sentiment and statistical conclusions to predict a team's ability to beat its spread each week. Should a gambler maintain a 52.5% winning percentage 
(against a 10% Vig), the bettor will remain profitable. This analysis attempts to use classification analysis to maintain a success rate above 52.5%.

**Features and Target Variables:**

Target: Did the target team beat it's spread? (column: 'beat_spread', 1=win against spread, 0=loss against spread)

Features are designed to reflect how much better/worse a team is than its opponent for each unit of public sentiment represented by the spread. 
Four features have been engineered (where target team = team being assessed, opponent = team playing against for a given game):

1. Target points scored per game through prior week / opponent points scored per game through prior week / (100-spread)

2. Target points scored against per game through prior week / opponent points scored against per game through prior week / (100-spread)

3. Wins against the spread/total games played in a given season

4. Is the target team the favorite?

**Data Used:**

Data taken from Kaggle, supplimentary data from pro-football-reference.com, Week 8 2020 odds taken from CBS Sports

**Tools Used:**

sklearn, XGBoost, Pandas, Seaborn

**Possible impacts of your project:**

A proven strategy that provides consistent success above 52.5% would provide a profitable returns.
