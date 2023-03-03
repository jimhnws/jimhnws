#!/usr/bin/env python
# coding: utf-8

# In[11]:


import excelFilename

def setUpHTML_mac():
    path_to_file = '/Users/jameshayes/'
    html_path = '/Users/jameshayes/Sites/'
    xls_filename = excelFilename.tempest()
    new_file = f'{path_to_file}{xls_filename}'
    return(new_file)

def setUpHTML_ec2():
    path_to_file = '/home/ec2-user/'
    html_path = '/var/html/www/000'
    xls_filename = excelFilename.davis()
    new_file = f'{path_to_file}{xls_filename}'
    return (new_file)


# In[ ]:




