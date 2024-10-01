#!/usr/bin/env python
# coding: utf-8

# ## importing libary and dataset

# In[80]:


# imoprting libaries for data manupulation
import pandas as pd
import numpy as np
import datetime as dt
import calendar
# imoprtiog libaries for data visualization
import matplotlib as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('C:\\Users\\HP\\Downloads\\Unemployment_Rate_upto_11_2020.csv')
data


# ## chacking for Null values
# 

# In[3]:


data.isnull().sum()


# ## formating and making new feldes

# In[4]:


data.rename(columns={'Region':'States','Region.1':'Region'},inplace=True)
# Converting 'Date' column to datetime format 
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
# Extracting month from 'Date' and creating a 'Month' column
data['Month'] = data['Date'].dt.month

# Converting 'Month' to integer format
data['Month_int'] = data['Month'].apply(lambda x: int(x))

# Mapping integer month values to abbreviated month names
data['Month_name'] = data['Month_int'].apply(lambda x: calendar.month_abbr[x])

# Dropping the original 'Month' column
data.drop(columns='Month', inplace=True)


# In[5]:


data


# In[6]:


data['Month_name'].unique()


# In[7]:


data.describe()


# In[8]:


per_region_data=data.groupby(['Region'])[['Estimated Unemployment Rate (%)','Estimated Employed','Estimated Labour Participation Rate (%)','Month_name']].mean().reset_index()
per_region_data


# In[9]:


# barplot to show unemployment rate in different Region
import plotly.express as px
fig = px.bar(per_region_data, x='Region', y='Estimated Unemployment Rate (%)', color='Region', title='Unemployment rate per Region', template='seaborn')
fig.show()


# In[10]:


# barplot to show unemployment rate in different States
fig = px.box(data, x='States', y='Estimated Unemployment Rate (%)', color='States', title='Unemployment rate per States', template='seaborn')
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()


# In[11]:


fig = px.violin(data, x='States', y='Estimated Labour Participation Rate (%)', color='Region', title='Estimated Labour Participation Rate (%)', template='seaborn')

# Updating the x-axis category order to be in descending total
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()


# In[12]:


# Creating a DataFrame with relevant columns
unemployed_df = data[['States', 'Region', 'Estimated Labour Participation Rate (%)', 'Estimated Employed', 'Estimated Unemployment Rate (%)']]

unemployed = unemployed_df.groupby(['Region', 'States'])['Estimated Unemployment Rate (%)'].mean().reset_index()

# Creating a Sunburst chart 
fig = px.sunburst(unemployed, path=['Region', 'States'], values='Estimated Unemployment Rate (%)', color_continuous_scale='rdylbu',
                  title='Unemployment rate in each Region and State', height=550, template='presentation')

fig.show()


# In[13]:


data


# In[64]:


before_lockdown= data[(data['Month_int'] >= 1) & (data['Month_int'] <=4)]
lockdown = data[(data['Month_int'] >= 4) & (data['Month_int'] <=7)]
before_lock= before_lockdown.groupby('States')['Estimated Unemployment Rate (%)'].mean().reset_index()
lock = lockdown.groupby('States')['Estimated Unemployment Rate (%)'].mean().reset_index()
lock['Unemployment Rate before lockdown'] = before_lock['Estimated Unemployment Rate (%)']
lock


# In[ ]:




