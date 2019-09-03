import numpy as np
import pandas as pd

# Removes most unnecessary data

# Reading in our dataset (357 MB)
df = pd.read_csv('Crime_Data_2010_2017.csv')

df.drop(df.columns[[0,6,9,12,13,14,15,16,17,18,19,20,21,22,23,24]],axis=1,inplace=True)
# Outputs to new CSV file (155 MB)

df = df[df['Crime Code'] != 110]
df = df[df['Crime Code'] != 113]
df.to_csv('minimized.csv',index=False)




