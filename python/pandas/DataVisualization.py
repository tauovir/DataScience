# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
list1 = [
        [10,5,15,9],
        [4,10,78,6],
        [25,12,47,16],
        [10,11,12,50],
        [13,1,15,25],
        [1,12,35,15],
        [1,16,10,14],
        [11,1,15,25],
        [1,4,5,7],
        [13,1,11,25]
        ]
data = pd.DataFrame(np.random.randn(10,4), index = pd.date_range('1/1/2000',periods = 10), columns = list('ABCD'))
data = pd.DataFrame(np.random.randn(10,4), index = [0,1,2,3,4,5,6,7,8,9], columns = list('ABCD'))
data22 = pd.DataFrame(list1, index = [0,1,2,3,4,5,6,7,8,9], columns = list('ABCD'))

data.plot()
data.A.plot()   #data['A'].plot()
data[['A','B']].plot()

data.plot.line()
data.plot.scatter(data['A'], data['B'])

# Barr Chart
data.plot.bar()
data.plot.bar(stacked = True)
data.plot.barh(stacked=True)

# HistoGram
data1 = pd.DataFrame({'a': np.random.randn(1000)+1,'b' : np.random.randn(1000),'c': np.random.randn(1000)-1},
                      columns = list('abc'))

data1.plot.hist(bins = 20)
data1.diff().hist(bins = 20)

# Box Plot
#Box Plot:L Max, min, median, Third quarterli, first quarterl
data22.plot.box()
data22['A'].median()

# Areac Char
data22.plot.area()


# Scatter Plot
data.plot.scatter(x = 'A', y = 'B', style = 'b')
data.plot.line()

ax = data.plot.scatter(x = 'A', y = 'B', style = 'b')
data.plot.line(x = 'A', y = 'B',ax=ax, style = 'b')


df = pd.DataFrame([[1,2],[10,20]])
ax = df.plot.scatter(x=0, y=1, style='b')
df.plot.line(x=0, y=1, ax=ax, style='b')

# Pie Chart 
data22.plot.pie(subplots = True)    # Pie Char does not allow negatie value






