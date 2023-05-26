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


# In[6]:


path = '/home/ec2-user/'
path1 = '/var/www/html/000/'

xr = calcTimeNow.calcTimeNow()
month_name, year, date = xr[1], xr[2],xr[3]
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

for monther in months:
    
    month31 = ['January','March', 'May', 'July', 'August', 'October', 'December']
    month30 = ['April', 'June', 'September', 'November']
    month28 = ['February']
 
    if monther in month31:
        r = 31
    elif monther in month30:
        r = 30 
    elif monther in month28:
        if leap_year:
            r = 29
        else:
            r = 28
    else:
        r = 31
    
print(date,r)
    
wxdata1 = f'{path}{month_name}_{year}_Tempest.xlsx'
wxdata = f'{path}{month_name}_{year}_Davis.xlsx'
df = pd.read_excel(wxdata1, skiprows=[0,1])
df = df.drop(df.columns[[1,2,3,4,5,8,9]], axis=1)
df = df.drop(df.index[date:r]) 

df1 = pd.read_excel(wxdata, skiprows=[0,1])
df1 = df1.drop(df1.columns[[1,2,3,4,5,7,8,9,10,11,12,13,14]], axis=1)
df1 = df1.drop(df1.index[date:r])              
    
df2 = pd.merge(df,df1, on='Date')
df2 = df2.drop(df2.columns[[1]], axis = 1)
print(df2)

df2.plot(kind="bar", x = "Date", rot = 0, color={"Rainfall": "green", "corR": "red"})

plot.figsize = (10,6)
plot.grid(axis = "y", linewidth = 1.0, color = 'black')
plot.xticks(fontsize=10)
plot.xlabel('Date', fontsize=12, fontweight ='bold')
plot.yticks(fontsize=12)
plot.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
plot.title(f'{month_name} {year} Rainfall - Davis vs Tempest', fontsize=12, fontweight ='bold')
plot.savefig(f'{path1}rainfall_DavisTempest')
        


# In[ ]:





# In[ ]:




