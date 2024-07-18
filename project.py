# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:54:54 2024

@author: dhras
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv("D://Dataset//project.csv")
cleaned_data=dataset.dropna()
cleaned_data

cleaned_data['Age_Label'] = pd.factorize(cleaned_data['Age'])[0]

x=cleaned_data.iloc[:,]
y=cleaned_data.iloc[:,-1].values


import seaborn as sns
plt.figure(dpi=300)
numeric_data=cleaned_data.select_dtypes(include='number')
sns.heatmap(numeric_data.corr(),annot=True,cmap='winter')
plt.show()


#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit_transform(x)

#splitting into train and test data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

#model fitting
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=6,random_state=0)
regressor.fit(x_train,y_train)

#predicting y value
y_pred=regressor.predict(x_test)
y_pred

#Data frame
pred_y=pd.DataFrame({"Actual value":y_test,"Predicted_value":y_pred,"Difference":y_test-y_pred})
pred_y

regressor.score(x_train,y_train)

from sklearn.metrics import r2_score
score=r2_score(y_test, y_pred)
score






'''from sklearn.model_selection import GridSearchCV

# Define the hyperparameters to tune
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt'],
    'bootstrap': [True, False]
}

# Create a GridSearchCV object
grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=0), param_grid=param_grid, cv=5, scoring='r2', n_jobs=-1)

# Fit the grid search to the data
grid_search.fit(x_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Use the best model for prediction
best_model = grid_search.best_estimator_
y_pred = best_model.predict(x_test)

# Evaluate the model
score = r2_score(y_test, y_pred)
print("R² Score:", score)'''










import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv("D://Dataset//project.csv")
cleaned_data = dataset.dropna()

# Labeling the age column
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
cleaned_data['Age'] = pd.factorize(cleaned_data['Age'])[0]
cleaned_data['Stay_In_Current_City_Years'] = pd.factorize(cleaned_data['Stay_In_Current_City_Years'])[0]
cleaned_data['Gender']=lb.fit_transform(cleaned_data['Gender'])
cleaned_data['City_Category']=lb.fit_transform(cleaned_data['City_Category'])





x = cleaned_data.iloc[:,2:11]
'''corr=x.corr()['Purchase'].sort_values(ascending=False)
corr'''
y = cleaned_data.iloc[:, -1].values


import seaborn as sns
plt.figure(dpi=300)
numeric_data = cleaned_data.select_dtypes(include='number')
sns.heatmap(numeric_data.corr(), annot=True, cmap='winter')
plt.show()




# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_scaled = sc.fit_transform(x)

# Splitting into train and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=0)

# Model fitting
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=6,random_state=0)
regressor.fit(x_train, y_train)

# Predicting y value
y_pred = regressor.predict(x_test)

# DataFrame
pred_y = pd.DataFrame({"Actual value": y_test, "Predicted_value": y_pred, "Difference": y_test - y_pred})
pred_y

# Model evaluation
regressor.score(x_train, y_train)

from sklearn.metrics import r2_score
score = r2_score(y_test, y_pred)
score

































