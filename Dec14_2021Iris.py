#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import percentile
import scipy.stats as stats
from numpy import median
df = pd.read_csv("...\Iris.csv", sep='\t', index_col=0)
df.head()


# In[57]:


# replace minus operator with underscore
df['Species'] =  df['Species'].str.replace('-', '_')


# In[58]:


# distribution of Sepal Length for three species
sns.displot(data=df, x='SepalLengthCm', hue='Species', kind='kde', fill=True,
            palette=sns.color_palette('bright')[:3], height=5, aspect=1.5)
#mean
plt.axvline(x=df.SepalLengthCm.mean(),
            color='blue')


# In[59]:


#select fields
_df = df[['SepalLengthCm', 'PetalLengthCm']]


# In[62]:


# find the five number summary
quatiles = _df.quantile([.25,.50,.75])
df_max, df_min = _df.max(), _df.min()
df_max, df_min


# In[96]:


print(quartiles)
print()
print(df_max, df_min)


# In[73]:


#find z-score for sepal and petal length
zscore_df = _df.apply(stats.zscore)


# In[74]:


zscore_df


# In[75]:


#based on the z-score std. dev. Sepal Length have a bigger size than Petal Length.
sns.boxplot(data=zscore_df)
plt.show()
