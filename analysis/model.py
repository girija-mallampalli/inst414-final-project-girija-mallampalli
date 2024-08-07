from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import data.loaded

# Define features and target variable
X = hosp_df_cleaned[['Effectiveness of care national comparison', 'Readmission national comparison', 'Timeliness of care national comparison', 'Efficient use of medical imaging national comparison']]
y = hosp_df_cleaned['Patient experience national comparison']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
