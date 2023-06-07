#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import calcTimeNow
import getDaysInMonth


# In[1]:


# Determine the date

path = '/home/ec2-user/'
path1 = '/var/www/html/000/'

sta = ['Tempest', 'Davis']

for qwe in sta:

    xr = calcTimeNow.calcTimeNow()
    month_name = calcTimeNow.calcMonthNow()
    year, date = xr[2],xr[3]
    year = int(year)
    date =  int(date)
    date = date - 1
    
    r = getDaysInMonth.getDaysInMonth()
    x_indexes = np.arange(1, r)
    height = 0.0
    width = 0.25
    
    wxdata = f'{path}{month_name}_{year}_{qwe}.xlsx'
    df = pd.read_excel(wxdata, skiprows=[0,1])
        
    if qwe == 'Tempest':
        df = df.drop(df.columns[[1,2,3,4,5,8,9]], axis=1)
        df = df.drop(df.index[date:r]) 
        df['Date'] = df['Date'].astype(int)
        plt.bar(x_indexes, height, color ='red', width = width, label = "Corrected")
        plt.bar(x_indexes + width, height, color ='green', width = width, label = "Tabulated")
        
    else:
        df = df.drop(df.columns[[1,2,3,4,5,7,8,9,10,11,12,13,14]], axis=1)
        df = df.drop(df.index[date:r])
        df['Date'] = df['Date'].astype(int)
        plt.bar(x_indexes + width, height, color ='green', width = width)     
    
    
    plt.figsize = (10,6)
    plt.locator_params(axis='x', nbins= r)
    plt.tick_params(axis='x', colors='black', direction='out', length=4, width=1)
    plt.locator_params(axis='x', nbins= r)
    plt.xlim(1, r)
    plt.xticks(fontsize=8)
    
    plt.xlabel('Date', fontsize=12, fontweight ='bold')
    plt.ylim(0, None)
    plt.grid(axis = "y", linewidth = 1.0, color = 'black')
    plt.yticks(fontsize=12)
    plt.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
    plt.legend()
    plt.title(f'{month_name} {year} Rainfall - {qwe}', fontsize=12, fontweight ='bold')
    plt.savefig(f'{path1}rainfall_{qwe}')    


# In[ ]:




