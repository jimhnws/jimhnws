#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

print(conn)
mycursor = conn.cursor()

mycursor.execute("USE hourlyt;")
mycursor.execute("SELECT * FROM testTempest INTO OUTFILE '/tmp/testKRBA.csv';")


# In[ ]:


path = '/tmp/'
path1 = '/home/ec2-user/'
path2 = '/var/www/html/000/'
file_name = 'testKRBA.csv'
data_file = f'{path}{file_name}'
lastFile = f'{path1}poppedSQL.csv'

df = pd.read_csv(data_file, index_col=False, sep = '\t', names = ['id', 'DateTime', 'LocalTime', 'Temperature'])
df = df.drop(df.columns[[0]], axis = 1)

df.to_csv(lastFile, sep = ',', index = False)
df.to_html(path2 + 'testT' + '.html', index = False)


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import calcTimeNow
import getDaysInMonth

t = df['Temperature']
y = t.to_numpy()

plt.figure(figsize= (10,6))
plt.yticks(fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12, fontweight ='bold')
#plt.locator_params(axis='y', nbins=20)

#plt.xlim(0,23)
plt.xticks(np.arange(0,24,1))
plt.xlabel('Hours (24 hour clock)', fontsize=12, fontweight ='bold')

plt.title('Test Graphic for 24 hours of rainfall')
#plt.title(f'{this_month} {date} {thisYear} Hourly Temperatures', fontsize=12, fontweight ='bold')
plt.plot(y, marker = "*", color = "red", linewidth = 4, label = "Temperature")
plt.grid(True)
plt.autoscale(enable = True, axis = 'y', tight = True)

plt.savefig(f'{path2}testFire')  

