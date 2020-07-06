# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

unsortedData = pd.DataFrame(np.random.rand(10,2), index=[1,4,6,2,3,5,9,8,0,9], columns = ['col2','col1'])

print(unsortedData)
sortedData = unsortedData.sort_index() # Sort Index
print(sortedData)

sortedData = unsortedData.sort_index(ascending = False) # Sort Index
print(sortedData)

#Sort the Columns
#By passing the axis argument with a value 0 or 1, the sorting can be done on the column labels. By default, axis=0, sort by row. 
unsortedData = pd.DataFrame(np.random.rand(10,2), index=[1,4,6,2,3,5,9,8,0,9], columns = ['col2','col1'])
print(unsortedData)
sorted_df=unsortedData.sort_index(axis=1)
print(sorted_df)

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(unsorted_df)
sorted_df = unsorted_df.sort_values(by='col1')
print(sorted_df)

sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')