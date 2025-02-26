import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset  
df = pd.read_csv('train.csv') 
df.head(1) 
 
# Convert 'Order Date' to datetime format 
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce') 
df['Year'] = df['Order Date'].dt.year 
df['Month'] = df['Order Date'].dt.month 

df = df[['Year', 'Month', 'Sales']] 

# Feature selection 
X = df[['Year', 'Month']]
y = df['Sales'] 

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Remove Nan 
X_train = X_train.dropna() 
y_train = y_train.dropna() 
# Train the model 

model = LinearRegression() 
model.fit(X_train, y_train) 

# Make predictions
X_test = X_test.dropna()
y_test = y_test.dropna()
y_pred = model.predict(X_test)

# Combine X_train and y_train into one DataFrame
df_train = pd.concat([X_train, y_train], axis=1)

# Drop rows with missing values
df_train = df_train.dropna()

# Reset index for X and y to align them
X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)

# Verify the shapes match
print(X_train.shape, y_train.shape)  
print(X_test.shape, y_test.shape)    

# Evaluate the model 
mae = mean_absolute_error(y_test, y_pred) 
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R^2 Score: {r2}")

# Visualizing actual vs predicted sales
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()