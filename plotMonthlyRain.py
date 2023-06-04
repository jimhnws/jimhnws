#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plot
import matplotlib.colors as mcolors
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
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
        
        
    print(date,r)    
    
    wxdata = f'{path}{month_name}_{year}_{qwe}.xlsx'
    df = pd.read_excel(wxdata, skiprows=[0,1])
        
    if qwe == 'Tempest':
        df = df.drop(df.columns[[1,2,3,4,5,8,9]], axis=1)
        df = df.drop(df.index[date:r+1]) 
        df['Date'] = df['Date'].astype(int)
        df.plot(kind="bar", x = "Date", rot = 0, width = 0.9, color={"totR": "green", "corR": "red"} )
    else:
        df = df.drop(df.columns[[1,2,3,4,5,7,8,9,10,11,12,13,14]], axis=1)
        df = df.drop(df.index[date:r+1])
        df['Date'] = df['Date'].astype(int)
        df.plot(kind="bar", x = "Date", rot = 0, width = 0.9, color={"Rainfall": "green"} )
        
    
    plot.tick_params(axis='x', colors='black', direction='out', length=4, width=1)
    plot.locator_params(axis='x', nbins= r)
    plot.figsize = (10,6)
    plot.ylim(0, 3)
    plot.grid(axis = "y", linewidth = 1.0, color = 'black')
    plot.xticks(fontsize=8)
    plot.xlabel('Date', fontsize=12, fontweight ='bold')
    plot.yticks(fontsize=12)
    plot.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
    plot.title(f'{month_name} {year} Rainfall - {qwe}', fontsize=12, fontweight ='bold')
    plot.savefig(f'{path1}rainfall_{qwe}')
    


# In[ ]:




