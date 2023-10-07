#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sandbox2
import sqlGet

def recordHigh():
    
    results = sandbox2.sandbox2()
    result1 = results[0]
    recYearNum = len(result1)
        
    if recYearNum > 1 and recYearNum < 4:
        recHigh = (result1[0][1])
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
            highPhrase = (f'The record high for today is {recHigh} set in {yearx}')
        elif recYearNum == 3:
            ax = years[recYearNum - 3]
            bx = years[recYearNum - 2]
            cx = years[recYearNum - 1 ]
            yearx = (f'{ax},{bx} and {cx}')
            highPhrase = (f'The record high for today is {recHigh} set in {yearx}')
        elif recYearNum == 4:
            ax = years[recYearNum - 4]
            bx = years[recYearNum - 3]
            cx = years[recYearNum - 2 ]
            dx =  years[recYearNum - 1 ]
            yearx = (f'{ax},{bx}, {cx} and {dx}')
            highPhrase = (f'The record high for today is {recHigh} set in {yearx}')
        return(recHigh, yearx, highPhrase)
                
    if recYearNum == 1:
        recHigh1 = (result1[0])
        recHigh = int(recHigh1[1])
        year1x = (result1[0])
        yearx = int(year1x[4])
        highPhrase = (f'The record high for today is {recHigh} set in {yearx}')
    return(recHigh, yearx, highPhrase)         


# In[5]:


recordHigh()


# In[6]:


import sandbox2
import sqlGet

def recordLow():
    
    results = sandbox2.sandbox2()
    result2 = results[1]
        
    recYearNum = len(result2)
    print(result2, recYearNum)     
    
    if recYearNum > 1 and recYearNum < 4:
        recLow = (result2[0][1])
        i = 0 
        years = []
        while i < recYearNum:
            years.append(str(result2[i][4]))
            i+= 1
        
        years.reverse()
    
        if recYearNum == 2:
            recLow = (result2[0][1])
            print("This is the record low value" ,recLow)
            ax = years[recYearNum - 2]
            bx = years[recYearNum - 1]
            yearx = (f'{ax} and {bx}')
            lowPhrase = (f'The record low for today is {recLow} set in {yearx}')
            
        elif recYearNum == 3:
            ax = years[recYearNum - 3]
            bx = years[recYearNum - 2]
            cx = years[recYearNum - 1 ]
            yearx = (f'{ax},{bx} and {cx}')
            lowPhrase = (f'The record low for today is {recLow} set in {yearx}')
            
        elif recYearNum == 4:
            ax = years[recYearNum - 4]
            bx = years[recYearNum - 3]
            cx = years[recYearNum - 2 ]
            dx =  years[recYearNum - 1 ]
            yearx = (f'{ax},{bx}, {cx} and {dx}')
            lowPhrase = (f'The record low for today is {recLow} set in {yearx}')
        return(recLow, yearx, lowPhrase)    
    
        if recYearNum == 1:
            recLow1 = (result2[0])
            recLow = int(recLow1[1])
            year1x = (result2[0])
            yearx = year1x[4]
            lowPhrase = (f'The record low for today is {recLow} set in {yearx}')   
        return(recLow, yearx, lowPhrase)       
     
    


# In[7]:


recordLow()


# In[55]:


import sandbox2
import sqlGet

def recordRain():
    
    results = sandbox2.sandbox2()
    result3 = results[2]       
    
    recYearNum = len(result3)
    print(result3, recYearNum)
    recRain = (result3[0][1])
    print(recRain)
    
    if recYearNum == 1:
        recRain = (result3[0][1])
        yearx = (result3[0][4])
        print(yearx)
        rainPhrase = (f'The record rainfall for today is {recRain} set in {yearx}')
    return(recRain, yearx, rainPhrase)   
                
    if recYearNum > 1 and recYearNum < 4:
        recRain = (result3[0][1])
        i = 0 
        years = []
        while i < recYearNum:
            years.append(str(result3[i][4]))
            i+= 1
        
        years.reverse()
    
    if recYearNum == 2:
        recRain = (result3[0][1])
        ax = years[recYearNum - 2]
        bx = years[recYearNum - 1]
        yearx = (f'{ax} and {bx}')
        print(yearx)
        rainPhrase = (f'The record rainfall for today is {recRain} set in {yearx}')
        
    elif recYearNum == 3:
        recRain = (result3[0][1])
        ax = years[recYearNum - 3]
        bx = years[recYearNum - 2]
        cx = years[recYearNum - 1 ]
        yearx = (f'{ax},{bx} and {cx}')
        print(yearx)
        rainPhrase = (f'The record rainfall for today is {recRain} set in {yearx}')
        
    elif recYearNum == 4:
        recRain = (result3[0][1])
        ax = years[recYearNum - 4]
        bx = years[recYearNum - 3]
        cx = years[recYearNum - 2 ]
        dx =  years[recYearNum - 1 ]
        yearx = (f'{ax},{bx}, {cx} and {dx}')
        print(yearx)
        rainPhrase = (f'The record rainfall for today is {recRain} set in {yearx}')
    return(recRain, yearx, rainPhrase)      


# In[56]:


recordRain()


# In[ ]:





# In[ ]:




