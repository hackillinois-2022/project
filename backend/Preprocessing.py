#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import pickle

df = pd.read_csv('final_data.csv', 
                 parse_dates = ["Date"])
model_df = df.groupby(['Commodity Name', 'City Name','Date']).agg({'Low Price':'mean',
                                                        'High Price':'mean'}).reset_index()
model_df['Date'] = pd.to_datetime(model_df['Date'])
model_df['Month'] = pd.DatetimeIndex(model_df['Date']).month
model_df['Year'] = pd.DatetimeIndex(model_df['Date']).year
model_df['Day'] = pd.DatetimeIndex(model_df['Date']).day

model_df1 = pd.get_dummies(model_df, prefix=['Commodity Name', 'City Name'])
model_df1 = model_df1.dropna()

y_low = model_df1['Low Price']
y_high = model_df1['High Price']
X = model_df1.drop(['Low Price', 'High Price','Date'], axis=1)

for col in X.columns:
    X[col] = X[col].astype('int')
    
commodity = CountVectorizer()
commodity.fit(model_df['Commodity Name'].values)

city = CountVectorizer()
city.fit(model_df['City Name'].values)


# In[ ]:




