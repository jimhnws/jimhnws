#!/usr/bin/env python
# coding: utf-8

# In[1]:


import getDays
import daysAndDates

#
# Calculating some date/time stuff
#

dayInfo = daysAndDates.daysAndDates()
month, month_num, date, year = dayInfo[0], dayInfo[1], dayInfo[2], dayInfo[3]
yesterday = int(dayInfo[4])
nextDay = int(dayInfo[5])
month_num = int(month_num)
date = int(date)


# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import datetime
from datetime import datetime
import sqlalchemy
import mysql.connector
import sqlite3
import getDays
import pymysql as dbapi

#
# Now the Tempest F6 table
#

QUERY = """SELECT * FROM tempestCompF6 
           WHERE month = %s""" % (month_num)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'tempestf6')

cur = db.cursor()
cur.execute(QUERY)
records = cur.fetchall()

qwe = ['Davis']

if qwe == 'Davis':
        df = pd.DataFrame(records, columns = ['index', 'Year', 'Month', 'Date', 'High', 'Low', 'Average', 'HDD', 'CDD','Rainfall', 'Max_Dew_Point'])
        df = df.drop(df.columns[[0,6,7]], axis=1)
else:
        df = pd.DataFrame(records, columns = ['index', 'Year', 'Month', 'Date', 'High', 'Low', 'Average', 'HDD', 'CDD', 'totR', 'corR', 'Lightning1_5', 'Lightning6_10'])
        df = df.drop(df.columns[[0,4,5,6,7,8,11,12]], axis=1)    
        
        
print(df)        


# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import datetime
import plotly.express as px
import plotly.graph_objs as go

df['Date'] = df['Date'].astype(int)
df['totR'] = df['totR'].astype(float)
df['corR'] = df['corR'].astype(float)
    
TOTR = df['totR']
CORR = df['corR']
DATE = df['Date']

y = TOTR.to_numpy()
y1 = CORR.to_numpy()
x = DATE.to_numpy()

fig = px.bar(
data_frame = df,
x = "Date",
y = [y, y1],       
orientation = "v",
barmode = 'group',
color_discrete_sequence=['red', 'green'], 
   
)

fig.update_layout(
title = f'{month} {year}  - Tempest Tabulated vs Corrected',
yaxis_title = "Rainfall (inches)", title_x = 0.5,  
xaxis = dict(
tickmode = 'linear',
tickfont = dict(size = 16), 
tick0 = 1,
dtick = 1),
legend_title = "Rainfall", 
    
)

#fig.write_html(f'/Users/jameshayes/Sites/tempestComp.html', auto_open = True)   
fig.write_html(f'/var/www/html/000/tempestComp.html', auto_open = True)   


# In[ ]:




