# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
"""
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)
"""
left = pd.DataFrame({
        'id' : [1,2,3,4,5],
        'Name' : ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'subject_id':['sub1','sub2','sub4','sub6','sub5']
        })

right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

print(left)
print(right)
print(pd.merge(left,right,on = 'id'))

# Merging Two DataFrame on multiple keys
print(pd.merge(left,right,on=['id','subject_id']))

print(pd.merge(left, right, on='subject_id', how='left'))   # left , inner, outer
