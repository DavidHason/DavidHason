#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from numpy.random import randn

randn()


# In[8]:


import numpy as np
from numpy.random import randn

N=100000
counter = 0
for i in randn(N):
    if i > -1 and i < 1:
        counter = counter + 1
counter / N
    


# In[ ]:




