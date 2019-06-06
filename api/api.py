# starting the api
# importing libraries

from flask import Flask, request, jsonify
from sklearn.externals import joblib    # to load the model
from sklearn.preprocessing import LabelEncoder  # for data preprocessing
import json # for deserialization
import pickle   # to handle the pkl file
import pandas as pd # to andle dataframes
from flask_restful import Resource, Api # to define the app
import numpy as np  

# in order to filter the warnings
import warnings 
warnings.filterwarnings("ignore")

app = Flask(__name__)
api = Api(app)

# load the model

model = joblib.load('depression_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # define the columns

    # data preprocessing

    # put all the columns into a list
    features = []

    # use the model to predict the class
    prediction = model.predict(features)

    # output the name of the predicted class
    if prediction == 1:
        pred_class = 'Depressed'
    else:
        pred_class = 'Not Depressed'

    # create and send a response to the API caller
    return jsonify(prediction=pred_class)

if __name__ == '__main__':
    app.run(port=5000, debug=True)


