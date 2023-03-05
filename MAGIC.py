#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# In[ ]:


#load data to dataframe
data=pd.read_csv('dataset.csv')


# In[ ]:


data.head()


# In[ ]:


#check the missing values for each column
data.isna().sum()


# In[ ]:


#visualize the labels(virusnot a virus) ratio
sb.countplot(data['isVirus'])


# In[ ]:


#visualize the data 
sb.pairplot(data,hue='isVirus')


# In[ ]:


#use mean value for each column to impute missing values
data['feature_1'] = data['feature_1'].fillna(data['feature_1'].mean())
data['feature_2'] = data['feature_2'].fillna(data['feature_2'].mean())
data['feature_3'] = data['feature_3'].fillna(data['feature_3'].mean())
data['feature_4'] = data['feature_4'].fillna(data['feature_4'].mean())


# In[ ]:


#check again missing values
data.isna().sum()


# In[ ]:


#visualize cleaned data
sb.pairplot(data=data, hue='isVirus', diag_kind='hist', 
             plot_kws={'alpha':0.6, 's':80, 'edgecolor':'k'},
             diag_kws={'alpha':0.6, 'edgecolor':'k', 'linewidth':0.5},
             palette=sb.color_palette(['#4C72B0', '#C49B4E']));


# In[ ]:


#I was able to do until this part.I don't have knowledge about machine learning models.I google it 
#and i find the ways of how the train model(Logistic Regression,Random Forest Classifier) but 
#as ı mentioned earlier i dont know much thing about machine learning.So i cant create model and 
#evaluate the model.

