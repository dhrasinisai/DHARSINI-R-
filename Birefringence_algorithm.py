# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:58:24 2024

@author: dhras
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv("D://Dataset//sensitivity.csv")
x=dataset.iloc[:,0].values
y=dataset.iloc[:,-1].values

#reshaping
x=x.reshape(-1,1)

#importing algorithm
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(x)

#importing linear regression
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_poly,y)

#predicting the y value
pred_y=regressor.predict(poly_reg.fit_transform(x))
pred_y

#calculating r2 score
from sklearn.metrics import r2_score
score=r2_score(y,pred_y)
score

#plotting
plt.figure(dpi=300)
plt.scatter(x,y,color='red',label='Actual Values')
plt.plot(x,pred_y,color='blue',label='Predicted Line')
plt.xlabel("Frequency")
plt.ylabel('Birefringence')
plt.title('Frequency vs Birefringence struct=10 um')
plt.text(0.5, 0.5, f'R2 Score: {score:.2f} , RI:{1.36}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)
plt.legend()
plt.show()