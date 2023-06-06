#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import calcTimeNow
import month_Days


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
    
    # figure out the month number
    months = ['January','February', 'March','April','May','June','July','August','September','October','November','December']

    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False

    month31 = ['January','March', 'May', 'July', 'August', 'October', 'December']
    month30 = ['April', 'June', 'September', 'November']
    month28 = ['February']
 
    if month_name in month31:
        r = 31
    elif month_name in month30:
        r = 30 
    elif month_name in month28:
        if leap_year:
            r = 29
        else:
            r = 28
    else:
        r = 31           
        
      
    x_indexes = np.arange(1, r+1)
    print(x_indexes)
    height = 0.0
    width = 0.25
    
    wxdata = f'{path}{month_name}_{year}_{qwe}.xlsx'
    df = pd.read_excel(wxdata, skiprows=[0,1])
        
    if qwe == 'Tempest':
        df = df.drop(df.columns[[1,2,3,4,5,8,9]], axis=1)
        df = df.drop(df.index[date:r+1]) 
        df['Date'] = df['Date'].astype(int)
        #df.plot(kind="bar", x = "Date", rot = 0, width = 0.9, color={"totR": "green", "corR": "red"} )
        plt.bar(x_indexes, height, color ='red', width = width, label = "Corrected")
        plt.bar(x_indexes + width, height, color ='green', width = width, label = "Tabulated")
        
    else:
        df = df.drop(df.columns[[1,2,3,4,5,7,8,9,10,11,12,13,14]], axis=1)
        df = df.drop(df.index[date:r+1])
        df['Date'] = df['Date'].astype(int)
        #df.plot(kind="bar", x = "Date", rot = 0, width = 0.9, color={"Rainfall": "green"})    
        plt.bar(x_indexes + width, height, color ='green', width = width)     
    
    
    plt.locator_params(axis='x', nbins= r)
    plt.tick_params(axis='x', colors='black', direction='out', length=4, width=1)
    plt.figsize = (10,6)
    plt.locator_params(axis='x', nbins= r)
    plt.xlim(1, r)
    plt.ylim(0, None)
    plt.grid(axis = "y", linewidth = 1.0, color = 'black')
    plt.xticks(fontsize=8)
    plt.xlabel('Date', fontsize=12, fontweight ='bold')
    plt.yticks(fontsize=12)
    plt.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
    plt.legend()
    plt.title(f'{month_name} {year} Rainfall - {qwe}', fontsize=12, fontweight ='bold')
    plt.savefig(f'{path1}rainfall_{qwe}')
    


# In[ ]:




