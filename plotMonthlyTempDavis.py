#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import calcTimeNow
import getDaysInMonth


# In[2]:


#
# Make some graphs - temperature line plots first
# For just one month
#

# Determine the date

sta = ['Davis']

for qwe in sta:

    x = calcTimeNow.calcTimeNow()
    month_name = calcTimeNow.calcMonthNow()
    year, date = x[2],x[3]
    year = int(year)
    date =  int(date)
    date = date - 1
    r = getDaysInMonth.getDaysInMonth()   
    print(r)    
    
    path = '/home/ec2-user/'
    wxdata = f'{path}{month_name}_{year}_{qwe}.xlsx'
    df = pd.read_excel(wxdata, skiprows=[0,1])
    if qwe == 'Davis':
        df = df.drop(df.columns[[3,4,5,6,7,8,9,10,11,12,13,14]], axis=1)
        
    else:
        df = df.drop(df.columns[[3,4,5,6,7,8,9]], axis=1)
        
       
    df = df.drop(df.index[date:r])
    df['Date'] = df['Date'].astype(int)
    
    HI = df['High']
    LO = df["Low"]
    DATE = df["Date"]

    y = HI.to_numpy()
    y1 = LO.to_numpy()
    x = DATE.to_numpy()
        
    #define x as 200 equally spaced values between the min and max of original x 
    xnew = np.linspace(x.min(), x.max(), 200) 

    #define spline
    HIspl = make_interp_spline(x, y, k=2)
    y_smooth = HIspl(xnew)
    LOspl = make_interp_spline(x, y1, k=2)
    y1_smooth = LOspl(xnew)
    
    path1 = '/var/www/html/trclimate/'
    
    plt.figure(figsize= (10,6))
    plt.locator_params(axis='x', nbins= r)
    plt.xlim(1, r)
    plt.xticks(fontsize=12)
    plt.xlabel('Date', fontsize=12, fontweight ='bold')
    
    plt.ylim(0, 105)
    plt.yticks(fontsize=12)
    plt.ylabel('Temperature (F)', fontsize=12, fontweight ='bold')
    plt.locator_params(axis='y', nbins=20)
    plt.title(f'{month_name} {year} Temperatures', fontsize=12, fontweight ='bold')
    plt.grid(True)
    #plt.grid(axis = "y", linewidth = 2.0, color = 'black')
    plt.plot(xnew, y_smooth, color = "red", linewidth =3, label ="High")
    plt.plot(xnew, y1_smooth, color = "blue", linewidth =3, label ="Low")
    plt.legend(fontsize=12)
    plt.savefig(f'{path1}tt_{qwe}')    


# In[ ]:




