# -*- coding: utf-8 -*-
#Pandas provides various facilities for easily combining together Series, DataFrame, and Panel objects.
# pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)
 import pandas as pd
 import numpy as np
 
one = pd.DataFrame({
  'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
  'subject_id':['sub1','sub2','sub4','sub6','sub5'],
  'Marks_scored':[98,90,87,69,78]},
  index=[1,2,3,4,5])
 
two = pd.DataFrame({
  'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
  'subject_id':['sub2','sub4','sub3','sub6','sub5'],
  'Marks_scored':[89,80,79,97,88]},
  index=[1,2,3,4,5])
xx = pd.concat([one,two])

print(pd.concat([one,two],keys=['x','y']))
print(pd.concat([one,two],keys=['x','y'], ignore_index = True))

xx = pd.concat([one,two],axis = 1)

# Using Append
print(one.append(two))

print(one.append([one,two]))

# Time Series
#the current date and time.
print(pd.datetime.now())
# Create TimeStamp
print(pd.Timestamp('2017-03-01'))

print(pd.Timestamp(1587687255,unit='s'))

print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
