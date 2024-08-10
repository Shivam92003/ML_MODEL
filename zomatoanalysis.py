# -*- coding: utf-8 -*-
"""ZomatoAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NK3td_s3uW_1so6vrqFB3AA0ek0m5FXr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Zomato data .csv')

df.sample(10)

def handleRate(value):
  value = str(value).split('/')
  value = value[0]
  return float(value)

df['rate']=df['rate'].apply(handleRate)
print(df.head())

df.info()

df.head()

"""Q1. What type of resturant do the majority of customers order from?"""

sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of Resturant")

"""Q2. How many votes has each type of restaurant received from customers?"""

sns.barplot(data=df, y='votes', x='listed_in(type)')

group_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':group_data})
plt.plot(result,c="purple",marker="o")
plt.xlabel("Type of Resto ",c="green",size=3)
plt.ylabel("Votes ",c="green",size=3)

"""Q3. What are the ratings that the majority of resturants have received?"""

plt.hist(df['rate'],bins=10)
plt.title("Ratings of Resto")
plt.xlabel("Ratings")
plt.ylabel("Frequency")

"""Q4. Zomato has observed that most couples order most of their food online. What is their average spending on each order?"""

couple_data =df['approx_cost(for two people)']
sns.countplot(x=couple_data)

"""Q5. Which mode (online or offline) has received the maximum rating?"""

plt.figure(figsize=(5,5))
sns.boxplot(x='online_order',y='rate',data=df)

"""Q6. Which type of restaurant received more offline orders, so that Zomato can customers with some good offers?"""

pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt='d')
plt.title('Offline vs Online Orders by Type of Restaurant')
plt.xlabel("Online Order")
plt.ylabel("Type of Reesto")
plt.show()
