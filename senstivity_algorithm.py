# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:34:13 2024

@author: dhras
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#importing dataset
dataset=pd.read_csv("D://Dataset//sensitivity.csv")
x=dataset.iloc[:,0].values
y=dataset.iloc[:,-1].values
#dataset
x= x.reshape(-1, 1)
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=5)
x_poly=poly_reg.fit_transform(x)

from sklearn.linear_model import LinearRegression
regressor_2=LinearRegression()
regressor_2.fit(x_poly,y)

y_pred=regressor_2.predict(poly_reg.fit_transform(x))
pred_y=pd.DataFrame({"Actual value":y,"Predicted value":y_pred,"Difference":y-y_pred})
pred_y

from sklearn.metrics import r2_score
score=r2_score(y, y_pred)
score

plt.figure(dpi=300)
plt.scatter(x,y,color='red',label='Actual data points')
plt.plot(x,y_pred,color='blue',label='Predcited line')
plt.xlabel("Frequency")
plt.ylabel("Sensitivity")
plt.title("Frequency vs Sensitivity struct=15 um")
plt.text(0.5, 0.5, f'R2 Score: {score:.2f} , RI:{1.36}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)
plt.legend()
plt.show()

