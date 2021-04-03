#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[1]:


#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# In[2]:


#loading csv data into a record array using numpy
x,y = np.loadtxt(r"C:\Users\HP\Desktop\Book1.csv",encoding='latin1',
                 unpack = True,
                 delimiter = ',')


# In[3]:


#adding style to improve graphical representation
style.use('ggplot')


# In[4]:


#Bar Graph
plt.title ('--Bar Graph--')
plt.bar(x,y, width=0.5,color=['green','yellow','pink','purple','blue','orange'])
plt.ylabel ('Y-axis')
plt.xlabel ('X-axis')
plt.show()


# In[5]:


plt.title ('--Chart--')
plt.plot(x,y)
plt.ylabel ('Y-axis')
plt.xlabel ('X-axis')

