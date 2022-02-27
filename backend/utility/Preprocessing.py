import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

import pickle

df = pd.read_csv('final_data.csv',
                 parse_dates=["Date"])

loaded_low_model = pickle.load(open("finalized_model_low.pkl", 'rb'))
loaded_high_model = pickle.load(open("finalized_model_high.pkl", 'rb'))


def model_build(final_list):
    output = {}
    output["high_price"] = round(loaded_high_model.predict(final_list)[0] / 40, 2)
    output["low_price"] = round(loaded_low_model.predict(final_list)[0] / 40, 2)
    return output

def preprocess(produceName, location, date):
    model_df = df.groupby(['Commodity Name', 'City Name','Date']).agg({'Low Price':'mean',
                                                   'High Price':'mean'}).reset_index()
    final_list = []
    final_list.append(date.month)
    final_list.append(date.year)
    final_list.append(date.day)

    commodity = CountVectorizer()
    commodity.fit(model_df['Commodity Name'].values)
    final_list.extend(np.array(commodity.transform([produceName]).todense()).tolist()[0])

    city = CountVectorizer()
    city.fit(model_df['City Name'].values)
    final_list.extend(np.array(city.transform([location]).todense()).tolist()[0][1:3])
    return np.array(final_list).reshape(1,-1)


def get_past_price(time_range, produceName, location):
    output = {}
    output[produceName]["location"] = location
    output[produceName]["predictions"] = []
    for date_val in time_range:
        final_list = preprocess(produceName, location, date_val)
        result = model_build(final_list)
        result["date"] = date_val
        output[produceName]["predictions"].append(result)
    return output















