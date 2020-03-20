# SVR

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Load Data
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2:3].values

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting SVR to dataset
from sklearn.svm import SVR
regressor = SVR(kernel = "rbf")
regressor.fit(X, y)

y_pre =sc_y.inverse_transform( regressor.predict(sc_y.transform(np.array([[6.5]]))))

#Visualising the SVR Result
plt.scatter(X,y, color="red")
plt.plot(X, regressor.predict(X),color="blue")
plt.title("SVr Graph")
plt.xlabel("Position lavel")
plt.ylabel("Salary")
plt.show()





