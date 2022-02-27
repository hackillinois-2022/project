import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

from backend.service.service import Service

df = pd.read_csv('final_data.csv',
                 parse_dates=["Date"])

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
        result = Service.model_build(final_list)
        result["date"] = date_val
        output[produceName]["predictions"].append(result)
    return output















