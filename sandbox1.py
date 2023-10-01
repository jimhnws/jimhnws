#!/usr/bin/env python
# coding: utf-8

# In[86]:


import sandbox2
import sqlGet

def recordHigh():
    
    results = sandbox2.sandbox2()
    result1 = results[0]
    recYearNum = len(result1)
    
    if recYearNum > 1 and recYearNum < 4:
        recHigh = (result1[0][1])
        print(recHigh)
        i = 0 
        years = []
        while i < recYearNum:
            years.append(str(result1[i][4]))
            i+= 1
        
        years.reverse()
    
        if recYearNum == 2:
            ax = years[recYearNum - 2]
            bx = years[recYearNum - 1]
            yearx = (f'{ax} and {bx}')
            print(f'The record high for today is {recHigh} set in {yearx}')
        elif recYearNum == 3:
            ax = years[recYearNum - 3]
            bx = years[recYearNum - 2]
            cx = years[recYearNum - 1 ]
            yearx = (f'{ax},{bx} and {cx}')
            print(f'The record high for today is {recHigh} set in {yearx}')
        elif recYearNum == 4:
            ax = years[recYearNum - 4]
            bx = years[recYearNum - 3]
            cx = years[recYearNum - 2 ]
            dx =  years[recYearNum - 1 ]
            yearx = (f'{ax},{bx}, {cx} and {dx}')
            print(f'The record high for today is {recHigh} set in {yearx}')
                
    if recYearNum == 1:
        recHigh1 = (result1[0])
        recHigh = int(recHigh1[1])
        year1x = (result1[0])
        yearx = int(year1x[4])
        print(f'The record high for today is {recHigh} set in {yearx}')
        
        


# In[ ]:


recordHigh()


# In[84]:


import sandbox2
import sqlGet

def recordLow():
    
    results = sandbox2.sandbox2()
    result2 = results[1]
        
    recYearNum = len(result2)
    print(result2, recYearNum)

    if recYearNum > 1 and recYearNum < 4:
        recLow1 = (result2[0][1])
        print(recLow1)
        i = 0 
        years = []
        while i < recYearNum:
            years.append(str(result2[i][4]))
            i+= 1
        
        years.reverse()
    
        if recYearNum == 2:
            ax = years[recYearNum - 2]
            bx = years[recYearNum - 1]
            yearx = (f'{ax} and {bx}')
            print(f'The record low for today is {recLow} set in {yearx}')
        elif recYearNum == 3:
            ax = years[recYearNum - 3]
            bx = years[recYearNum - 2]
            cx = years[recYearNum - 1 ]
            yearx = (f'{ax},{bx} and {cx}')
            print(yearx)
        elif recYearNum == 4:
            ax = years[recYearNum - 4]
            bx = years[recYearNum - 3]
            cx = years[recYearNum - 2 ]
            dx =  years[recYearNum - 1 ]
            yearx = (f'{ax},{bx}, {cx} and {dx}')
            print(f'The record low for today is {recLow} set in {yearx}')
                
    if recYearNum == 1:
        recLow1 = (result2[0])
        recLow = recLow1[1]
        year1x = (result2[0])
        yearx = year1x[4]
        print(f'The record low for today is {recLow} set in {yearx}')       


# In[ ]:


recordLow()


# In[67]:


import sandbox2
import sqlGet

def recordRain():
    
    results = sandbox2.sandbox2()
    result3 = results[2]       
    
    recYearNum = len(result3)
    print(result3, recYearNum)
    
    if recYearNum > 1 and recYearNum < 4:
        recRain = (result3[0][1])
        i = 0 
        years = []
        while i < recYearNum:
            years.append(str(result3[i][4]))
            i+= 1
        
        years.reverse()
    
    if recYearNum == 2:
        ax = years[recYearNum - 2]
        bx = years[recYearNum - 1]
        yearx = (f'{ax} and {bx}')
        print(f'The record rainfall for today is {recRain} set in {yearx}')
    elif recYearNum == 3:
        ax = years[recYearNum - 3]
        bx = years[recYearNum - 2]
        cx = years[recYearNum - 1 ]
        yearx = (f'{ax},{bx} and {cx}')
        print(f'The record rainfall for today is {recRain} set in {yearx}')
    elif recYearNum == 4:
        ax = years[recYearNum - 4]
        bx = years[recYearNum - 3]
        cx = years[recYearNum - 2 ]
        dx =  years[recYearNum - 1 ]
        yearx = (f'{ax},{bx}, {cx} and {dx}')
        print(f'The record rainfall for today is {recRain} set in {yearx}')
    
        
    if recYearNum == 1:
        recRain1 = result3[0]
        recRain = recRain1[1]
        year1x = result3[0]
        yearx = year1x[4]
        print(f'The record rainfall for today is {recRain} set in {yearx}')


# In[ ]:


recordRain()

