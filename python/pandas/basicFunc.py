# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# ==========Series Basic Functionality
s = pd.Series(np.random.rand(15))
print(s.axes) # return the list of label series
print(s.empty) # Is object is empty
print(s.ndim) # return Dimension
print(s.size) # return Size
print(s.head(3))
print(s.tail(3))
print(s.values)



# Data Frame basic Functionality
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
trans = df.T
print(df.T) #Returns the transpose of the DataFrame. The rows and columns will interchange.
print(df.axes)
print(df.dtypes)
print(df.empty)
print(df.ndim)
print(df.shape)
print(df.size) # return Size(ros * cols)
print(df.head(3))
print(df.tail(3))
print(df.values)







