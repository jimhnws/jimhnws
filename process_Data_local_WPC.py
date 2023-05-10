#!/usr/bin/env python
# coding: utf-8

# In[123]:


import json

with open('/Users/jameshayes/TEST996.json','r') as fd:
     dataAPI = json.load(fd)     


# In[124]:


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


# In[125]:


station = dataAPI['STATION']
y = 0 

with open('/Users/jameshayes/outfile2.txt','w') as outfile: 

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
print(f'Wrote {y} stations to /Users/jameshayes/outfile2.txt')   
                     
       


# In[126]:


#
# Remove lines with missing data
#

full_file = '/Users/jameshayes/outfile2.txt'

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


# In[127]:


import pandas as pd

df = pd.read_csv('/Users/jameshayes/outfile2.txt', names = ['STID', 'Location', 'State','Lat', 'Lon', 'Elev','TZ','Date','LOW','Time_Min_Local','HIGH', 'Time_Max_Local'] )
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

new_Path = ('/Users/jameshayes/Sites/') # ***THIS NEEDS TO BE CHANGED***

#
# Write the MAX html file first
#

ccc = (df.sort_values(by="HIGH", ascending=False))
cccc = ccc.round({"HIGH":0})
cccc.head(50).to_html(new_Path + 'Max' + '.html', index = False)

#
# Now write the MIN html file
#

ddd = (df.sort_values(by='LOW', ascending=True))
dddd = ddd.round({"LOW":0})
dddd.head(50).to_html(new_Path + 'Min' + '.html', index = False)


# In[ ]:





# In[ ]:




