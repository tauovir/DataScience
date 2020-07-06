# -*- coding: utf-8 -*-
import numpy as np
"""
This function is similar to numpy.array except for the fact that it has fewer parameters.
 This routine is useful for converting Python sequence into ndarray.
 numpy.asarray(a, dtype = None, order = None)
 """
 ## convert list to ndarray 
x = [1,2,3,4]
a = np.asarray(x, dtype = np.float)
a

x = (1,2,3)
a = np.asarray(x)
a

x1 = [(1,2,3),(4,5)]
a = np.asarray(x1)
print(a)


# From Buffer
s = " Hello Khan"
a = np.frombuffer(s, dtype = 'S1')
a

#
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print(x)
