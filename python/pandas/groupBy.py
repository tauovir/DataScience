# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dataSet = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
data = pd.DataFrame(dataSet)
data.Team
data['Rank']
data.groupby('Team') # It will return Object
print(data.groupby('Team').groups) # View Group Data


print(data.groupby(['Team','Year']).groups) # View Group Data

# Iterating Through Group
grouped = data.groupby('Team')
for name,group in grouped:
    print(name)
    print(group)

# Select Group
#Using the get_group() method, we can select a single group.
grouped = data.groupby('Team')
print(grouped.get_group('Royals'))

# Aggregation
#An aggregated function returns a single aggregated value for each group. Once the group by object is created, 
#several aggregation operations can be performed on the grouped data.
print(grouped['Points'].agg(np.mean))
print(grouped['Rank'].agg(np.max))
print(grouped.agg(np.size))
# Apply multiple function at once
print(grouped['Points'].agg([np.sum, np.mean, np.std]))

# Transformation
"""
Transformation on a group or a column returns an object that is indexed the same size of that is being grouped.
 Thus, the transform should return a result that is the same size as that of a group chunk.
"""
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))

# Filteration
print(data.groupby('Team').filter(lambda x: len(x) >= 3))


