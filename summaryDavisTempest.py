#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import datetime
from datetime import datetime
import time

now = (datetime.now())

df1 = pd.read_csv('/Users/jameshayes/HiLoRain.csv', names = ['High','Low','Rainfall','Fake Rain','Time'], index_col = False)
df1['Platform'] = 'Davis'
df2 = pd.read_csv('/Users/jameshayes/HiLoRain_tempest.csv', names = ['High','Low','Rainfall','Fake Rain','Time'], index_col = False)
df2['Platform'] = 'Tempest'
pd.set_option('display.precision', 2)
pd.set_option('display.colheader_justify', 'center')
df3 = pd.concat([df1,df2])
print(f'Done at {now}')
df3.to_html('/Users/jameshayes/Sites/together.html', index = False)  


# In[ ]:





# In[ ]:




