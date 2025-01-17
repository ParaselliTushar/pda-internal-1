# -*- coding: utf-8 -*-
"""LVADSUSR126-Tushar-lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fHNN07MpPnv8yFaI-ihfvBl4GR33fbac
"""

import numpy as np
import pandas as pd
df=pd.read_csv('/content/booking.csv')
df.head()

df.describe()

df.info()

df.isnull().sum()

duplicate_rows = df.duplicated()
print(df[duplicate_rows])

df.drop_duplicates()
df.duplicated()

df.shape

from scipy.stats import zscore
numeric_df = df.select_dtypes(include=[np.number])
z_scores = zscore(numeric_df)

abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
df_cleaned = df[filtered_entries]

print("Original DataFrame:")
print(df.shape)
print("\nDataFrame after removing outliers:")
print(df_cleaned.shape)

df.corr()

import seaborn as sns

sns.heatmap(df.corr(),annot=True)

df.duplicated().sum()
df.drop_duplicates()

sns.boxplot(df)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['type of meal']=le.fit_transform(df['type of meal'])
df['room type']=le.fit_transform(df['room type'])
df['booking status']=le.fit_transform(df['booking status'])
df['market segment type']=le.fit_transform(df['market segment type'])
df.head()

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
x=df[['number of weekend nights','number of week nights','market segment type','repeated','lead time','average price','room type']]
y=df['booking status']
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.4,random_state=42)
model.fit(train_x,train_y)
pred=model.predict(test_x)
print(pred)

import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(features, weights):
    z = np.dot(features, weights)
    return sigmoid(z)

features = np.array([[1, 2], [2, 3], [3, 4]])
weights = np.array([0.5, -0.5])

predictions = predict(features, weights)
print(predictions)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

accuracy = accuracy_score(test_y, pred)
precision = precision_score(test_y, pred)
recall = recall_score(test_y, pred)

f1 = f1_score(test_y, pred)

conf_matrix = confusion_matrix(test_y, pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:")
print(conf_matrix)