import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Presents visuals which shows the number of victims in an age group

df = pd.read_csv('minimized.csv')

df['Victim Age'] = df['Victim Age']

grouped_df = df.groupby('Crime Code')    
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]
counter = 0

for df in df_arr:
    #print(df.groupby('Time Occurred').count()['Date Reported'])
    times = list(range(0,100,5))

    ax = df.groupby('Victim Age').count().reindex(times,fill_value=0)['Date Reported'].plot(kind='bar',title=df['Crime Code Description'].iloc[0],figsize=(15, 10),fontsize=12)
    ax.set_xlabel("Age", fontsize=12)
    ax.set_ylabel("# of Crimes", fontsize=12)
    filename = 'crime_age' + str(counter) + '.png'
    plt.savefig(filename)
    plt.close()
    counter += 1
