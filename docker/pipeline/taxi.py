#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas pyarrow fastparquet')


# In[27]:


import pandas as pd
df = pd.read_parquet(
    "data/green_tripdata_2025-11.parquet"
)

df.head()


# In[28]:


df.shape[1]


# In[29]:


df.drop('ehail_fee', axis=1)


# In[30]:


df.query("trip_distance <= 1").shape[0]


# In[26]:


len(df.columns)


# In[4]:


df.query("trip_distance <= 100") \
  .sort_values("trip_distance", ascending=False) \
  .head(1)


# In[5]:


print(df.columns)


# In[6]:


df.groupby('PULocationID')['fare_amount'] \
  .sum() \
  .sort_values(ascending=False) \
  .head(2)


# In[7]:


import sys
sys.executable


# In[8]:


get_ipython().run_line_magic('pip', 'install sqlalchemy psycopg2-binary')


# In[9]:


from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://root:root@localhost:5432/ny_taxi"
)


# In[11]:


print(pd.io.sql.get_schema(df, name='green_taxi_data', con=engine))


# In[12]:


df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')


# In[14]:


df.to_sql(
    name="green_taxi_data",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=100_000,
    method="multi"
)


# In[19]:


print(len(df))


# In[ ]:




