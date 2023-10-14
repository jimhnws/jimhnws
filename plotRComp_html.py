#!/usr/bin/env python
# coding: utf-8

# In[32]:


import getDays

todayInfo = getDays.getToday()
yesterdayInfo = getDays.getYesterday()
tomorrowInfo = getDays.getTomorrow()

month, month_num, date, year = todayInfo[0], todayInfo[1], todayInfo[2], todayInfo[3]
yesterday = yesterdayInfo[2]
yesterday = int(yesterday)
month_num = int(month_num)
nextDay = tomorrowInfo[2]
nextDay = int(nextDay)
date = int(date)


# In[33]:


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
# First the Tempest F6 table
#

QUERY = """SELECT * FROM davisF6 
           WHERE month = %s""" % (month_num)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'davisf6')

cur = db.cursor()
cur.execute(QUERY)
records = cur.fetchall()

#
# Now the Davis F6 table
#

QUERY1 = """SELECT * FROM tempestF6 
           WHERE month = %s""" % (month_num)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'tempestf6')

cur = db.cursor()
cur.execute(QUERY1)
records1 = cur.fetchall()


# In[39]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

sta = ['Davis', 'Tempest']

for qwe in sta:
    print(qwe)
    
    #
    # Dump the data into a pandas DataFrame
    #

    if qwe == 'Davis':
        df = pd.DataFrame(records, columns = ['index', 'Year', 'Month', 'Date', 'High', 'Low', 'Rainfall', 'Max_Dew_Point'])
        df = df.drop(df.columns[[0,4,5,7]], axis = 1)
        df['Date'] = df['Date'].astype(int)
        df['Rainfall'] = df['Rainfall'].astype(float)
        r1 = df['Rainfall']              
        
    else:
        df = pd.DataFrame(records1, columns = ['index', 'Year', 'Month', 'Date', 'High', 'Low', 'totR', 'corR', 'Lightning1_5', 'Lightning6_10'])
        df = df.drop(df.columns[[0,4,5,6,8,9]], axis = 1) 
        df['Date'] = df['Date'].astype(int)
        df['corR'] = df['corR'].astype(float)
        r2 = df['corR']  
        
fig = px.bar(
data_frame = df,
x = "Date",
y = [r1, r2],       
orientation = "v",
barmode = 'group',
color_discrete_sequence=['red', 'green'], 
   
)

fig.update_layout(
title = f'{month} {year}  - Davis vs Tempest',
yaxis_title = "Rainfall (inches)", title_x = 0.5,  
xaxis = dict(
tickmode = 'linear',
tickfont = dict(size = 16), 
tick0 = 1,
dtick = 1),
legend_title = "Rainfall", 
    
)

fig.write_html(f'/var/www/html/000/newRComp.html', auto_open = True)   
#fig.write_html(f'/Users/jameshayes/Sites/newRComp_{qwe}.html', auto_open = True)


# In[ ]:




