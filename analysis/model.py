import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from data import loaded


# Setting up logging
logging.basicConfig(filename='data/logs/model.log', level=logging.DEBUG, 
                    format='%(asctime)s %(message)s')

def model():
     """
    Trains a Random Forest Regressor model using the cleaned hospital data and saves the predictions.

    Returns:
        tuple: A tuple containing the trained Random Forest model (`rf_model`), 
               the actual target values from the test set (`y_test`), 
               and the predicted values (`y_pred_rf`).

    Raises:
        Exception: If any error occurs during the model training or saving process, 
                   the error is logged, and the exception is re-raised.
    """
    try:
        logging.info('Started model training')
        hosp_df_cleaned = pd.read_csv('data/loaded/hosp_df_cleaned.csv')
        
        features = hosp_df_cleaned.drop(columns=['State'])
        target = hosp_df_cleaned['State']

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        # Random Forest Model
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_model.fit(X_train, y_train)
        y_pred_rf = rf_model.predict(X_test)

        logging.info('Model training completed successfully')

        # Save the model predictions
        os.makedirs('data/outputs', exist_ok=True)
        pd.DataFrame({'y_test': y_test, 'y_pred_rf': y_pred_rf}).to_csv('data/outputs/rf_predictions.csv', index=False)
        logging.info('Model predictions saved successfully')

        return rf_model, y_test, y_pred_rf
    except Exception as e:
        logging.error(f'Error during model training: {e}')
        raise

