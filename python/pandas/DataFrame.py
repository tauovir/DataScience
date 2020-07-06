# -*- coding: utf-8 -*-
"""
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
Features of DataFrame
Potentially columns are of different types
Size – Mutable
Labeled axes (rows and columns)
Can Perform Arithmetic operations on rows and columns
"""
#Pandas.DataFrame 
#pandas.DataFrame( data, index, columns, dtype, copy)
"""
Create DataFrame
A pandas DataFrame can be created using various inputs like −
Lists
dict
Series
Numpy ndarrays
Another DataFrame
"""
import pandas as pd
df =  pd.DataFrame()
print(df)
#Create a DataFrame from Lists
l1 = list('12355')
l2 = [1,2,3,4,5,6]
df = pd.DataFrame(l2)
print(df)
list2 = [['khan',25],['kapil',30],['Mango',25],['Opps',25]]
df = pd.DataFrame(list2, columns = ['Name','Age'], dtype = float)
print(df)

#Dictionary
data = {'Name':['Taukir','Khan','Mango','Orange'],'Age':[25,26,55,59]}
df = pd.DataFrame(data,index = ['rank1','rank2','rank3','rank4'])
print(df)
#
data = [{'a':10,'b':50},{'a':60,'b':88,'c':77}]
df = pd.DataFrame(data)
print(df)
 
#Creating Dictinary and Series and Column Addition
data = {'one': pd.Series([1,2,3], index = ['a','b','c']),'two': pd.Series([1,2,3,4], index = ['a','b','c','d'])}
df = pd.DataFrame(data)
df['three'] = pd.Series([50,60,35], index = ['a','b','c'])
df['four'] = df['one'] + df['three']
print(df)

# Columns Deletion
data = {'one': pd.Series([1,2,3], index = ['a','b','c']),'two': pd.Series([1,2,3,4], index = ['a','b','c','d'])}
df = pd.DataFrame(data)
df['three'] = pd.Series([50,60,35], index = ['a','b','c'])
df['four'] = df['one'] + df['three']
print(df)
del df['four']
print(df)
df.pop('two')
print(df)

# Rwo Selection, Addition and deletion
data = {'one': pd.Series([1,2,3], index = ['a','b','c']),'two': pd.Series([1,2,3,4], index = ['a','b','c','d'])}
df = pd.DataFrame(data)
df['three'] = pd.Series([50,60,35], index = ['a','b','c'])
df['four'] = df['one'] + df['three']
print(df)
# Passing by row Label
print(df.loc['a'])  # result Will Be series
print(df.loc['a'].values)
# Passing by integer
print(df.iloc[2])  # result Will Be series
# Slicing
print(df[2:4])

# Adding Row
df = pd.DataFrame([[1,2],[3,4]], columns = ['a','b'])
print(df)

df2 = pd.DataFrame([[10,20],[30,40]], columns = ['a','b'])
df = df.append(df2)
# Dleting Row
df = df.drop(0)

















 






