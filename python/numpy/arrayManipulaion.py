# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

num = np.arange(30)
arr = num.reshape(10,3)
flt = arr.flat[5]

arr1 = np.arange(30).reshape(10,3)
ravel = arr1.ravel()    # Ravel


# numpy hstack
a1 = np.arange(4).reshape(2,2)
print("Print First row")
print(a1)
b1 = np.array([[50,60],[70,80]])
print("Second Array")
print(b1)

print("Horizontal Stacking")
c = np.hstack((a1, b1)) # it will append b1 matrix row wise
c1 = np.vstack((a1, b1))    # it will append b1 matrix columns wise
print('Stack the two arrays along axis 0:' )
print(np.stack((a1,b1),1))

# Concate
print("Concating")
print(np.concatenate((a1,b1)))
