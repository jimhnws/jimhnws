#!/usr/bin/env python
# coding: utf-8

# In[66]:


import json
import urllib
import requests
import csv
import time

# Calculate the time and date for calcualtions so far

end = int(time.time())
start = end - 86400

print(start,end)


# In[67]:


import datetime
from datetime import datetime
import dataFile

#
# Get data from the Tempest database for the new station
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
print(start_time, end_time)
#
# Put it together
# 

goGetDeviceSummary = (f'{protocol}{urlSiteDevice}{deviceID}{preStart}{start_time}{preEnd}{end_time}{format1}{preToken}{token}')
print(goGetDeviceSummary)
r =  requests.get(goGetDeviceSummary)
#path_to_file = '/Users/jameshayes/'
path_to_file = '/home/ec2-user/'
full_file = (f'{path_to_file}latestTempestinfo.csv')

with open(full_file,'w') as fd:
     fd.write(r.text)


# In[68]:


import pandas as pd
import dataFile
import datetime
#from datetime import datetime
from dateutil.tz import tzutc, tzlocal
import pytz
import numpy as np

#
# Read in the CSV file for processing in pandas
#

path_to_file = '/home/ec2-user/'
full_file =(f'{path_to_file}latestTempestinfo.csv')
df = pd.read_csv(full_file, index_col=False)
df = df.drop(df.columns[[0,1,2,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24]], axis=1)

pd.set_option('display.max_rows', 1440)
pd.set_option('display.max_columns', 35)
pd.set_option('display.width', 1500)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)

as3 = len(df) 
#print(as3)
timestamp = df['timestamp']
timezone = pytz.timezone("America/New_York")

with open(f'{path_to_file}outfile121.csv','w') as outfile: 

    i = 0
    while i < as3:
        try:
            timestamp = (df['timestamp'].loc[i])
            dt_object = datetime.datetime.fromtimestamp(timestamp)
            localT = dt_object.astimezone(timezone)
            lastTime = localT.strftime('%I:%M %p')  
            time24 = localT.strftime('%-H')  
            time24 = int(time24)
            fmT = (df['temperature'].loc[i])
            nextT = (fmT*1.8) + 32
            
            #print(i,lastTime,nextT)
            print(f'{lastTime},{nextT}', file = outfile)
            
            i += 1
        except:
            continue


# In[82]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import calcTimeNow
import getDaysInMonth
import getNameNumbers_ec1

# Defining some variables

new_path = '/home/ec2-user/'
finalFile = f'{new_path}outfile121.csv'
path1 = '/var/www/html/000/'    
print(finalFile)

# Get some variables from elsewhere

gg = getNameNumbers_ec1.tempest_ec2()

xls_filename, xls_fullfile, path_name, date, this_month, thisYear = gg[0], gg[1], gg[2], gg[3], gg[4], gg[5]
new_path = '/home/ec2-user/'


column_names = ['Time','Temperature']
df = pd.read_csv(finalFile, names = column_names)
xcd = df['Temperature']
rwe = df['Time']
y = xcd.to_numpy()

plt.figure(figsize= (10,6))
plt.yticks(fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12, fontweight ='bold')

sas = (1440/24)
plt.xticks(np.arange(0,1440,sas))
plt.xlabel('Hours (24 hour clock)', fontsize=12, fontweight ='bold')

plt.title(f'Hourly Temperatures over the last 24 hours', fontsize=12, fontweight ='bold')
plt.plot(y,  color = "red", linewidth = 4, label ="Temperature")
plt.grid(True)
plt.autoscale(enable = True, axis = 'y', tight = True)

plt.savefig(f'{path1}testTToneMin')  


# In[ ]:





# In[ ]:




