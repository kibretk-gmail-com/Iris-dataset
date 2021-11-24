#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("...file path", sep='\t')
#data source: ("https://www.kaggle.com/uciml/iris/version/2?select=Iris.csv")
df.head()


# In[2]:


df.isna().sum()


# In[3]:


df.info()


# In[9]:


#plot the correlation matrix of Petal Length(Cm), Petal Width(Cm), Sepal Length(Cm) and Sepal Width(Cm) in Iris data
df[['PetalLengthCm','PetalWidthCm','SepalLengthCm', 'SepalWidthCm']].corr()
sns.heatmap(df[['PetalLengthCm','PetalWidthCm','SepalLengthCm', 'SepalWidthCm']].corr(), annot=True, cmap = 'Reds')
plt.show()


# In[4]:


# replace minus operator with underscore
df['Species'] =  df['Species'].str.replace('-', '_')


# In[10]:


# distribution of Sepal Length for three species
sns.displot(data=df, x='SepalLengthCm', hue='Species', kind='kde', fill=True,
            palette=sns.color_palette('bright')[:3], height=5, aspect=1.5)
#mean
plt.axvline(x=df.SepalLengthCm.mean(),
            color='blue')


# In[11]:


# distribution of Sepal Width for three species
sns.displot(data=df, x='SepalWidthCm', hue='Species', kind='kde', fill=True,
            palette=sns.color_palette('bright')[:3], height=5, aspect=1.5)
#mean
plt.axvline(x=df.SepalWidthCm.mean(),
            color='blue')


# In[12]:


# distribution of Petal Length for three species
sns.displot(data=df, x='PetalLengthCm', hue='Species', kind='kde', fill=True,
            palette=sns.color_palette('bright')[:3], height=5, aspect=1.5)
#mean
plt.axvline(x=df.PetalLengthCm.mean(),
            color='blue')


# In[13]:


# distribution of Petal Width for three species
sns.displot(data=df, x='PetalWidthCm', hue='Species', kind='kde', fill=True,
            palette=sns.color_palette('bright')[:3], height=5, aspect=1.5)
#mean
plt.axvline(x=df.PetalWidthCm.mean(),
            color='blue')

