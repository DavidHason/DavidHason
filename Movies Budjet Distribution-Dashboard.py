#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[5]:


print (os.getcwd())


# In[8]:


movies = pd.read_csv('C:/Users/David/Desktop/Python Programming Course/P4-Movie-Ratings.csv')


# In[9]:


movies


# In[12]:


len (movies)


# In[13]:


movies.head()


# In[14]:


movies.columns


# In[29]:


movies.columns  = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']


# In[30]:


movies.head()


# In[31]:


movies.info()


# In[32]:


movies.describe()


# In[33]:


movies.Film


# In[34]:


movies.Film =movies.Film.astype('category')


# In[37]:


movies.info()


# In[36]:


movies.Year =movies.Year.astype('category')
movies.Genre =movies.Genre.astype('category')


# In[38]:


movies.info()


# In[39]:


movies.Genre.cat.categories


# In[40]:


movies.describe()


# In[41]:


from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[42]:


#jointplots


# In[46]:


j=sns.jointplot(data=movies, x='CriticRating', y='AudienceRating')


# In[48]:


j=sns.jointplot(data=movies, x='CriticRating', y='AudienceRating',kind='hex' )


# --- # Chart no.1

# In[50]:


j=sns.jointplot(data=movies, x='CriticRating', y='AudienceRating',kind='resid')


# In[52]:


# HISTOGRAMS


# In[56]:


m1=sns.distplot(movies.AudienceRating, bins=30)


# In[57]:


m1=sns.distplot(movies.CriticRating, bins=30)


# In[63]:


n1 = plt.hist(movies.AudienceRating, bins=30)


# In[64]:


sns.set_style('white')
n1 = plt.hist(movies.AudienceRating, bins=30)


# In[ ]:


# Chart2


# In[62]:


sns.set_style('darkgrid')
n1 = plt.hist(movies.CriticRating, bins=30)


# In[65]:


#chart3


# In[66]:


#stacked Histograms


# In[75]:


plt.hist(movies [movies.Genre == 'Action'].BudgetMillions)

plt.hist(movies [movies.Genre == 'Drama'].BudgetMillions)
plt.hist(movies [movies.Genre == 'Thriller'].BudgetMillions)


# In[ ]:


# Filtering 


# In[70]:


movies [movies.Genre == 'Drama'].BudgetMillions


# In[82]:


[(movies [movies.Genre == 'Action'].BudgetMillions), (movies [movies.Genre == 'Drama'].BudgetMillions)]
plt.hist ([movies [movies.Genre == 'Action'].BudgetMillions,            movies [movies.Genre == 'Drama'].BudgetMillions,           movies [movies.Genre == 'Thriller'].BudgetMillions,           movies [movies.Genre == 'Comedy'].BudgetMillions],           
           bins=15, stacked=True)


# In[83]:


for gen in movies.Genre.cat.categories:
    print(gen)


# In[89]:


list1=[]
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies [movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
h= plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)

plt.legend()
    


# In[90]:


#Chart4


# In[91]:


#KDE Plot


# In[93]:


vis1=sns.lmplot(data=movies, x='CriticRating', y= 'AudienceRating', fit_reg=False, hue= 'Genre', size=7, aspect=1)


# In[98]:


k1=sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade=True, shade_lowest = False, cmap='Reds')


# In[101]:


k1=sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade=True, shade_lowest = False, cmap='Reds')
k1=sns.kdeplot(movies.CriticRating, movies.AudienceRating, cmap='Reds')


# In[106]:


sns.set_style("dark")
k1=sns.kdeplot(movies.CriticRating, movies.BudgetMillions, shade=True, shade_lowest = False, cmap='Reds')


# In[103]:


#subplots()


# In[112]:


sns.set_style("dark")
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating)


# In[119]:


f, axes = plt.subplots(2,2, figsize=(12,6), sharex=True , sharey=True)
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,1])
k1=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[1,0])
k1.set(xlim=(-20,160))


# In[116]:


axes


# In[120]:


#violin Plot


# In[122]:


z = sns.boxplot(data=movies, x='Genre', y='CriticRating')


# In[121]:


z = sns.violinplot(data=movies, x='Genre', y='CriticRating')


# In[123]:


#facid Grid


# In[126]:


g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')


# In[128]:


g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating')


# In[130]:


g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.hist, 'BudgetMillions')


# In[136]:


g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor= 'black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
for ax in g.axes.flat:
    ax.plot ((10,90), (10,90), c="gray", ls="--")
    
g.add_legend()


# In[137]:


#chart-4


# In[138]:


#Building Dashboard


# In[139]:


from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[149]:


sns.set_style("darkgrid")
f, axes = plt.subplots(2,2, figsize= (15,15))
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,0])
k2=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,1])

z = sns.violinplot(data=movies[movies.Genre=='Drama'], x='Genre', y='CriticRating', ax=axes[1,0])

#k4=sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade=True, shade_lowest = False, cmap='Reds', ax=axes[1,1])
#k4=sns.kdeplot(movies.CriticRating, movies.AudienceRating, cmap='Reds', ax=axes[1,1])

axes[1,1].hist(movies.CriticRating, bins=30)


# ---

# In[151]:


#Styling Dashboard


# In[ ]:




