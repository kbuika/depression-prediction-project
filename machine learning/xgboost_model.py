# importing dependencies
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
# %matplotlib inline 

# from collections import counter
import xgboost as xgb
# from sklearn.ensemble import XGBClassifier

from sklearn.preprocessing import LabelEncoder, StandardScaler

sns.set(style='white', context='notebook', palette='deep')
# end of importing

# loading the data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# view the train data
print("The train data")
print(train.head())

# viewing the missing datapoints
print("*************************")
# from visualization, the data has alot of missing values

# dropping the date and the survey_id
s = (['survey_data', 'surveyid'])
train = train.drop(s, axis=True)

