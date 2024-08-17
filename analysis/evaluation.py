import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from data import outputs

# Setting up logging
logging.basicConfig(filename='data/logs/evaluate.log', level=logging.DEBUG, 
                    format='%(asctime)s %(message)s')

def evaluate():
   """
    Evaluates the performance of the Random Forest Regressor model using mean squared error (MSE) and R-squared (R2) metrics.
    
    Returns:
        tuple: A tuple containing the Mean Squared Error (`mse_rf`) and R-squared (`r2_rf`) values.

    Raises:
        Exception: If any error occurs during the evaluation or saving process, 
                   the error is logged, and the exception is re-raised.
    """
    try:
        logging.info('Started model evaluation')
        predictions = pd.read_csv('data/model/rf_predictions.csv')

        mse_rf = mean_squared_error(predictions['y_test'], predictions['y_pred_rf'])
        r2_rf = r2_score(predictions['y_test'], predictions['y_pred_rf'])

        logging.info('Model evaluation completed successfully')

        # Save the evaluation metrics
        os.makedirs('data/outputs', exist_ok=True)
        pd.DataFrame({'MSE': [mse_rf], 'R2': [r2_rf]}).to_csv('data/outputs/evaluation_metrics.csv', index=False)
        logging.info('Evaluation metrics saved successfully')

        return mse_rf, r2_rf
    except Exception as e:
        logging.error(f'Error during model evaluation: {e}')
        raise
