#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
from datetime import datetime
from dateutil.tz import tzutc, tzlocal
import pytz
import sqlalchemy
import mysql.connector
import sqlite3
import os
import pyodbc

filePath = '/home/ec2-user/'
fileName = 'dataDumpSQL.csv'

# Database connection variable.
#connect = None

# Check if the file path exists.
#if os.path.exists(filePath):
#
#    try:
#
#        # Connect to database.
#        connect = pyodbc.connect(Driver='MySQL', host='3.135.162.69',
#                                 database='hourlyt', user='chuckwx',
#                                 password='jfr716!!00')
#        
#
#    except pyodbc.Error as e:
#
#        # Confirm unsuccessful connection and stop program execution.
#        print("Database connection unsuccessful", e)
#        quit()

#cursor = connect.cursor()
#
#sqlSelect = \
#        "SELECT Year, Month, Date, Hour, Minute,Temperature \
#         FROM hourlyt \
#         ORDER BY Year"

# Execute query.
#cursor.execute(sqlSelect)

# Fetch the data returned.
#results = cursor.fetchall()
#print(results)

# Extract the table headers.
#headers = [i[0] for i in cursor.description]

#connect = None
#cursor = connect.cursor()

database_username = 'chuckwx'
database_password = 'jfr716!!00'
database_ip       = '3.135.162.69'
database_name     = 'hourlyt'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name), connect_args={'connect_timeout': 30})

sqlSelect = \
        "SELECT Year, Month, Date, Hour, Minute,Temperature \
         FROM hourlyt \
         ORDER BY Year"

cursor.execute(SQLSelect)
#df2.to_sql(con=database_connection, name='hourlyt', if_exists='append')

