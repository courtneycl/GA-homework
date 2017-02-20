
# coding: utf-8

# In[21]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[87]:

#This dataset has 63 features - only add the columns that we are interested in 
data = pd.read_csv('./assets/Crashes.csv', usecols=['XCOORD', 'YCOORD', 'INTERSECTIONTYPE', 'ISWORKZONERELATED', 'STREETLIGHTING', 'FIRSTHARMFULEVENTSPECIFICS', 'ADDRESS1', 'LIGHTCONDITION', 'WEATHER', 'REPORTDATE', 'ISDRINKING', 'CYCLISTSINVOLVED', 'PEDESTRIANSINVOLVED', 'MINORINJURIES', 'MAJORINJURIES', 'FATALITIES'])


# In[88]:

data.head()


# In[89]:

#fill NaN data with 0 
data.CYCLISTSINVOLVED.fillna(0, inplace=True)
data.PEDESTRIANSINVOLVED.fillna(0, inplace=True)
data.MINORINJURIES.fillna(0, inplace=True)
data.MAJORINJURIES.fillna(0, inplace=True)
data.FATALITIES.fillna(0, inplace=True)


# In[90]:

#convert floats to ints to simplify 
data.CYCLISTSINVOLVED = data.CYCLISTSINVOLVED.astype(int)
data.PEDESTRIANSINVOLVED = data.PEDESTRIANSINVOLVED.astype(int)
data.MINORINJURIES = data.MINORINJURIES.astype(int)
data.MAJORINJURIES = data.MAJORINJURIES.astype(int)
data.FATALITIES = data.FATALITIES.astype(int)


# In[91]:

data.head()


# In[92]:

event_dummies = pd.get_dummies(data.FIRSTHARMFULEVENTSPECIFICS, prefix='event')
event_dummies.head(1)


# In[93]:

data = data.join(event_dummies.ix[:, 'event_Bridge Overhead Structure':])


# In[94]:

light_dummies = pd.get_dummies(data.LIGHTCONDITION, prefix='light')
light_dummies.head(1)


# In[95]:

data = data.join(light_dummies.ix[:, 'light_Dark-Lighted':])


# In[96]:

drinking_dummies = pd.get_dummies(data.ISDRINKING, prefix='drink')
drinking_dummies.head(1)


# In[97]:

data = data.join(drinking_dummies.ix[:, 'drink_No data provided'])


# In[98]:

intersection_dummies = pd.get_dummies(data.INTERSECTIONTYPE, prefix='int')
intersection_dummies.head(1)


# In[99]:

data = data.join(intersection_dummies.ix[:, 'int_Four-Way Intersection':])
data.head()


# In[100]:

data = data.drop(['event_Unknown', 'event_null', 'light_null', 'drink_No data provided','int_null'], 1)


# In[101]:

data.corr()


# In[ ]:



