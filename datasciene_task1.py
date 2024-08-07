# -*- coding: utf-8 -*-
"""datasciene_TASK1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11oeLgxTylCsRdkahil7gAhGoNF6YgG6n
"""

# Import necessary libraries



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from google.colab import files


# -- steps involving the building the machine learning model--#


#load dataset

#explore

#preprossing like cleaning etc

#reomove any null if present and remove any missing value presnet

#train the model at the ratio of 70:30

#test the sample data

#accuracy calaculation

file_name = list(uploaded.keys())[0]

df = pd.read_csv(file_name)

print(df.head())

X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#trianing the dataset

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=df['Species'].unique())

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)