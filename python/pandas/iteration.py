# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame({
        'A': pd.date_range(start = '2015-02-01', periods = N, freq = 'D'),
        'x' : np.linspace(0,stop = N-1, num= N),
        'y' : np.random.rand(N),
        'C': np.random.choice(['Low','Medium','High'],N).tolist(),
        'D': np.random.normal(100, 10, size=(N)).tolist()
        })
df.head(2)

for col in df:
    print(col)
#iteritems() − to iterate over the (key,value) pairs
data = pd.DataFrame(np.random.rand(4,3), columns = ['col1','col2','col3'])

for key,value in data.iteritems():
    #print("Key=" + key + " value =" + value)
    print(value)
    
for row_index,row in data.iterrows():
    print(row_index)
    print(row)
    
for row in df.itertuples():
    print(row)