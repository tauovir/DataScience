# -*- coding: utf-8 -*-

#How to import pandas and check the version?
import pandas as pd

print(pd.__version__)

#2. How to create a series from a list, numpy array and dict?
import numpy as np
sr1 = pd.Series(list('abcsdrd'))
sr2 = pd.Series(np.array([1,2,3,4,5]))
sr3 = pd.Series({'a':12,'b':55})
list1 = list('abcd')
num = np.arange(4)
dic = dict(zip(list1,num))
sr4 = pd.Series(dic)

#How to convert the index of a series into a column of a dataframe?

list1 = list('abcd')
num = np.arange(4)
dic = dict(zip(list1,num))
sr45 = pd.Series(dic)
df = sr45.to_frame().reset_index()

#4. How to combine many series to form a dataframe?
s1 = pd.Series(list('abcdefghijklmnopqrstwyxz'))
s2 = pd.Series(np.arange(26))
data = pd.concat([s1,s2], axis = 1)

#5. How to assign name to the series’ index?
sr = pd.Series(list('abcdef'))
sr.name = 'index22'
sr.head()

#6. How to get the items of series A not present in series B?
sr1 = pd.Series([1,2,3,4,5])
sr2 = pd.Series([4,5,6,7,8])
cc = sr1[~sr1.isin(sr2)]
 #7. How to get the items not common to both series A and series B?
s1 = pd.Series([1,2,3,4,5,10])
s2 = pd.Series([1,5,3,5,20,60])
cc1 = s1[~s1.isin(s2)]

# 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
state = np.random.RandomState(100)

serial = pd.Series(state.normal(10,5,25))
np.percentile(serial, q=[0, 25, 50, 75, 100])

# 9 How to get frequency counts of unique items of a series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
#Create a DataFrame
df = pd.DataFrame(d)
print (df)
frq = df['Age'].value_counts()
boolInd = df['Age'].value_counts()
df.loc[df["Age"].isin(boolInd.index[2:]),"Age"] = "Other"
print(df)

#10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
df = pd.DataFrame(d)
print (df)
frq = df['Age'].value_counts()
boolInd = df['Age'].value_counts()
df.loc[df["Age"].isin(boolInd.index[2:]),"Age"] = "Other"
print(df)

# 11. How to bin a numeric series to 10 groups of equal size
sr1 = pd.Series(np.random.rand(20))
sr1
pd.qcut(sr1, q = [0,.10,.20,.30,.40,.50,.60,.70,.80,.90,1], labels = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head()
















