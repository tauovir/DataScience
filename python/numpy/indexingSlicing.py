
# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(10)
a
s = slice(2,7,2)    #start, stop, and step values 2, 7, and 2 respectively
print(a[s])
# same result can be found as
print(a[2:7:2])
print(a[5])
print(a[2:])
print(a[2:5])

#===========================
data = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(data[1:])

# Elipsis
"""
Slicing can also include ellipsis (…) to make a selection tuple of the same length as the dimension of an array.
If ellipsis is used at the row position,it will return an ndarray comprising of items in rows.
"""
print(data)

print("The item in second Column")
print(data[...,1])
# Now we will slice all items from the second row 
print('The items in the second row are:' )
print(data[1,...])
