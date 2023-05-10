#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json

file_path = '/home/ec2-user/' 

with open(f'{file_path}synop.json','r') as fd:
     dataAPI = json.load(fd)     


# In[2]:


x = 0
for data in dataAPI['STATION']:
    if 'MINMAX' in data:
        pass 
    else:
        data['MINMAX'] = 'Missing'
                                      
    x = x + 1 

print()    
print(f'There are {x} observations this hour')
print()


# In[3]:


station = dataAPI['STATION']
y = 0 

with open(f'{file_path}outfile2.txt','w') as outfile: 

    while (y < x):
      
        mnet_id = station[y]
        stid = mnet_id.get('STID')
        station_name = mnet_id.get('NAME')
        station_name = station_name.replace(',','')
        state = mnet_id.get('STATE')
        lat = mnet_id.get('LATITUDE')
        lon = mnet_id.get('LONGITUDE')
        el = mnet_id.get('ELEVATION')
        tz = mnet_id.get('TIMEZONE')
        temps_info = mnet_id.get('MINMAX')
        if temps_info == 'Missing':
            print(f'The air temperature information is missing for {stid}') 
            air_temps_info == 'Missing'
            dates == 'Missing'
            max_local == 'Missing'
            min_local == 'Missing'
            time_min_local == 'Missing'
            time_max_local == 'Missing'
            y +=1
            continue      
        
        
        air_temps_info = temps_info.get('air_temp_value_1')
        dates = air_temps_info.get('dates')
        dates = (''.join(dates))
        max_local = air_temps_info.get('value_max_local')
        max_local = ("".join([str(i)for i in max_local]))  
        min_local = air_temps_info.get('value_min_local')
        min_local = ("".join([str(i)for i in min_local]))
        time_min_local = air_temps_info.get('datetime_min_local')
        time_max_local = air_temps_info.get('datetime_max_local')
        
        #print(f'{y},{stid},{station_name},{state},{lat},{lon},{el},{tz},{dates},{min_local},{time_min_local},{max_local},{time_max_local}')
        print(f'{stid},{station_name},{state},{lat},{lon},{el},{tz},{dates},{min_local},{time_min_local},{max_local},{time_max_local}', file = outfile)
        y +=1    
        
print()        
print(f'Wrote {y} stations to {file_path}outfile2.txt')   
                     
       


# In[4]:


#
# Remove lines with missing data
#

full_file = f'{file_path}outfile2.txt'

lines = []
# read file
with open(full_file, 'r') as f:
    # read an store all lines into list
    lines = f.readlines()

# Write file
with open(full_file, 'w') as f:
    # iterate each line
    for line in lines:
          
        # condition for data to be deleted
        if 'None' not in line:
        #if line.strip("\n") != 'None': 
            f.write(line)            


# In[ ]:


#
# Read in the blacklist and remove those lines
#

values = []
lines = []

import os
import sys

#Set the path and file name of the blacklist file

name_of_file = ('blacklist.txt')
new_fileName = f'{file_path}{name_of_file}'
file_name = f'{path_to_file}outfile2.txt'

# read blacklist file

try:

    with open(new_fileName, 'r') as f:
        values = f.readlines()
        for i,n in enumerate(values):
            values[i] = n.strip("\n")          
        
except os.error as err:
       print(f"Unable to open {new_fileName}: {err}", file=sys.stderr)      
                                     
dummy_name = 'test1009.txt'
dummy_file = f'{file_path}{dummy_name}' 

#number of values
a = (len(values))
print(values)

#
# Set the values for checking in the loop
#

print(f'There are {a} members of the blacklist')
        
with open(file_name, 'r') as f:
        lines = f.readlines()
        print(f'read in the file {file_name}')
                  
with open(file_name, 'w') as fd:
         print(f'writing the file {file_name}')
         for line in lines:
                
                result = any(map(line.startswith, values))
                if result == False:
                    fd.writelines(line) 


# In[5]:


import pandas as pd

df = pd.read_csv(f'{file_path}outfile2.txt', names = ['STID', 'Location', 'State','Lat', 'Lon', 'Elev','TZ','Date','LOW','Time_Min_Local','HIGH', 'Time_Max_Local'] )
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1500)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)

#
# Set the path 
#
# This path is where you want to the created HTML files to reside. It is 
# different from the installation directory. Check with the webmaster 
# to fins the path to the coreect directory on your system
#

html_path = '/var/www/html/000/'

#
# Write the MAX html file first
#

ccc = (df.sort_values(by="HIGH", ascending=False))
cccc = ccc.round({"HIGH":0})
cccc.head(50).to_html(new_Path + 'Max_local' + '.html', index = False)

#
# Now write the MIN html file
#

ddd = (df.sort_values(by='LOW', ascending=True))
dddd = ddd.round({"LOW":0})
dddd.head(50).to_html(new_Path + 'Min_local' + '.html', index = False)

