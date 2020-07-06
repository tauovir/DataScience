# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

print(pd.date_range('1/1/2014',periods = 5))
print(pd.date_range('1/1/2014',periods = 5, freq = 'm'))

#
start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)
print(pd.date_range(start, end))
