#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


dt = pd.read_excel(r'C:\Users\DELL\Pictures\iris.xls\iris.xls')


# In[6]:


dt


# In[8]:


missing_values = dt.isnull().sum()


# In[9]:


print(missing_values)


# In[10]:


dt_duplicates_removed = dt.drop_duplicates()


# In[11]:


dt_duplicates_removed 


# In[13]:


dt_filled = dt.fillna(0)


# In[14]:


dt_filled


# In[26]:


dt_f= dt.ffill()


# In[27]:


dt_f


# In[29]:


dt_f1 = dt_f.bfill()


# In[30]:


dt_f1


# In[36]:


import matplotlib.pyplot as plt


# In[38]:


plt.hist(dt['SL'], bins=10)
plt.xlabel('SL')
plt.ylabel('Frequency')
plt.title('Distribution of SL')
plt.show()


# In[39]:


from sklearn.model_selection import train_test_split


# In[ ]:




