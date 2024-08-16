import os
import logging
import pandas as pd
from data import transformed

# Setting up logging for load.py
logging.basicConfig(
    filename='data/logs/load.log',  # Log file specific to the load.py script
    level=logging.DEBUG,            # Log level set to DEBUG to capture all messages
    format='%(asctime)s %(levelname)s %(message)s'  # Log format with timestamp, level, and message
)

def load_data(hosp_df_cleaned):
    try:
        logging.info('Started data loading')
        os.makedirs('data/loaded', exist_ok=True)
        hosp_df_cleaned.to_csv('data/loaded/hosp_df_cleaned.csv', index=False)
        logging.info('Data loading completed successfully')
    except Exception as e:
        logging.error(f'Error during data loading: {e}')
        raise
