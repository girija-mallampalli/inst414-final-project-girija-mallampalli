import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import etl.load


hosp_df_cleaned = pd.read_csv('Hospital_General_Ratings_Cleaned.csv')

# Initialize the label encoder
label_encoder = LabelEncoder()

# List of columns to encode
columns_to_encode = ['Effectiveness of care national comparison', 
                      'Readmission national comparison', 
                      'Timeliness of care national comparison', 
                      'Efficient use of medical imaging national comparison', 
                      'Patient experience national comparison']

# Loop through each column and apply label encoding
for column in columns_to_encode:
    if column in hosp_df_cleaned.columns:
        hosp_df_cleaned[column] = label_encoder.fit_transform(hosp_df_cleaned[column].astype(str))


# Define features and target variable
X = hosp_df_cleaned[['Effectiveness of care national comparison', 
                     'Readmission national comparison',
                     'Timeliness of care national comparison',
                     'Efficient use of medical imaging national comparison']]
y = hosp_df_cleaned['Patient experience national comparison']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Regressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

