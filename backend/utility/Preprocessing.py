import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from datetime import datetime as datetime


def preprocess(produceName, location):

    df = pd.read_csv('final_data.csv',
                 parse_dates = ["Date"])
    model_df = df.groupby(['Commodity Name', 'City Name','Date']).agg({'Low Price':'mean',
                                                   'High Price':'mean'}).reset_index()
    final_list = []
    final_list.append(datetime.now().month)
    final_list.append(datetime.now().year)
    final_list.append(datetime.now().day)

    commodity = CountVectorizer()
    commodity.fit(model_df['Commodity Name'].values)
    final_list.extend(np.array(commodity.transform([produceName]).todense()).tolist()[0])

    city = CountVectorizer()
    city.fit(model_df['City Name'].values)
    final_list.extend(np.array(city.transform([location]).todense()).tolist()[0][1:3])

    return np.array(final_list).reshape(1,-1)







