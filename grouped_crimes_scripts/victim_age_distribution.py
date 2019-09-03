import numpy as np
import pandas as pd

# Determining number of victims by age group and then assigning a score
# showing how uniform crimes are among an age group

df = pd.read_csv('minimized.csv')
df2 = pd.DataFrame()

df_titles = []
grouped_df = df.groupby('Crime Code') 
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]

for dfa in df_arr:
    df_titles.append(str(dfa['Crime Code Description'].iloc[0]))

df2['titles'] = df_titles

def grouped(lower, upper):
    return df.groupby('Crime Code')['Victim Age'].apply(lambda x: ((x<upper) & (x>=lower)).sum()).reset_index(name='count')

total = grouped(100,110)['count']

for i in range(0,11):
    df2[str(i*10)+'-'+str((i+1)*10-1)] = grouped((i*10),((i+1)*10))['count']
    total += df2[str(i*10)+'-'+str((i+1)*10-1)]

df2['total'] = total

for i in range(0,11):
    df2[str(i*10)+'-'+str((i+1)*10-1)+"%"] = df2[str(i*10)+'-'+str((i+1)*10-1)]*100/df2['total'].apply(lambda n: round(n, 2))
#new_df.columns = ['Crime Desc','df2']
df2.to_csv('question2_age.csv',index=False)
