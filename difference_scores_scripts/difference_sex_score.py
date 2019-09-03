import numpy as np
import pandas as pd
import random

# Graphs the difference scores explained in slides with respect to gender

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

df = pd.read_csv('minimized.csv')
diff_list = []


grouped_df = df.groupby('Crime Code')    
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]

for df in df_arr:
    #if(df['Crime Code Description'][0] == 'MANSLAUGHTER, NEGLIGENT' or df['Crime Code Description'][0] == 'CRIMINAL HOMICIDE'):
    #    continue
    ax = df.groupby('Victim Sex').count()['Date Reported']
    total = ax.sum()
    valX = 0
    valF = 0
    valM = 0
    if ('X' in ax.index):
        valX = (100*int(ax['X'])/total)
    if ('F' in ax.index):
        valF = (100*int(ax['F'])/total)
    if ('M' in ax.index):
        valM = (100*int(ax['M'])/total)
    temp_list = [valX, valF, valM]
    temp_diff = 0
    for j in range(3):
        if max(temp_list) != temp_list[j]:
            temp_diff += max(temp_list) - temp_list[j]
   
    score = temp_diff/2
    print(str(df['Crime Code Description'].iloc[0]) + " " + str(score))
    #score = temp_diff/3
    #print(str(i+2) + " " + str(score))
    diff_list.append(round(score,2))

diff_list = chunkIt(diff_list,4)
df2 = pd.read_csv('question2_age.csv')
crime_titles = chunkIt(list(df2['titles']),4)



import seaborn as sns
import matplotlib.pyplot as plt

for i in range(4):
    ax = sns.barplot(crime_titles[i],diff_list[i])
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
    plt.ylim([0, 100])
    filename = 'diff_sex' + str(i) +'.png'
    plt.savefig(filename, bbox_inches = "tight")
    plt.close()

