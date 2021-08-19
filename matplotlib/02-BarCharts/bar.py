# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:56:48 2021

@author: rober
"""
#import csv
#import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []
#total=sum([item[1] for item in language_counter.most_common(15)])
#percentage=[]


for item in language_counter.most_common(15):
    #percentage.append(str(round(item[1]/total,2))+"%")
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
#percentage.reverse()

count=-0.2
for result in zip(languages,popularity):#,percentage):
  plt.barh(result[0], result[1],0.5,color="blue")
  plt.text(x=result[1]+5000,y=count,s=result[1],ha="center",color="red")
  count+=1
  
 
plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

    
#plt.tight_layout()

plt.show()

