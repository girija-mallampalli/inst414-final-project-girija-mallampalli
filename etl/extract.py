# importing necessary libraries
import logging
import pandas as pd

# Setting up logging
logging.basicConfig(filename='data/logs/extract.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')

def extract():
    try:
        logging.info('Started data extraction')
        hosp_df = pd.read_csv('Hospital_General_Ratings.csv', encoding='latin1')
        logging.info('Data extraction completed successfully')

        # Save the extracted DataFrame
        os.makedirs('data/extracted', exist_ok=True)
        hosp_df.to_csv('data/extracted/hosp_df.csv', index=False)
        logging.info('Extracted data saved successfully')
        
        return hosp_df
    except Exception as e:
        logging.error(f'Error during data extraction: {e}')
        raise
