# -*- coding: utf-8 -*-
import pandas as pd
import xlrd
df=pd.read_csv('tm1.csv',index_col='name')
#df=pd.read_csv('tm1.csv')
print df.describe()