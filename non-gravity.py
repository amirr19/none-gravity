#!/usr/bin/env python
# coding: utf-8

# In[16]:


import math
g = 9.8
v = 100
alpha_start = 50
alpha_end = -50
gama_dot_arr = []
deg_arr = []


# In[17]:


import numpy as np
for alpha in np.arange (alpha_start,alpha_end,-2):
    gama_dot = g/(v*math.cos(math.radians(alpha)))
    gama_dot_arr.append(gama_dot) 
    deg_arr.append(alpha)
print(len(deg_arr))    
print(len(gama_dot_arr))


# In[25]:


import pandas as pd
from matplotlib import pyplot as plt
data = {'alpha': deg_arr,
        'gama_dot(deg/s)': gama_dot_arr,
       }
gomma_dot_plot = pd.DataFrame(data,columns=['alpha','gama_dot(deg/s)'])
gomma_dot_plot.plot(x ='alpha', y='gama_dot(deg/s)', kind = 'scatter')
plt.show()


# In[ ]:




