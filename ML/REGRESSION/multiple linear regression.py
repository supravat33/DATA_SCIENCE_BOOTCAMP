# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 19:25:02 2025

@author: Supravata
"""

import pandas as pd
import matplotlib as plt
import numpy as np

dataset = pd.read_csv(r"C:\Users\Supravata\Desktop\datascience\pdfs\excels\Investment.csv")

X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,4]

X = pd.get_dummies(X,dtype=int)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train,Y_test = train_test_split(X,Y, test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred = regressor.predict(X_test)



m = regressor.coef_
print(m)

c = regressor.intercept_
print(c)

X = np.append(arr=np.full((50,1),42467).astype(int),values = X,axis = 1)


import statsmodels.api as sm 
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm 
X_opt = X[:,[0,1,2,3,5]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm 
X_opt = X[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm 
X_opt = X[:,[0,1,3]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm 
X_opt = X[:,[0,1]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

bias = regressor.score(X_train,Y_train)
bias