#!/usr/bin/env python
# coding: utf-8

# In[10]:


import datetime
from datetime import datetime

# Set up directory tree for writing to Excel files

def tempest():
    now = datetime.now()
    myMonth = now.strftime("%B")
    myYear = now.strftime("%Y")
    platform = "Tempest"
    xls_suffix = '.xlsx'
    xls_filename = f'{myMonth}_{myYear}_{platform}{xls_suffix}'
    return(xls_filename)


# In[ ]:


def davis():
    now = datetime.now()
    myMonth = now.strftime("%B")
    myYear = now.strftime("%Y")
    platform = "Davis"
    xls_suffix = '.xlsx'
    xls_filename = f'{myMonth}_{myYear}_{platform}{xls_suffix}'
    return(xls_filename)

