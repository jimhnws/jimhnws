#!/usr/bin/env python
# coding: utf-8

# In[28]:


import sqlalchemy
import pandas as pd


# In[29]:


path = '/home/ec2-user/'
file_name = 'AvgHiLo.csv'
full_file = f'{path}{file_name}'
df = pd.read_csv(full_file, index_col=False)
tableName = 'avgHiLo'


# In[30]:


database_username = 'chuckwx'
database_password = 'jfr716!!00'
database_ip       = '3.135.162.69'
database_name     = 'trweather'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name), connect_args={'connect_timeout': 30})
print(database_connection)
df.to_sql(con=database_connection, name='avgHiLo', if_exists='replace')


# In[ ]:




