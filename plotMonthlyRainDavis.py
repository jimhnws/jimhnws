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
import getDaysInMonth


# In[2]:


path = '/home/ec2-user/'
path1 = '/var/www/html/trclimate/'

sta = ['Davis']

for qwe in sta:

    xr = calcTimeNow.calcTimeNow()
    month_name = calcTimeNow.calcMonthNow()
    year, date = xr[2],xr[3]
    year = int(year)
    date =  int(date)
    date = date - 1
    
    r = getDaysInMonth.getDaysInMonth()
    print(r)    
              
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
        df.plot(kind="bar", x = "Date", rot = 0, width = 0.9, color={"Rainfall": 'green'})


# In[ ]:


#Plot the results in matplotlib
plot.figure(figsize=(10, 6))
plot.grid(True)
#plot.grid(axis = "y", linewidth = 2.0, color = 'black')
plot.locator_params(axis='x', nbins= r)
plot.xlim(1,r)
plot.ylim(0, None)
plot.xticks(fontsize=12)
plot.xlabel('Date', fontsize=12, fontweight ='bold')
plot.yticks(fontsize=12)
plot.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
plot.locator_params(axis='y', nbins=10)
plot.title(f'{month_name} {year} Rainfall', fontsize=12, fontweight ='bold')
plot.savefig(f'{path1}rain_{qwe}')

