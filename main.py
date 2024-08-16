import logging
from etl import extract, transform, load
from modeling import train_model
from evaluation import evaluate_and_visualize

def main():
    """
    The main function orchestrates the ETL process, model training, and evaluation.
    It calls functions from the ETL, modeling, and evaluation modules to process data,
    train models, and generate performance metrics and visualizations.
    """
    try:
        logging.info('Started the main function')

        # ETL Process
        hosp_df = extract()
        hosp_df_cleaned = transform(hosp_df)
        load(hosp_df_cleaned)

        # Modeling
        results = train_model(hosp_df_cleaned)

        # Evaluation and Visualization
        evaluate_and_visualize(results)

        logging.info('Finished the main function successfully')
    except Exception as e:
        logging.error(f'Unexpected error in main function: {e}')

if __name__ == '__main__':
    main()
