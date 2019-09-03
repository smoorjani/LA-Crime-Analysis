import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Presents graphs that display the number of victims based on their gender

df = pd.read_csv('minimized.csv')

df['Victim Sex'] = df['Victim Sex']

grouped_df = df.groupby('Crime Code')    
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]
counter = 0

for df in df_arr:
    #print(df.groupby('Time Occurred').count()['Date Reported'])

    ax = df.groupby('Victim Sex').count()['Date Reported'].plot(kind='bar',title=df['Crime Code Description'].iloc[0],figsize=(15, 10),fontsize=12)
    ax.set_xlabel("Sex", fontsize=12)
    ax.set_ylabel("# of Crimes", fontsize=12)
    filename = 'crime_sex' + str(counter) + '.png'
    plt.savefig(filename)
    plt.close()
    counter += 1
