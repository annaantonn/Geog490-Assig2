#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

cities = gpd.read_file('lab2/data/oregon_fires.shp')
cities.head()


# In[2]:


cities.shape


# In[3]:


cities[cities['year'] == '2021']


# In[4]:


import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

cities = gpd.read_file('lab2/data/oregon_fires.shp')
cities.head()


# In[5]:


cities[cities['year'] == 2021].shape[0]


# In[6]:


cities.crs


# In[7]:


cities_reproject = cities.to_crs('EPSG:32610')
cities_reproject.crs


# In[8]:


cities_reproject['area'] = cities_reproject['geometry'].area
cities_reproject.head()


# In[9]:


cities_reproject.nlargest(n=5, columns='area')


# In[10]:


cities_area = cities_reproject[cities_reproject['year'] == 2021]


# In[11]:


cities_area


# In[12]:


total_area = cities_area['area'].sum()


# In[13]:


total_area


# In[14]:


total_area / 1000000 


# In[15]:


import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

owls = gpd.read_file('lab2/data/spotted_owls.shp')
owls.head()


# In[16]:


owls.shape


# In[17]:


owls['males'].min()


# In[18]:


owls['males'].max()


# In[19]:


owls['females'].min()


# In[20]:


owls['females'].max()


# In[21]:


owl = owls[owls['females'] == 1.0].shape[0]


# In[22]:


(owl / owls.shape[0]) * 100


# In[23]:


owls['geometry'].x.max()


# In[24]:


owls.crs


# In[25]:


owls_reproject = owls.to_crs('EPSG:32610')
owls_reproject.crs


# In[26]:


owls_reproject['pairs'] = ((owls_reproject['males'] == 1) & (owls_reproject['females'] == 1)) * 1
owls_reproject


# In[ ]:





# In[27]:


df = owls_reproject.sjoin(cities_reproject, how="left")


# In[28]:


df


# In[29]:


join = df.dropna()


# In[30]:


join


# In[31]:


join['pairs'].sum()


# In[32]:


join.groupby('year')['pairs'].sum().reset_index()


# In[33]:


ax = owls_reproject.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
cities_reproject.plot(ax=ax, color='black', markersize=5)


# In[34]:


ax


# In[ ]:




