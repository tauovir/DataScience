import pandas as pd
import numpy as np
serl = pd.Series(['Tom','William Rick','John','Albert@t',np.nan,'123','khan'])
print(serl)
print(serl.str.lower())
print(serl.str.upper())
print(serl.str.len())


s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s)
print ("After Stripping:")
print (s.str.strip())
print (s.str.split(' '))
print (s.str.cat(sep = '_'))

"""
data = pd.DataFrame({
        'Age' : [20,30,50,60,45],
        'Gender' : ['Male','Female','Male','Female','Male'],
        'Salary' : [25000,35000,60000,40000,55000]
        }
        )
"""
print (s.str.get_dummies())
print(s)

print(s.str.contains(' '))

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s)

print ("After replacing @ with $:")
print(s.str.replace('@','$'))
print(s.str.swapcase())
print(s.str.islower())
print(s.str.methods)
print(dir(s.str)) # Check all Method In librara



