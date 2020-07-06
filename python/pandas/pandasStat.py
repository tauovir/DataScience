# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = {"Name":["Taukir","Khan","Banana","Sanu","Mango"],"Age":[20,30,25,60,54],"Salary":[30000,25000,60000,15000,80000]}
dataset = pd.DataFrame(data)
print(dataset)
dataMax = dataset.max(numeric_only = True)
print("==========Max================")
print(dataMax)
print("==========Mean================")
print(dataset.mean(numeric_only = True))
print("==========MIn================")
print(dataset.min(numeric_only = True))

print(dataset.describe())

print(dataset.describe(include=['O']))

print(dataset[['Age','Salary']].head())
dataset['Salary'] = 0000
print(dataset[['Age','Salary']].head())

dataset.loc[2,'Salary'] = 99
print(dataset[['Age','Salary']].head())
