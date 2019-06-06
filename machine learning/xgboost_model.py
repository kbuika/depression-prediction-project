# importing dependencies
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
# %matplotlib inline 

import xgboost as xgb
from xgboost import XGBClassifier

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
s = (['survey_date', 'surveyid'])
train = train.drop(s, axis=True)

# dealing with the missing values
"""
The next step is the part that differenciates most data scientists. This is where you are either to fill the missing datapoints with values or you decide to drop all the columns all together.

    * Dropping the columns with missing values will reduce the number of features to use to train the model. This may lead to poor accuracy.
    * Filling the missing values may lead to the creation of artificial features. This will render the dataset useless and will hence not aid in the improvement of our accurecy.

    Tricky! right?? But i decided to fill the missing values.

"""
# for now i'll just fill the missing values
# use the fillna method to fill the missing values with the mean value of the whole column.
train = train.fillna(train.mean())

# allocating the x and y values
x = train.drop(['depressed'], axis=1)
y = train.depressed

# using train_test_split for cross validation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# standardazing the data
# the standard scaler converts all input to a similar datatype
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Training the Model
print("Training the Model")
# for this problem i'll be using XGBoost Classifier
model = XGBClassifier()
model.fit(X_train_std, y_train)
print("**********Done******************")

from sklearn.metrics import mean_absolute_error
pred_train = model.predict(X_train_std)
print("The model has an error of:")
print(mean_absolute_error(pred_train, y_train))

# since i only need the model for prediction, I dont have to test the model

# pickling the model
from sklearn.externals import joblib
joblib.dump(model, 'depression_predict.pkl')