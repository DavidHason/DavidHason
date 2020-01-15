#!/usr/bin/env python
# coding: utf-8

# Line Chart 

# In[3]:


import pandas as pd
unrate = pd.read_csv('C:/Users/David/Desktop/Python Programming Course/Dataquest/unrate.csv')



# In[4]:


unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))


# In[5]:


import matplotlib.pyplot as plt
plt.plot()
plt.show()


# In[7]:


first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.show()
import warnings
warnings.filterwarnings('ignore')


# In[18]:


plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()


# In[19]:


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()


# In[24]:


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])

plt.show()


# In[28]:


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()
fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()


# In[29]:


fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

plt.show()


# In[46]:


unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(10,6))

plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red', ls='--',marker='v', label='1948')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue', label='1949')
plt.plot(unrate[24:36]['MONTH'], unrate[24:36]['VALUE'], c='black', label='1950')
plt.plot(unrate[36:48]['MONTH'], unrate[36:48]['VALUE'], c='green',label='1951')
plt.plot(unrate[48:60]['MONTH'], unrate[48:60]['VALUE'], c='yellow',label='1952')
plt.legend(loc='upper right')
plt.show()


# In[52]:



fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()


# ---
