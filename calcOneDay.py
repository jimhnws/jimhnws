#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import time
from datetime import timezone
from datetime import datetime, timedelta

def calcOneDay():
    end =  int(time.time())
    start = (end - 86398)
    end = str(end)
    start = str(start)
    return (start,end)


# In[ ]:




