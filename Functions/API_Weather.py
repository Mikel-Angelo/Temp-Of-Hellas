#!/usr/bin/env python
# coding: utf-8

# ---
# # Import Libraries

# In[1]:


from weatherbit.api import Api

import pandas as pd


# ---
# # Import Functions

# In[2]:


api_key = "22f849e233da44399648441609edde9d"
api = Api(api_key)


# In[3]:


def Extract_Data_For_Specific_Location_Weather(name, lat, lon):
    try:
        dataframe_data = api.get_forecast(lat=lat, lon=lon, city=name, days=15, tp='daily').get(['datetime', 'temp', 'max_temp', 'min_temp'])
        
        dataframe = pd.DataFrame(data=dataframe_data)
        dataframe.drop(['timestamp_utc','timestamp_local'], axis=1, inplace=True)
        dataframe['Latitude'] = lat
        dataframe['Longitude'] = lon
    
        return dataframe

    except: print('No, options!')


# ---

# In[ ]:




