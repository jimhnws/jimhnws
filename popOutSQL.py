#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import dataFile
import getNameNumbers
import sqlalchemy
import mysql.connector
import sqlite3

path = '/tmp/'
path1 = '/home/ec2-user/'
file_name = 'test12114.csv'
data_file = f'{path}{file_name}'
df = pd.read_csv(data_file, index_col=False, sep = ';', names = ['id', 'Year', 'Month', 'Date', 'Hour', 'temperature'])
df = df.drop(df.columns[[0]], axis = 1)
print(df)


