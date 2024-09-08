#!/usr/bin/env python
# coding: utf-8

# ---
# # Import Libraries

# In[1]:


import pandas as pd


# ---
# # Import Functions

# In[2]:


def Prepare_Dataframe(name_of_dataframe, Coutry_Name):
    try:
        for _ in range(len(name_of_dataframe.columns)):
            name_of_dataframe.rename(columns={name_of_dataframe.columns[_] : Coutry_Name+'_'+name_of_dataframe.columns[_]}, inplace=True)
        return name_of_dataframe
    
    except:
        print('No, options!')


# ---

# In[ ]:




