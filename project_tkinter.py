# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:34:28 2024

@author: dhras
"""

import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load your dataset
dataset = pd.read_csv("D://Dataset//project.csv")
cleaned_data = dataset.dropna()
x = cleaned_data.iloc[:, [-4, -3, -2]]
y = cleaned_data.iloc[:, -1].values

# Feature scaling
sc = StandardScaler()
x_scaled = sc.fit_transform(x)

# Train the model
regressor = RandomForestRegressor(n_estimators=6, random_state=0)
regressor.fit(x_scaled, y)

# Create Tkinter GUI
class ModelApp:
    def __init__(self, master):
        self.master = master
        master.title("Model Deployment App")

        self.label1 = tk.Label(master, text="Feature 1:")
        self.label1.grid(row=0, column=0)
        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Feature 2:")
        self.label2.grid(row=1, column=0)
        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1)

        self.label3 = tk.Label(master, text="Feature 3:")
        self.label3.grid(row=2, column=0)
        self.entry3 = tk.Entry(master)
        self.entry3.grid(row=2, column=1)

        self.predict_button = tk.Button(master, text="Predict", command=self.predict)
        self.predict_button.grid(row=3, columnspan=2)

    def predict(self):
        # Get input from entry fields
        feature1 = float(self.entry1.get())
        feature2 = float(self.entry2.get())
        feature3 = float(self.entry3.get())

        # Scale the input features
        input_data = sc.transform([[feature1, feature2, feature3]])

        # Make prediction
        prediction = regressor.predict(input_data)

        # Display prediction
        messagebox.showinfo("Prediction", f"The model predicts: {prediction[0]}")

def main():
    root = tk.Tk()
    app = ModelApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
