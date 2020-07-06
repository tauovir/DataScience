# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

list1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12],
        [13,14,15]
        ]
data = pd.DataFrame(list1, index = ['a','c','d','e','f'],columns = ['one','two','three'])
data
data = data.reindex(['a','b','c','d','e','f','g','g'])
data

# Check For Missing data
print(data['one'].isnull())
print(data['one'].notnull())
print(data['one'].sum())

# Filling Missing Data
#data.fillna(0)
data
#data = data.fillna(data['one'].mean())

print(data.fillna(method = 'pad')) # Fill Name with immediate above row
print(data.fillna(method = 'backfill')) # Fill Name with immediate below row
print(data.fillna(method = 'ffill')) # Fill Name with immediate above row


#Drop Missing Values
print(data.dropna())
print(data.dropna(axis = 1))

# Replace Value
print(data.replace({4:400,15:1500}))

