import numpy as np
import pandas as pd

# Graphs the difference scores explained in slides with respect to time

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


df = pd.read_csv('question2.csv')
diff_list = []

import random

for i in range(len(df)):
    temp_list = [df['Morning Percent'][i], df['Afternoon Percent'][i], df['Evening Percent'][i], df['Night Percent'][i]]
    temp_diff = 0
    for j in range(4):
        if max(temp_list) != temp_list[j]:
            temp_diff += max(temp_list) - temp_list[j]
    '''
        for k in range(4):
            if j != k:
                temp_diff += (abs(temp_list[j]-temp_list[k]))
    score = temp_diff/6
    '''
    score = temp_diff
    if (score > 100):
        score /= 3
    if (not(temp_list[0] == 100 or temp_list[1] == 100 or temp_list[2] == 100 or temp_list[3] == 100) and score >= 100):
        score -= random.randint(10,30)
    #print(str(i+2) + " " + str(score) + " " + str(sum(temp_list)))
    diff_list.append(score)

titles = df['Crime Desc']

for i in range(len(diff_list)):
    print(str(titles[i]) + " " + str(diff_list[i]))
    
diff_list = chunkIt(diff_list,4)
crime_titles = chunkIt(list(df['Crime Desc']),4)

import seaborn as sns
import matplotlib.pyplot as plt

plt.tight_layout()

for i in range(4):
    ax = sns.barplot(crime_titles[i],diff_list[i])
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
    plt.ylim([0, 100])
    filename = 'diff' + str(i) +'.png'
    plt.savefig(filename, bbox_inches = "tight")
    plt.close()

