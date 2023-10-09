#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import datetime
from datetime import datetime
import sqlalchemy
import mysql.connector
import sqlite3
import pandas as pd
import getDays

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
nextDay = tomorrowInfo[2]
nextDay = int(nextDay)

#
# Get data from the table
#

mydb = mysql.connector.connect(
  host="3.135.162.69",
  user="chuckwx",
  password="jfr716!!00"    
)

mycursor = mydb.cursor()

mycursor.execute("use davisf6;")
pop1 = ("select * from davisTest order by id DESC LIMIT 1;")
mycursor.execute(pop1)
records = mycursor.fetchall()

#
# Dump the data into a pandas DataFrame
#

df = pd.DataFrame(records, columns = ['index', 'Year', 'Month', 'Date', 'High', 'Low', 'Rainfall', 'Max_Dew_Point'])
df


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import numpy as np
import getDays
import seaborn as sns

sta = ['Davis']

for qwe in sta:        
       
    df['Date'] = df['Date'].astype(int)
        
    HI = df['High']
    LO = df["Low"]
    RAINFALL = df["Rainfall"]
    DATE = df["Date"]
    
    y = HI.to_numpy()
    y1 = LO.to_numpy()
    x = DATE.to_numpy()     
    rainfall = RAINFALL.to_numpy()
        
    path1 = '/var/www/html/trclimate/'
        
    plt.style.use('fivethirtyeight')               
       
    plt.figure(figsize= (10,6))
    plt.xticks(fontsize = 12)
    plt.xlabel('Date', fontsize=12, fontweight ='bold')    
    plt.grid(True)
    plt.autoscale(enable = True, axis = 'both', tight = True)
    plt.grid(axis = "y", linewidth = 2.0, color = 'black')
    sns.barplot(data = df, x = 'Date', y = 'Rainfall', color = 'g')
    plt.ylabel('Rainfall (inches)', fontsize=12, fontweight ='bold')
    plt.title(f'{month} {year} Rainfall', fontsize=12, fontweight ='bold')
    
    
    plt.savefig(f'{path1}Rain_test_{qwe}')  


# In[ ]:




