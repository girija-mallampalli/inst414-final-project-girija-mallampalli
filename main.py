import logging
from analysis import extract, transform, load
from model import train_random_forest
from evaluate import evaluate
from visualizations import visualize


def main():
    """
    Orchestrates the entire data processing, model training, evaluation, and visualization pipeline.
    
    """
    try:
        logging.info('Started the main function')

        # Model training and saving predictions
        rf_model, y_test, y_pred_rf = model()

        # Model evaluation and saving metrics
        mse_rf, r2_rf = evaluate()

        # Generating and saving visualizations
        visualize()

        logging.info('Main function completed successfully')
    except Exception as e:
        logging.error(f'Unexpected error in main function: {e}')
        raise
        
if __name__ == '__main__':
    main()
