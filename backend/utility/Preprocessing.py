import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from datetime import datetime as dt
import pickle

df = pd.read_csv('final_data.csv',
                 parse_dates=["Date"])
model_df = df.groupby(['Commodity Name', 'City Name','Date']).agg({'Low Price':'mean',
                                                   'High Price':'mean'}).reset_index()

loaded_low_model = pickle.load(open("finalized_model_low.pkl", 'rb'))
loaded_high_model = pickle.load(open("finalized_model_high.pkl", 'rb'))


def model_build(final_list):
    output = {}
    output["high_price"] = round(loaded_high_model.predict(final_list)[0] / 40, 6)
    output["low_price"] = round(loaded_low_model.predict(final_list)[0] / 40, 6)
    return output

def preprocess(produceName, location, date_val):

    final_list = []
    print(date_val, type(date_val))
    final_list.append(date_val.month)
    final_list.append(date_val.year)
    final_list.append(date_val.day)

    commodity = CountVectorizer()
    commodity.fit(model_df['Commodity Name'].values)
    final_list.extend(np.array(commodity.transform([produceName]).todense()).tolist()[0])

    city = CountVectorizer()
    city.fit(model_df['City Name'].values)
    final_list.extend(np.array(city.transform([location]).todense()).tolist()[0][1:3])
    return np.array(final_list).reshape(1,-1)


def get_past_price(time_range, produceName, location):
    output = {}
    output["location"] = location
    output["predictions"] = []
    for date_val in time_range:        
        final_list = preprocess(produceName, location, date_val)
        print(final_list)
        result = model_build(final_list)
        
        result["date"] = date_val.strftime("%Y-%m-%d")
        output["predictions"].append(result)
    return output















