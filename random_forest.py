# -*- coding: utf-8 -*-
"""Random Forest

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hhviNTYx-kkhreVV5xJguZqVCxCZuZy1
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
# Replace 'your_dataset.csv' with your actual file path
data = pd.read_csv('/content/breast_cancer.csv')

# Define features (X) and target variable (y)
X = data.drop('Class', axis=1)
y = data['Class']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42) # Example parameters
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred_class = rf_classifier.predict(X_test)

# Evaluate the classifier
print("Classification Report:\n", classification_report(y_test, y_pred_class))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_class))

# --- Regression Example ---
# Load your regression dataset
# Load your regression dataset
data_reg = pd.read_csv('/content/Salary_Data.csv')

# Check for possible typos in the column name
# Print the actual column names in the DataFrame
print(data_reg.columns)

# Assuming the actual column name is 'YearsExperience', adjust your code:
X_reg = data_reg['YearsExperience']  # Corrected column name
y_reg = data_reg['Salary']

# ... (Rest of your code)
# Split the data
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
# Split the data
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Reshape X_train_reg and X_test_reg to be 2-dimensional
X_train_reg = X_train_reg.values.reshape(-1, 1)  # Reshape to a column vector
X_test_reg = X_test_reg.values.reshape(-1, 1)    # Reshape to a column vector

# Initialize and train a RandomForestRegressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train_reg, y_train_reg)

# Make predictions
y_pred_reg = rf_regressor.predict(X_test_reg)
# Evaluate the regressor
mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print("\nRegression Results:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Plot the results (for regression)
plt.figure(figsize=(8, 6))
plt.scatter(X_test_reg, y_test_reg, color='blue', label='Actual')
plt.plot(X_test_reg, y_pred_reg, color='red', label='Predicted')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Random Forest Regression')
plt.legend()
plt.show()