import os
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Setting up logging
logging.basicConfig(filename='data/project.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')

def extract():
    try:
        logging.info('Started data extraction')
        hosp_df = pd.read_csv('Hospital_General_Ratings.csv', encoding='latin1')
        logging.info('Data extraction completed successfully')
        return hosp_df
    except Exception as e:
        logging.error(f'Error during data extraction: {e}')
        raise

def transform(hosp_df):
    try:
        logging.info('Started data transformation')
        hosp_df_cleaned = hosp_df[['State', 'Readmission national comparison', 'Patient experience national comparison', 
                                   'Effectiveness of care national comparison', 'Timeliness of care national comparison', 
                                   'Efficient use of medical imaging national comparison']]
        hosp_df_cleaned = hosp_df_cleaned.replace('Not Available', pd.NA)
        hosp_df_cleaned = hosp_df_cleaned.dropna()

        # Encode categorical variables
        label_encoder = LabelEncoder()
        columns_to_encode = ['Effectiveness of care national comparison', 'Readmission national comparison', 
                             'Timeliness of care national comparison', 'Efficient use of medical imaging national comparison', 
                             'Patient experience national comparison']
        for column in columns_to_encode:
            hosp_df_cleaned[column] = label_encoder.fit_transform(hosp_df_cleaned[column].astype(str))
        
        logging.info('Data transformation completed successfully')
        return hosp_df_cleaned
    except Exception as e:
        logging.error(f'Error during data transformation: {e}')
        raise

def load(hosp_df_cleaned):
    try:
        logging.info('Started data loading')
        os.makedirs('data/cleaned', exist_ok=True)
        hosp_df_cleaned.to_csv('data/hosp_df_cleaned.csv', index=False)
        logging.info('Data loading completed successfully')
    except Exception as e:
        logging.error(f'Error during data loading: {e}')
        raise

def model(hosp_df_cleaned):
    try:
        logging.info('Started model training')
        features = hosp_df_cleaned.drop(columns=['State'])
        target = hosp_df_cleaned['State']  # Replace 'State' with the actual target variable if different

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        # Linear Regression Model
        lr_model = LinearRegression()
        lr_model.fit(X_train, y_train)
        y_pred_lr = lr_model.predict(X_test)

        mse_lr = mean_squared_error(y_test, y_pred_lr)
        r2_lr = r2_score(y_test, y_pred_lr)

        # Random Forest Model
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_model.fit(X_train, y_train)
        y_pred_rf = rf_model.predict(X_test)

        mse_rf = mean_squared_error(y_test, y_pred_rf)
        r2_rf = r2_score(y_test, y_pred_rf)

        logging.info('Model training completed successfully')
        return {
            'Linear Regression': {'model': lr_model, 'MSE': mse_lr, 'R2': r2_lr},
            'Random Forest': {'model': rf_model, 'MSE': mse_rf, 'R2': r2_rf}
        }
    except Exception as e:
        logging.error(f'Error during model training: {e}')
        raise

def evaluate_and_visualize(results):
    try:
        logging.info('Started model evaluation and visualization')
        os.makedirs('data/evaluation', exist_ok=True)

        # Save evaluation metrics to CSV
        metrics_df = pd.DataFrame({
            'Model': ['Linear Regression', 'Random Forest'],
            'MSE': [results['Linear Regression']['MSE'], results['Random Forest']['MSE']],
            'R2': [results['Linear Regression']['R2'], results['Random Forest']['R2']]
        })
        metrics_df.to_csv('data/metrics.csv', index=False)

        # Plotting and saving charts
        plt.figure(figsize=(10, 5))

        # Plot for MSE
        plt.subplot(1, 2, 1)
        plt.bar(metrics_df['Model'], metrics_df['MSE'])
        plt.title('Mean Squared Error')
        plt.xlabel('Model')
        plt.ylabel('MSE')

        # Plot for R2
        plt.subplot(1, 2, 2)
        plt.bar(metrics_df['Model'], metrics_df['R2'])
        plt.title('R-squared')
        plt.xlabel('Model')
        plt.ylabel('R2')

        # Save the plot
        plt.tight_layout()
        plt.savefig('data/model_performance.png')
        plt.show()

        logging.info('Model evaluation and visualization completed successfully')
    except Exception as e:
        logging.error(f'Error during evaluation and visualization: {e}')
        raise

def main():
    try:
        logging.info('Started the main function')

        # ETL Process
        hosp_df = extract()
        hosp_df_cleaned = transform(hosp_df)
        load(hosp_df_cleaned)

        # Modeling
        results = model(hosp_df_cleaned)

        # Evaluation and Visualization
        evaluate_and_visualize(results)

        logging.info('Finished the main function successfully')
    except Exception as e:
        logging.error(f'Unexpected error in main function: {e}')

if __name__ == '__main__':
    main()
