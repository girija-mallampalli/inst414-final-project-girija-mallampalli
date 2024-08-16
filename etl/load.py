import os
import logging
import pandas as pd
from etl import extract, transform

def load(hosp_df_cleaned):
    try:
        logging.info('Started data loading')
        os.makedirs('data/cleaned', exist_ok=True)
        hosp_df_cleaned.to_csv('data/hosp_df_cleaned.csv', index=False)
        logging.info('Data loading completed successfully')
    except Exception as e:
        logging.error(f'Error during data loading: {e}')
        raise
