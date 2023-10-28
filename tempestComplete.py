#!/usr/bin/env python
# coding: utf-8

# In[40]:


import calcOneDay
import getDays
import daysAndDates
from datetime import datetime, timedelta
import calcTimeNow
import logging

#
# Set some logging info
#

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('/home/ec2-user/tempestComp.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#logging.basicConfig(filename = 'test.log', level = logging.INFO,
#                    format = '%(levelname)s:%(name)s:%(message)s')

# Calculate the time and date for end of day calculations

xy = calcOneDay.calcOneDay()
start, end = (xy[0], xy[1])
dayInfo = daysAndDates.daysAndDates()
logger.info('Start time: {}'.format(start)) 
logger.info('End time: {}'.format(end))

month, month_num, date, year = dayInfo[0], dayInfo[1], dayInfo[2], dayInfo[3]
logger.info('Month, MonthNumber, Date, Year: {} {} {} {}'.format(month, month_num, date, year))

yesterday = int(dayInfo[4])
nextDay = int(dayInfo[5])


# In[13]:


import datetime
from datetime import datetime
import dataFile
import getNameNumbers
import requests

#
# Get data from the Tempest database 
#

token = '877f6425-04a5-4f33-86e7-7123b7ef53d9'
protocol = 'https://'
urlSiteDevice = 'swd.weatherflow.com/swd/rest/observations/device/'
urlSiteStation = 'swd.weatherflow.com/swd/rest/observations/station/'
deviceID = '246921'
stationID = '95775'
preToken = '&token='
preStart = '?time_start='
preEnd = '&time_end='
start_time = start
end_time = end
dayOffset = '&day_offset=1'
format1 = '&format=csv'

#
# Put it together
# 

goGetDeviceSummary = (f'{protocol}{urlSiteDevice}{deviceID}{preStart}{start_time}{preEnd}{end_time}{format1}{preToken}{token}')
r =  requests.get(goGetDeviceSummary)

path = '/home/ec2-user/'
file_name = 'tempest_temp.csv'
full_file = f'{path}{file_name}'

with open(full_file,'w') as fd:
     fd.write(r.text)


# In[14]:


import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import math

#
# Read in Tempest data from csv into a Pandas DataFrame
#

df = pd.read_csv('/home/ec2-user/tempest_temp.csv', index_col=False)

#
# Calculate needed F6 data
#

max_temp  = (df.sort_values(by='temperature', ascending=False))
max_T = max_temp.iloc[:1]
maxT = max_T['temperature'].values[0]
maxT = round((maxT*1.8) + 32)

min_temp  = (df.sort_values(by='temperature', ascending=True))
min_T = min_temp.iloc[:1]
minT = min_T['temperature'].values[0]
minT = round((minT*1.8) + 32)

max_pres = (df.sort_values(by='pressure', ascending=False))
max_P = max_pres.iloc[:1]
maxP = max_P['pressure'].values[0]

min_pres = (df.sort_values(by='pressure', ascending=True))
min_P = min_pres.iloc[:1]
minP = min_P['pressure'].values[0]

cor_rain = (df.sort_values(by='local_daily_precip_final', ascending=False))
corR_rain = cor_rain.iloc[:1]
corR = corR_rain['local_daily_precip_final'].values[0]
corR = round((corR*0.03937), 2)

tot_rain = df['precip'].sum()
totR = round((tot_rain*0.03937), 2)

strike_distance = (df.sort_values(by='strike_distance', ascending=False))
lightning1 = (df['strike_distance'].between(1,8))
lightning2 = (df['strike_distance'].between(9,16))

df.insert(10,'lightning1',lightning1)
df.insert(11,'lightning2',lightning2)

#
# Determine if the strike distance is close enough to count as a thunderstorm
#

x = len(df)
a = 0

while a < x:
        if (df['lightning1'] == True).any():
            q = "Yes"
        else:
            q = "No"
        if (df['lightning2'] == True).any():   
            r1 = "Yes"
        else:
            r1 = "No"
        a += 1    

avgTemp = math.ceil((int(maxT + minT)/2))

hdd = (65 - avgTemp)
if hdd < 0:
    hdd = 0
cdd = (avgTemp - 65)
if cdd < 0:
    cdd = 0         


# In[15]:


import sqlalchemy
import mysql.connector
import sqlite3

#
# Rearrangethe Pandas DataFrame to match the SQL table
#

df2 = pd.DataFrame(columns = ['Year', 'Month', 'Date', 'High', 'Low', 'Average', 'HDD', 'CDD', 'totR', 'corR', 'Lightning1_5', 'Lightning6_10'])
newRow = pd.DataFrame({'Year': year, 'Month': month_num, 'Date': yesterday, 'High': maxT, 'Low': minT, 'Average': avgTemp, 'HDD': hdd, 'CDD': cdd, 'totR': totR, 'corR': corR, 'Lightning1_5': q, 'Lightning6_10': r1 }, index = [yesterday])
df2 = pd.concat([newRow, df2]).reset_index(drop = True)

#
# Write the F6 data to the tempestCompF6 table
#

database_username = 'chuckwx'
database_password = 'jfr716!!00'
database_ip       = '3.135.162.69'
database_name     = 'tempestf6'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name), connect_args={'connect_timeout': 30})
df2.to_sql(con=database_connection, name='tempestCompF6', if_exists='append', index = False)


