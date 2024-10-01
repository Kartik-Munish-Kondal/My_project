#!/usr/bin/env python
# coding: utf-8

# #  import libraries to used 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # import and cleaning the data

# In[30]:


raw_data= pd.read_csv("C:\\Users\\HP\\Downloads\\Iris Flower - Iris.csv")
raw_data


# In[32]:


raw_data.isnull().sum()


# In[31]:


data=raw_data.drop("Id",axis=1)
data


# # Analysing and Visualising data

# In[7]:


data.describe()


# In[8]:


sns.pairplot(data,hue="Species")


# In[15]:


sns.scatterplot(x="SepalLengthCm",y="SepalWidthCm",data=data,hue="Species")


# ### by the plot above we can say thet Iris-virginica is the talest among the three. On the otherand, Iris-setosa is the shortest but with the most width

# # preparing data for training and testing

# In[23]:


from sklearn.model_selection import train_test_split
x=data.drop('Species',axis=1)
y= data['Species']
y


# In[24]:


x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.4,random_state=6)


# # fiting data in k Nearest Neighbor

# In[28]:


from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors = 5,p=2 )
knn.fit(x_train,y_train)


# # testing the model

# In[29]:


from sklearn import metrics
from sklearn.metrics import accuracy_score
knn.score(x_test,y_test)


# In[ ]:




