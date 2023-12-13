#!/usr/bin/env python
# coding: utf-8

# In[165]:


import json
import urllib
import requests
import csv


# In[174]:


import pandas as pd
import calendar
from PIL import Image
from pretty_html_table import build_table
import sys

#
# Read JSON request into a pandas Dataframe
#

colNames = ['index', 'Rain', 'HiTemp', 'LowTemp', 'Year', 'Month', 'Day']
df = pd.read_json('/var/www/html/000/monthly.txt')
if df.empty:
    Image2 = Image.open('/var/www/html/000/monthlyRain_db.png')
    Image2copy = Image2.copy()
    Image1 = Image.open('/var/www/html/000/NoRain.png')
    Image1copy = Image1.copy()
    Image2copy.paste(Image1copy, (0, 0))
    Image1copy.save('/var/www/html/000/monthlyRain_db.png')
    
    Image4 = Image.open('/var/www/html/000/monthlyTemps_db.png')
    Image4copy = Image4.copy()
    Image3 = Image.open('/var/www/html/000/NoTemps.png')
    Image3copy = Image3.copy()
    Image4copy.paste(Image1copy, (0, 0))
    Image3copy.save('/var/www/html/000/monthlyTemps_db.png')
    
    with open('/var/www/html/000/monthlyTable.html', 'w') as f:
    #with open('/Users/jameshayes/monthlyTable.html', 'w') as f:
        html_table_blue_light = build_table(df, 'blue_light', text_align='center')
        f.write(html_table_blue_light)    
        
    sys.exit()    

#df = pd.read_json('/Users/jameshayes/monthly.txt')
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
totRainfall = Rainfall.sum().round(2)

month_High_avg = High.mean().round(1) 
month_Low_avg = Low.mean().round(1) 
month_avg = Avg.mean().round(1)
totHDD = HDD.sum()
totCDD = CDD.sum()

df.insert(6, 'Average', Avg)
df.insert(7, 'HDD', HDD)
df.insert(8, 'CDD', CDD)
df.insert(9, 'High', High)
df.insert(10, 'Low', Low)
df.insert(11, 'Rainfall', Rainfall)
df.insert(12, 'Date', Date)

df = df.reindex(columns=['Year', 'Month', 'Date', 'High', 'Low', 'Average', 'HDD', 'CDD','Rainfall'])
df = df.drop(df.columns[[0,1]], index = None, axis=1)


# In[175]:


from pretty_html_table import build_table

if year < 1989:
    Rainfall = (df['Rainfall']).astype(float).fillna("M")
else:
    Rainfall = (df['Rainfall']).astype(float).fillna(0)

html_table_blue_light = build_table(df, 'blue_light', text_align='center')

with open('/var/www/html/000/monthlyTable.html', 'w') as f:
#with open('/Users/jameshayes/monthlyTable.html', 'w') as f:
    f.write(html_table_blue_light)    


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
    
HI = df['High']
LO = df['Low']
DAY = df['Date']

y = HI.to_numpy()
y1 = LO.to_numpy()
x = DAY.to_numpy()
            
plt.style.use('seaborn-v0_8-white')
    
path1 = '/var/www/html/000/'
plt.figure(figsize= (6,4))
plt.locator_params(axis = 'x', nbins = 31)
plt.xlim(1,31)
plt.ylim(-15, 110)
plt.xticks(fontsize=10, rotation='vertical')
plt.xlabel('Date', fontsize=10, fontweight ='bold')
plt.yticks(fontsize=12)
plt.ylabel('Temperature (F)', fontsize=10, fontweight ='bold')
plt.locator_params(axis='y', nbins=20)
plt.title(f'{month_name} {year} Temperatures', fontsize=12, fontweight ='bold')
#plt.grid(axis = "y", linewidth = 1.0, color = 'gray')
#plt.grid(axis = "x", linewidth = 1.0, color = 'gray')   
plt.plot(x, y, color = "red", linewidth =3, label ="High")
plt.plot(x, y1, color = "blue", linewidth =3, label ="Low")
plt.legend(fontsize = 12)
plt.savefig(f'{path1}monthlyTemps_db')
#plt.show()


# In[177]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import datetime
from PIL import Image

print(year)

if year < 1989:
    Image2 = Image.open('/var/www/html/000/monthlyRain_db.png')
    Image2copy = Image2.copy()
    Image1 = Image.open('/var/www/html/000/NoRain.png')
    Image1copy = Image1.copy()
    Image2copy.paste(Image1copy, (0, 0))
    Image1copy.save('/var/www/html/000/monthlyRain_db.png')
    
else:    

    path1 = '/var/www/html/000/'

    df['Rainfall'] = df['Rainfall'].astype(float)
    
    RAINFALL = df['Rainfall']
    DATE = df['Date']

    y = RAINFALL.to_numpy()
    x = DATE.to_numpy()

    plt.style.use('seaborn-v0_8-white')
    
    plt.figure(figsize= (6,4))
    plt.locator_params(axis = 'x', nbins = 31)
    plt.xlim(1, 31)
    plt.xticks(fontsize=10, rotation='vertical') 
    plt.xlabel('Date', fontsize=12, fontweight ='bold')
    plt.yticks(fontsize=12)
    plt.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
    plt.locator_params(axis='y', nbins=20)
    plt.title(f'{month_name} {year} Rainfall', fontsize=12, fontweight ='bold')
    #plt.grid(axis = "y", linewidth = 1.0, color = 'gray')
    #plt.grid(axis = "x", linewidth = 1.0, color = 'gray')

    plt.bar(df['Date'], df['Rainfall'], color ='green', width = 0.7)
    plt.autoscale(enable = True, axis = 'y', tight = True)
    #plt.legend(fontsize = 12)
    plt.savefig(f'{path1}monthlyRain_db')
    #plt.show()


# In[ ]:




