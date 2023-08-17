#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import the library
import mysql.connector

# creating connection
conn = mysql.connector.connect(
  host="3.135.162.69",
  user="chuckwx",
  password="jfr716!!00"
)

#print the connection
print(conn)
# import the cursor from the connection (conn)

mycursor = conn.cursor()
#print the mycursor

mycursor.execute("USE hourlyt;")
mycursor.execute("SELECT * FROM hourlyt ORDER BY Month ASC LIMIT 24;")
for row in mycursor:
    print(row)

