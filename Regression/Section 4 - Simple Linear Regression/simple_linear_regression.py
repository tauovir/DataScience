# Simple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Impoprt Dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:,1].values

#Split Dataset intoi training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size = 0.2,random_state = 0)

# fitting Simple Linear Regression to the trainng set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
#Predicting the test result
predictedSalary = regressor.predict(X_test)
#Visualising the training set result
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("Salary vs Experience(Training Set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()
#Visualising the test set result
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("Salary vs Experience(Test Set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

     