#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import calcTimeNow
import getDaysInMonth


# In[3]:


path = '/home/ec2-user/'
path1 = '/var/www/html/000/'

# Defining some variables
xr = calcTimeNow.calcTimeNow()
month_name = calcTimeNow.calcMonthNow()
year, date = xr[2],xr[3]
year = int(year)
date =  int(date)
date = date - 1

####################################
r = getDaysInMonth.getDaysInMonth()     
x_indexes = np.arange(1, r + 1)
height = 0.0
width = 0.25     

# Working with the Panda dataframes
wxdata1 = f'{path}{month_name}_{year}_Tempest.xlsx'
wxdata = f'{path}{month_name}_{year}_Davis.xlsx'

df = pd.read_excel(wxdata1, skiprows=[0,1])
df = df.drop(df.columns[[1,2,3,4,5,6,8,9]], axis=1)
df = df.drop(df.index[date:r]) 

df1 = pd.read_excel(wxdata, skiprows=[0,1])
df1 = df1.drop(df1.columns[[1,2,3,4,5,7,8,9,10,11,12,13,14]], axis=1)
df1 = df1.drop(df1.index[date:r])              

df2 = pd.merge(df,df1, on='Date')
df2['Date'] = df2['Date'].astype(int)

# Settings for plotting the rainfall
plt.bar(x_indexes, height, color ='red', width = width, label = 'corR')
plt.bar(x_indexes + width, height, color ='green', width = width, label = 'Rainfall')

plt.figsize = (10,6)
plt.tick_params(axis='x', colors='black', direction='out', length=4, width=1)
plt.locator_params(axis='x', nbins= r)
plt.xlim(1, r)
plt.xticks(fontsize=8)
plt.xlabel('Date', fontsize=12, fontweight ='bold')
plt.grid(axis = "y", linewidth = 1.0, color = 'black')
plt.ylim(0, None)

plt.yticks(fontsize=12)
plt.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
plt.legend()
plt.title(f'{month_name} {year} Rainfall - Davis vs Tempest', fontsize=12, fontweight ='bold')
plt.savefig(f'{path1}rainfall_DavisTempest')   


# In[ ]:





# In[ ]:




