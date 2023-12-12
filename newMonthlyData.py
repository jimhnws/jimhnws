#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import urllib
import requests
import csv


# In[156]:


import pandas as pd
import calendar

#
# Read JSON request into a pandas Dataframe
#

colNames = ['index', 'Rain', 'HiTemp', 'LowTemp', 'Year', 'Month', 'Day']
df = pd.read_json('/var/www/html/000/monthly.txt')
df = df.drop(df.columns[[0]], axis=1)

#
# Get month name from month number and make some conversions 
#

Date = (df['Day']).astype(int)
month_num  = (df['Month']).astype(int)
month_num = month_num[0]
month_name = calendar.month_name[month_num]
Year = (df['Year']).astype(int)
year = Year[0]

High = (df['HiTemp']).round(0).astype(int)
Low = (df['LowTemp']).round(0).astype(int)
Avg = ((High + Low)/2).round(0).astype(int)
HDD = (65 - Avg).round(0).astype(int)
HDD = HDD.where(HDD > 0, 0) 
CDD = (Avg - 65).round(0).astype(int)
CDD = CDD.where(CDD > 0, 0) 
Rainfall = (df['Rain']).astype(float).fillna(0)

month_High_avg = High.mean().round(1) 
month_Low_avg = Low.mean().round(1) 
month_avg = Avg.mean().round(1)
totHDD = HDD.sum()
totCDD = CDD.sum()
totRainfall = Rainfall.sum().round(2)

df.insert(6, 'Average', Avg)
df.insert(7, 'HDD', HDD)
df.insert(8, 'CDD', CDD)
df.insert(9, 'High', High)
df.insert(10, 'Low', Low)
df.insert(11, 'Rainfall', Rainfall)
df.insert(12, 'Date', Date)

df = df.reindex(columns=['Year', 'Month', 'Date', 'High', 'Low', 'Average', 'HDD', 'CDD','Rainfall'])
df = df.drop(df.columns[[0,1]], index = None, axis=1)


# In[162]:


from pretty_html_table import build_table

html_table_blue_light = build_table(df, 'blue_light', text_align='center')

with open('/var/www/html/000/monthlyTable.html', 'w') as f:
    f.write(html_table_blue_light)

