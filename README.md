Sales Forecasting Using Machine Learning

Project Overview
This project implements a Linear Regression model to predict future sales based on historical data. The dataset contains order dates and sales values, from which features like year and month are extracted for forecasting future trends.

Technologies Used

Python
Pandas (Data manipulation)
NumPy (Numerical computations)
Matplotlib & Seaborn (Data visualization)
Scikit-learn (Machine Learning framework)

Dataset
The dataset contains:
Order Date: Date of the sale transaction
Sales: Sales revenue for the given transaction

Steps Involved
Load and Preprocess Data:
Convert the Order Date column to datetime format.
Extract Year and Month as features.
Select relevant columns for modeling.

Feature Selection:

Independent Variables: Year, Month
Target Variable: Sales

Split Dataset:
80% Training, 20% Testing

Train the Model:
Implement Linear Regression using scikit-learn

Make Predictions:
Use the trained model to predict sales on test data.

Evaluate Performance:
Calculate MAE, MSE, RMSE, and R² Score to measure accuracy.

Visualization:

Plot Actual vs Predicted Sales using a Seaborn scatterplot.
Project Outputs
After running the model, the following outputs are generated:

Performance Metrics:
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score

Predicted Sales vs Actual Sales Scatterplot:
A scatterplot visualization comparing actual sales to predicted sales.

Sales Trend Analysis:
Insights on sales patterns based on historical data.