# In[16]:


#
# Get the data from the mySQL table for yesterday
#

#
# Pop data out of the SQL table, read it into a Pandas DataFrame, and 
# create an HTML table for display
#

QUERY2 = """SELECT * FROM tempestCompF6 
         WHERE Month = %s""" % (month_num)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'tempestf6')
html_path = '/var/www/html/000/'

cur = db.cursor()
cur.execute(QUERY2)
dateResult = cur.fetchall()

colNames = (['index', 'Year', 'Month', 'Date', 'High', 'Low', 'Average', 'HDD', 'CDD', 'totR', 'corR', 'Lightning1_5', 'Lightning6_10']) 
df3 = pd.DataFrame(dateResult, columns = colNames) 
df3 = df3.drop(df3.columns[[0, 1]], axis = 1)
df3 = df3.reindex(columns=['Date', 'High', 'Low', 'Average', 'HDD', 'CDD', 'totR', 'corR', 'Lightning1_5', 'Lightning6_10'])

df3.to_html(f'{html_path}tempest_Throttle.html', index = False) 


# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
import pymysql as dbapi
import sys
import csv
from tabulate import tabulate

#
# Get normal highs and lows
#

QUERY = """SELECT * FROM avgHiLo 
           WHERE Month = %s 
           AND Day = %s""" % (month_num, date)

db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'trweather')

cur = db.cursor()
cur.execute(QUERY)
result = cur.fetchall()

dataset = result[0]
nmlHi = int(dataset[3])
nmlLo = int(dataset[4])

#
# Get the record high for the date
#

QUERY1 = """SELECT * FROM recHigh 
           WHERE Month = %s 
           AND Day = %s""" % (month_num, date)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'trweather')

cur = db.cursor()
cur.execute(QUERY1)
result1 = cur.fetchall()
recordHigh = result1[0]
recHigh = int(recordHigh[1])
recHighYear = int(recordHigh[4])

#
# Get the record low for the date
#

QUERY2 = """SELECT * FROM recLow 
           WHERE Month = %s 
           AND Day = %s""" % (month_num, date)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'trweather')

cur = db.cursor()
cur.execute(QUERY2)
result2 = cur.fetchall()
recYearNum = len(result2)
recordLow = result2[0]
recLow = int(recordLow[1])
recLowYear = int(recordLow[4])

#
# Get the record rainfall for the date
#

QUERY3 = """SELECT * FROM recRain 
           WHERE Month = %s 
           AND Day = %s""" % (month_num, date)


db = dbapi.connect(host='3.135.162.69',user='chuckwx',passwd='jfr716!!00', database = 'trweather')

cur = db.cursor()
cur.execute(QUERY3)
result3 = cur.fetchall()
recordRain = result3[0]
recRain = recordRain[1]
recRainYear = int(recordRain[4])


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
import pymysql as dbapi
import sys
import csv
from tabulate import tabulate
import sandbox1
import sandbox2

#
# Retrieve normal and record data that has been checked for 
# multiple values 
#

nmlData = sandbox2.sandbox2()
nmlHi = nmlData[3]
nmlLo = nmlData[4]

highData = sandbox1.recordHigh()
lowData = sandbox1.recordLow()
rainData = sandbox1.recordRain()

highPhrase = highData[2]
lowPhrase = lowData[2]
rainPhrase = rainData[2]

#
# Write the phrases to a text file for display on the page
#

with open('/var/www/html/000/climoTempestText.txt','w') as outfile1: 
    print(f'Daily almanac for {month} {yesterday}, {year}', file = outfile1)
    print('\n', file = outfile1)
    print(f'The high yesterday was {maxT} degrees', file = outfile1)
    print(f'The low yesterday was {minT} degrees', file = outfile1)
    print(f'The average temperature was {avgTemp} degrees', file = outfile1)
    print(f'The rainfall yesterday was {("%.2f" % corR)} inches', file = outfile1)
    if hdd == 0:
        print('')
    else:
        print(f'There were {hdd} heating degree days', file = outfile1)
    if cdd == 0:
        print('')
    else:
        print(f'There were {cdd} cooling degree days', file = outfile1)
            
    
    print('\n', file = outfile1)
    
    print(f'Normal and Record information for {month} {date}, {year}', file = outfile1)
    print('\n', file = outfile1)
    print(f'The normal high for today is {nmlHi} degrees', file = outfile1)
    print(f'The normal low for today is {nmlLo} degrees' , file = outfile1)
    print('\n', file = outfile1)
    print(highPhrase, file = outfile1)
    print(lowPhrase, file = outfile1)
    print(rainPhrase, file = outfile1)  


# In[ ]:




