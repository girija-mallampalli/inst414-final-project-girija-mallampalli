# importing necessary libraries
import logging
import pandas as pd

def extract():
    try:
        logging.info('Started data extraction')
        hosp_df = pd.read_csv('Hospital_General_Ratings.csv', encoding='latin1')
        logging.info('Data extraction completed successfully')
        return hosp_df
    except Exception as e:
        logging.error(f'Error during data extraction: {e}')
        raise
