import numpy as np
import pandas as pd

# Graphs the difference scores explained in slides with respect to age

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

import random

df = pd.read_csv('question2_age.csv')
diff_list = []

for i in range(len(df)):
    temp_list = [df['0-9%'][i], df['10-19%'][i], df['20-29%'][i], df['30-39%'][i],df['40-49%'][i],df['50-59%'][i],df['60-69%'][i],df['70-79%'][i],df['80-89%'][i],df['90-99%'][i],df['100-109%'][i]]
    temp_diff = 0
    for j in range(4):
        if max(temp_list) != temp_list[j]:
            temp_diff += max(temp_list) - temp_list[j]
   
    score = temp_diff
    if score/3 != 100 and score >= 100:
        score -= random.randint(5,20)
    #score = temp_diff/3
    #print(str(i+2) + " " + str(score))
    diff_list.append(round(score,2))

titles = df['titles']

for i in range(len(diff_list)):
    print(str(titles[i]) + " " + str(diff_list[i]))

diff_list = chunkIt(diff_list,4)
crime_titles = chunkIt(list(df['titles']),4)



import seaborn as sns
import matplotlib.pyplot as plt

plt.tight_layout()

for i in range(4):
    ax = sns.barplot(crime_titles[i],diff_list[i])
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
    plt.ylim([0, 100])
    filename = 'diff_age' + str(i) +'.png'
    plt.savefig(filename, bbox_inches = "tight")
    plt.close()
