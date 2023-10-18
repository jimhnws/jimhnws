#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import dataFile
import getNameNumbers
import sqlalchemy
import mysql.connector
import sqlite3

# creating connection
conn = mysql.connector.connect(
  host="3.135.162.69",
  user="chuckwx",
  password="jfr716!!00"
   
)

mycursor = conn.cursor()
mycursor.execute("USE hourlyt;")
pop1 = ("select * from testTempest order by id DESC LIMIT 25;")
#pop1 = ("select @startTime := timeStamp from testTempest order by id DESC LIMIT 1;")
#pop2 = ("SELECT @endTime := DATE_SUB(@startTime, INTERVAL 24 Hour);")
#pop3 = ("SELECT * from testTempest WHERE timeStamp BETWEEN @endTime AND @startTime;")
#popSelect = pop1 + pop2 + pop3

mycursor.execute(pop1)
hours = mycursor.fetchall()

colNames = ['index', 'dtg', 'hourLocal', 'temp']
df = pd.DataFrame(hours, columns = colNames)
df = df.drop(df.columns[[0, 1]], axis = 1)
df = df.iloc[::-1]


# In[58]:


import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns

df['temp'] = df['temp'].astype(int)
df['hourLocal'] = df['hourLocal'].astype(str)

t = df['temp']
y = t.to_numpy()
hour = df['hourLocal']
x = hour.to_numpy()

sns.set_style('darkgrid')
    
path1 = '/var/www/html/000/'
plt.figure(figsize= (10,6))
plt.xticks(fontsize = 9, rotation = 45, fontweight = 'bold')
plt.ylabel('Temperature (F)', fontsize=12, fontweight ='bold')
plt.yticks(fontsize = 12, fontweight = 'bold')
plt.grid(axis = "y", linewidth = 1.0, color = 'gray')
plt.grid(axis = "x", linewidth = 1.0, color = 'gray')
plt.plot(x, t, marker = "*", color = "red", linewidth = 4, label = "Temperature")
plt.title('Hourly Temperatures - last 24 hours', fontsize = 12, fontweight = 'bold')
plt.savefig(f'{path1}testFire')       
#plt.show()


# In[ ]:




