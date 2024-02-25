#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json
import base64
import sys
import io
import os
import pandas as pd

get_json = sys.argv[1]
#final_output = json.loads(base64.b64decode(get_json))
obj = json.loads(get_json)

df = pd.DataFrame(obj)
print(df)

'''
y = 0 
x = len(obj)
print(x)

while y < x:
    #print(obj[y])
    y +=1  

tester = obj[:x]
print(tester)  
'''


# In[ ]:




