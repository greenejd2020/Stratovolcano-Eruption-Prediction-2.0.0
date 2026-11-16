# -*- coding: utf-8 -*-

#How often do stratovolcanoes erupt?

#Importing Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

#Setting the CSV File to a variable

st = pd.read_csv('Stratovolcano_Eruption_Prediction.csv')

st_columns = st[['Southeastness', 'Height', 'Days Between Eruptions']]

x = st_columns[['Southeastness', 'Height']]
y = st_columns['Days Between Eruptions']

#Train Test Splitting

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2)

#Linear Regression

lr = LinearRegression()
lr.fit(xtrain, ytrain).predict(xtest).astype(np.int64)

#Prediction

print('Predict!')
Southeastness = int(input('Enter how southeast the volcano is.'))
Height = int(input('Enter the height in feet.'))
print('y' + ' ' + '=' + ' ' + str(lr.coef_[0]) + 'S' + ' ' + '+' + ' ' + str(lr.coef_[1]) + 'H' + ' ' + '+' + ' ' + str(lr.intercept_))
print(f'{int((lr.coef_[0] * Southeastness) + (lr.coef_[1] * Height) + lr.intercept_)} Days')
