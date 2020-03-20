# Multiple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score

#Load Data set
dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#Encoding Independent Variable
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder = LabelEncoder()
X[:,3] = labelEncoder.fit_transform(X[:,3])
oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X)
X = X.toarray()
# Avoid the dummy variable trap
X = X[:,1:]     #All row and column from 1 to end, We skipped one encoded variable
#Because we need to skipp one column if there R 100 encoded,we shoud keep 99
# But most model take cae of it,

#Splitting the Dataset into the Training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Fitting Multiple Linear Regression  to The training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
# Predicting The Test Set result
y_pred = regressor.predict(X_test) 



#Build Optimal model using Backward Elimination to find independent variable
# which are statistically significant for dependent variabke. simple term important variable
import statsmodels.formula.api as sm
# Here we are building Y = b0 + b1x1 + b2x2 = bnxn  to Y = box0 + b1x1 + b2x2 + bnxn where x0 = 1
# Regression model take care of b0 =1 but statsmodels not thats why we have to add
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog= y, exog = X_opt).fit()
regressor_OLS.summary()


X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog= y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog= y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,4,5]]
regressor_OLS = sm.OLS(endog= y, exog = X_opt).fit()
regressor_OLS.summary()









