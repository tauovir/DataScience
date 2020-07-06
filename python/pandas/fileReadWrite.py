# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv("insurance.csv")
#data1 = pd.read_csv("insurance.csv", index_col='rr')
#help(pd.read_csv)
data1 = pd.read_csv("insurance.csv", dtype = {'children' :  np.float32})

# Headred Name
data2 = pd.read_csv("insurance.csv", names = list('abcdefg'))
data2['a'][0]

#skiprows : skiprows skips the number of rows specified.
data3=pd.read_csv("insurance.csv", skiprows=2)
