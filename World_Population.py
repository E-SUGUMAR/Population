#!/usr/bin/env python
# coding: utf-8

# # Importing required libraries

# In[2]:


get_ipython().system('pip install pandas')


# In[3]:


get_ipython().system('pip install seaborn')


# In[129]:


get_ipython().system('pip install plotly')


# In[128]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px
plt.style.use('fivethirtyeight')
import seaborn as sns


# # Importing the Dataset

# In[35]:


population = pd.read_csv("E:/Data Science/New folder/world_population.csv")
population.head()


# # Exploratory Data Analysis

# In[ ]:


# Data cleaning


# In[36]:


population.shape


# In[37]:


population.info()


# In[ ]:


# Removing the unwanted data from the dataset using "drop()"


# In[41]:


new_population = population.drop(['CCA3','Capital'], axis='columns')


# In[42]:


new_population.head()


# In[43]:


new_population.info()


# In[ ]:


# The above output shows the country and continent in object datatype it has be change to string formate


# In[46]:


new_population['Country']=new_population['Country'].astype(str)
new_population['Continent']=new_population['Continent'].astype(str)


# In[48]:


new_population.describe()


# In[ ]:


#checking for missing values


# In[51]:


new_population.isna().sum()


# In[ ]:


# In the above output there's no null values so we don't want to balance the dataset 


# In[ ]:





# In[ ]:




