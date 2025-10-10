# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\Supravata\Desktop\datascience\pdfs\excels\salary_Data.csv")

# Select only numeric columns
dataset = dataset.select_dtypes(include=['float64', 'int64'])

# Drop any rows that contain missing values (NaN)
dataset = dataset.dropna()

x = dataset.iloc[:, :-1]  
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 

y_pred = regressor.predict(x_test)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

m = regressor.coef_[0]
print(m)

c = regressor.intercept_
print(c)

y_12 = m * 12 + c
print(y_12)

y_20 = m * 20 + c
print(y_20)

y_10 = m * 10 + c
print(y_10)

