#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
import pandas as pd
import dataFile
import getNameNumbers
import sqlalchemy
import mysql.connector
import sqlite3
import NoDaysInMonth

# creating connection
conn = mysql.connector.connect(
  host="3.135.162.69",
  user="chuckwx",
  password="jfr716!!00"
)

mycursor = conn.cursor()
mycursor.execute("USE trweather;")
pop1 = ("select @startTime := timeGroup from trw order by timeGroup DESC LIMIT 1;")
pop2 = ("SELECT @endTime := DATE_SUB(@startTime, INTERVAL 30 Day);")
pop3 = ("SELECT * from trw WHERE timeGroup BETWEEN @endTime AND @startTime into OUTFILE '/tmp/trw1.csv';")
popSelect = pop1 + pop2 + pop3

mycursor.execute(popSelect)
'''


# In[ ]:


import pandas as pd
import os

path = '/tmp/'
path1 = '/home/ec2-user/'
path2 = '/var/www/html/000/'
fileName = 'trw1.csv'
dataFile = f'{path}{fileName}'

df = pd.read_csv(dataFile, index_col = False, sep = '\t', names = ['index', 'Rain', 'HiTemp', 'LowTemp', 'Year', 'Month', 'Day', 'timeGroup'])
newDate = df['Month'] + df['Day']
df = df.drop(columns = ['index','HiTemp', 'LowTemp', 'timeGroup'], axis = 1)

df.to_html(path2 + 'testRR' + '.html', index = False, justify = 'center')


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns

#t = df['Rain']
#y = t.to_numpy()
#date = df['Day']
#x = date.to_numpy()
#print(x)

year = (df['Year']).astype(str)
month = (df['Month']).astype(str)
day = (df['Day']).astype(str)

df['newDate'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df['new_date'] = df['newDate'].dt.date
df['new_date'].astype('str')
df['new_date'] = df['new_date'].apply(str).str.replace('2023-', '')


plt.figure(figsize= (10,6))
plt.yticks(fontsize = 12)
plt.xticks(fontsize = 8, rotation = 45, fontweight = 'bold')
plt.title('Rainfall over the last 30 days', fontsize = 12, fontweight = 'bold')
sns.barplot(data = df, x = 'new_date' , y = 'Rain', color = 'g', width=0.8)
plt.xlabel('Date',fontsize = 12, fontweight = 'bold')
plt.ylabel('Rainfall (inches)', fontsize = 12, fontweight = 'bold')
plt.grid(True)
plt.autoscale(enable = True, axis = 'both', tight = True)
plt.savefig(f'{path2}testIce')  


# In[ ]:





# In[ ]:




