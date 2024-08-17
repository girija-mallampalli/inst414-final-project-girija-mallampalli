import logging
from analysis import extract, transform, load
from model import train_random_forest
from evaluate import evaluate
from visualizations import visualize


def main():
    """
    Orchestrates the entire data processing pipeline, including ETL (Extract, Transform, Load),
    model training, evaluation, and visualization.

    Raises:
        Exception: If any step in the pipeline fails, an exception is logged and re-raised.
    """
    try:
        logging.info('Started the main execution')

        # ETL Process
        hosp_df = extract()
        hosp_df_cleaned = transform(hosp_df)
        load(hosp_df_cleaned)

        # Model Training
        model_results = train_random_forest(hosp_df_cleaned)

        # Evaluation
        evaluate(model_results)

        # Visualization
        visualize()

        logging.info('Main execution completed successfully')

    except Exception as e:
        logging.error(f'Error during main execution: {e}')
        raise
        
if __name__ == '__main__':
    main()
