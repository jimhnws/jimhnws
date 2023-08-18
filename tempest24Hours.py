#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import sqlalchemy
import dataFile
import getNameNumbers
import mysql.connector
import sqlite3

#
# Read in the CSV file for processing in pandas
#

name1 = ['device_id','type', 'bucket_step_minutes', 'timestamp', 'wind_lull', 'wind_avg', 'wind_gust', 'wind_dir', 'wind_interval', 'pressure', 'temperature', 'humidity', 'lux', 'uv', 'solar_radiation', 'precip', 'precip_type', 'strike_distance', 'strike_count', 'battery', 'report_interval', 'local_daily_precip', 'precip_final', 'local_daily_precip_final', 'precip_analysis_type']
path = '/home/ec2-user/'
file_name = 'tempest_temp.csv'
full_file = f'{path}{file_name}'
table_name = 'tempestwx'

df = pd.read_csv(full_file, index_col=False)
df = df.drop(df.columns[[0,1,2,4,8,12,16,20,20,24]], axis=1)

database_username = 'chuckwx'
database_password = 'jfr716!!00'
database_ip       = '3.135.162.69'
database_name     = 'tempestwx'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name), connect_args={'connect_timeout': 30})
df.to_sql(con=database_connection, name='tempestWX', if_exists='replace', index = False )


# In[ ]:




