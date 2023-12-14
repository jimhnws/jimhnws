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
print(df)
if df.empty:
    print("The dataset is empty")
    Image2 = Image.open('/var/www/html/000/allInOne.png')
    Image2copy = Image2.copy()
    Image1 = Image.open('/var/www/html/000/NoData.png')
    Image1copy = Image1.copy()
    Image2copy.paste(Image1copy, (0, 0))
    Image1copy.save('/var/www/html/000/allInOne.png')     
    
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
month_abbrev = month_name[0:3]
Year = (df['Year']).astype(int)
year = Year[0]

#
# Calculate the last day of each month
#

lastDay = calendar.monthrange(year,month_num)
lastDay1 = lastDay[1]

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


'''
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
plt.locator_params(axis = 'x', nbins = lastDay1)
plt.xlim(1, lastDay1)
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
'''


# In[178]:


'''
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
    plt.locator_params(axis = 'x', nbins = lastDay1)
    plt.xlim(1, lastDay1)
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
'''    


# In[ ]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = go.Figure()
fig.add_trace(go.Bar(
       x=df['Date'],
       y=df['Rainfall'],
       name="Rainfall",
       yaxis='y2',
       opacity=0.8,
       marker = {'color' : 'darkgreen'}))

fig.add_trace(go.Scatter(
       x=df['Date'],
       y=df['High'],
       name="High",
       marker = {'color' : 'red'},
       yaxis='y', 
       line = {'width': 4} ))

fig.add_trace(go.Scatter(
       x=df['Date'],
       y=df['Low'],
       name="Low",
       marker = {'color' : 'blue'},
       yaxis='y',
       line = {'width': 4}))    

fig.update_layout(
       autosize=False,
       width=1000,
       height=600,
       plot_bgcolor='white',
       title_text = f'{month_name} {year}', title_x = 0.5, title_font_family = "Arial Black",
       yaxis=dict(
        title="Temperature (F)",
          range = [-15,110],  
        tick0 = 0,
        dtick = 10,  
        titlefont=dict(
            color="black"
        ),
        tickfont=dict(
            color="black",
            size = 14, 
          
        )
    ),
       yaxis2=dict(
        title="Rainfall (inches)",
        titlefont=dict(
            color="black"
        ),
        tickfont=dict(
            color="black"
        ),
        anchor="free",
        side="right",
        overlaying = "y",    
        position=1.0),
       
       xaxis = dict(
        title="Date",
        titlefont=dict(
            color="black"
        ),   
        tickmode = 'linear',
        tickfont = dict(size = 14), 
        tickfont_family="Arial Black",
        tick0 = 1,
        dtick = 1),
    
      legend=dict(
#            yanchor="top",
#            y=0.99,
#            xanchor="left",
#            x=0.01,
#            bordercolor="Black",
#            borderwidth=1
    
            orientation="h",
            entrywidth=70,
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=1
))                
 
fig.update_xaxes(showline=True, linewidth=1.5, linecolor='black', 
               )
fig.update_yaxes(showline=True, linewidth=1.5, linecolor='black', 
               )

fig.write_html(f'/var/www/html/000/allInOne.html', auto_open = True)    
fig.write_image(f'/var/www/html/000/allInOne.png', engine="kaleido")

