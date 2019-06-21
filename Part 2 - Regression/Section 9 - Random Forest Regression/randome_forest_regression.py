#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load Data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,-1].values

#Fitting Randome Forest Regressor
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(X, y)
y_pred = regressor.predict(np.array([[6.5]]))

#Hi Dimension Visualization
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y)
plt.plot(X_grid,regressor.predict(X_grid),color = 'red')
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()
