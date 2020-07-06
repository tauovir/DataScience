# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

a = np.arange(0,60,5)
a = a.reshape(3,4)
a
print("================")
for x in np.nditer(a):
    print(x)

trans = a.T
trans
for x in np.nditer(trans):
    print(x)

# Iteration Order

print("Sorted in C-style order")
c = .copy(order = 'C')
c

for x in np.nditer(c):
    print(x)

print("Sorted in F-style order")
c = trans.copy(order = 'F')
c

for x in np.nditer(c):
    print(x)

# Use explicit condition
a
print("Sorted in C-style order")
for x in np.nditer(a, order = 'C'): 
    print(x)

# Modifying Array
print("Sorted in C-style order")
for x in np.nditer(a, op_flags = ['readwrite']): 
    x[...] = 2*x
a

for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print(x)

list = ['a','e','i','o','u']
print(list[8:])

