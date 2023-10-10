#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd
import datetime
from datetime import datetime
import sqlalchemy
import mysql.connector
import sqlite3
import pandas as pd
import getDays
import pymysql as dbapi

#
# Get some time/date info
#

todayInfo = getDays.getToday()
yesterdayInfo = getDays.getYesterday()
print(todayInfo)
print(yesterdayInfo)
tomorrowInfo = getDays.getTomorrow()

month, month_num, date, year = todayInfo[0], todayInfo[1], todayInfo[2], todayInfo[3]
yesterday = yesterdayInfo[2]
yesterday = int(yesterday)
month_num = int(month_num)
print(month_num)
nextDay = tomorrowInfo[2]
nextDay = int(nextDay)
date = int(date)

#
# Get data from the table
#

QUERY = """SELECT * FROM davisF6 
           WHERE month = %s""" % (month_num)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'davisf6')

cur = db.cursor()
cur.execute(QUERY)
records = cur.fetchall()

#
# Dump the data into a pandas DataFrame
#

df = pd.DataFrame(records, columns = ['index', 'Year', 'Month', 'Date', 'High', 'Low', 'Rainfall', 'Max_Dew_Point'])
print(df)


# In[118]:


import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import getDays
import numpy as np

sta = ['Davis']

for qwe in sta:        
       
    df['Date'] = df['Date'].astype(int)    
    df['High'] = df['High'].astype(int) 
    df['Low'] = df['Low'].astype(int) 
        
    HI = df['High']
    LO = df["Low"]
    DATE = df["Date"]

    y = HI.to_numpy()
    y1 = LO.to_numpy()
    x = DATE.to_numpy()
    
    print(x, y, y1)
            
    path1 = '/var/www/html/trclimate/'
        
    plt.style.use('fivethirtyeight')                       
    plt.figure(figsize = (10,6))
            
    plt.xticks(fontsize = 12)
    plt.xlabel('Date', fontsize=12, fontweight = 'bold')
    plt.locator_params(axis = 'x', nbins = date)
    plt.xlim(1, date - 1)
        
    plt.ylim(0, 105)
    plt.yticks(fontsize = 12)
    plt.ylabel('Temperature (F)', fontsize = 12, fontweight ='bold')
    plt.locator_params(axis = 'y', nbins = 20)
    plt.title(f'{month} {year} Temperatures', fontsize=12, fontweight ='bold')
    plt.grid(True)
    #plt.autoscale(enable = True, axis = 'y', tight = True)
    plt.grid(axis = "y", linewidth = 2.0, color = 'black')
    
    plt.plot(x, y, marker = "x", color = "red", linewidth =3, label ="High")
    plt.plot(x, y1, marker = "x", color = "blue", linewidth =3, label ="Low")      
    plt.legend(fontsize = 12)
    plt.savefig(f'{path1}Temps_test_{qwe}')  
    


# In[ ]:




