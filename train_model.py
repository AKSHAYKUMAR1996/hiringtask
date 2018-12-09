# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('new_train_data.csv')

X = dataset.iloc[:, 1:].values.astype(int)
y = dataset.iloc[:, 0].values.astype(int)

print X[0],y[0]
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

'''from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 5, random_state = 0)
'''
regressor.fit(X_train, y_train)
# Predicting the Test set results
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
print "MSE: ",mean_squared_error(y_test, y_pred) 

dataset = pd.read_csv('new_test_data.csv')

X = dataset.iloc[1:, :].values.astype(int)
print X[0]
pred = regressor.predict(X)

x = pd.DataFrame(X)
y = pd.DataFrame(pred)

frames = [x,y]

result = pd.concat(frames)

result.to_csv("output.csv")