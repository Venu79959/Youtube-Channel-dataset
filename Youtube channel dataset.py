#!/usr/bin/env python
# coding: utf-8

# # Youtube channel dataset analysis by KODI VENU

# In[1]:


import pandas as pd
import numpy as np
data = pd.read_csv('top-5000-youtube-channels.csv')


# Displaying ALL Rows of the Dataset except last 5 rows using head method

# In[2]:


data.head()


# In[3]:


data.head(-5)


# Displaying ALL Rows of the Dataset except first 5 rows using tail method

# In[4]:


data.tail(-5)


# Finding shape of the Dataset

# In[5]:


data.shape


# In[6]:


print("Number of rows", data.shape[0])
print("Number of columns", data.shape[1])


# Dataset Information

# In[7]:


data.info()


# Dataset Overall Statistics

# In[8]:


data.describe()


# In[9]:


data.describe(include='all')


# Resizing to decimal values

# In[10]:


pd.options.display.float_format='{:2f}'.format
data.describe()


# Data cleaning Replace '--' to NaN

# In[11]:


data.head(20)


# In[12]:


import numpy as np


# In[13]:


data=data.replace('--',np.nan,regex=True)


# In[14]:


data.head(20)


# Checking Null Values in the dataset

# In[15]:


data.isnull()


# In[16]:


data.isnull().sum()


# In[17]:


per_missing=data.isnull().sum() *100/len(data)


# In[18]:


per_missing


# In[20]:


import seaborn as sns
sns.heatmap(data.isnull())


# In[21]:


data.dropna(axis=0,inplace=True)


# In[22]:


sns.heatmap(data.isnull())


# Data cleaning [ Rank column ]

# In[23]:


data.head()


# In[24]:


data.tail()


# In[25]:


data.dtypes


# In[37]:


data['Rank'] = data['Rank'].str[0:-2]


# In[38]:


data.head()


# In[39]:


data.tail()


# In[40]:


data['Rank']=data['Rank'].str.replace(',','')


# In[36]:


data.tail()


# In[56]:


data['Rank']=data['Rank'].astype('int')


# In[48]:


data.dtypes


# Data cleaning [video uploads & subscribers]

# In[49]:


data.head()


# In[51]:


data['Video Uploads']=data['Video Uploads'].astype('int')


# In[54]:


data['Subscribers']=data['Subscribers'].astype('int')


# In[55]:


data.dtypes


# Data cleaning [Grade column]

# In[57]:


data.head()


# In[58]:


data['Grade'].unique()


# In[59]:


data['Grade']=data['Grade'].map({'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1})


# In[60]:


data['Grade']


# In[61]:


data.head()


# Find average views for each channel

# In[62]:


data.columns


# In[63]:


data['Avg_views']=data['Video views']/data['Video Uploads']


# In[64]:


data.head()


# Find out top five channels with maximum number of video uploads

# In[65]:


data.columns


# In[66]:


data.sort_values(by='Video Uploads')


# In[67]:


data.sort_values(by='Video Uploads',ascending=False)


# In[68]:


data.sort_values(by='Video Uploads',ascending=False).head()


# find correlation matrix

# In[69]:


data.corr()


# In[ ]:





# which grade has a maximum number of video uploads?

# In[70]:


data.columns


# In[71]:


sns.barplot(x='Grade',y='Video Uploads',data=data)


# which grade has the highest average views?

# In[72]:


data.columns


# In[73]:


sns.barplot(x='Grade',y='Avg_views',data=data)


# which grade has the highest number of subscribers?

# In[74]:


data.columns


# In[75]:


sns.barplot(x='Grade',y='Subscribers',data=data)


# which grade has the highest video views?

# In[76]:


data.groupby('Grade').mean()


# In[ ]:




