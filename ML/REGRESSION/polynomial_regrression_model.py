# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 19:14:54 2025

@author: Supravata
"""

import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv(r"C:\Users\Supravata\Desktop\datascience\pdfs\excels\emp_sal.csv")


x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)


# linear regression visualization
plt.scatter(x, y, color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title('Linear regression graph')
plt.xlabel(('position level'))
plt.ylabel('salary')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(x)

poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()
lin_reg_2.fit(x_poly,y)

#polynomial regression visualizaation
plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('truth or bluff (polynimial regression')
plt.xlabel(('position level'))
plt.ylabel('salary')
plt.show()

# prediction
lin_model_pred=lin_reg.predict([[6.5]])
print(lin_model_pred)

poly_model_pred=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)

#svr (support vector regression)

from sklearn.svm import SVR
svr_model=SVR(kernel='poly',degree=3,gamma='auto',C=1)
svr_model.fit(x,y)

svr_model_pred=svr_model.predict([[6.5]])
print(svr_model_pred)

# knn reggression model
from sklearn.neighbors import KNeighborsRegressor
knn_model=KNeighborsRegressor(n_neighbors=5,weights='distance',algorithm='brute',p=1)
knn_model.fit(x,y)


knn_model_pred=knn_model.predict([[6.5]])
print(knn_model_pred)


# decission tree model
from sklearn.tree import DecisionTreeRegressor
dt_model=DecisionTreeRegressor()
dt_model.fit(x,y)

dt_model_pred=dt_model.predict([[6.5]])
print(dt_model_pred)

# random forest
from sklearn.ensemble import RandomForestRegressor
rf_model=RandomForestRegressor(n_estimators=23,random_state=0)
rf_model.fit(x,y)

rf_model_pred=rf_model.predict([[6.5]])
print(rf_model_pred)