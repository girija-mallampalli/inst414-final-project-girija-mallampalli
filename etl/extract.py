# importing necessary libraries
import os
import logging
import pandas as pd


# Setting up logging
logging.basicConfig(filename='data/logs/extract.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')

def extract():
    """
    Extracts the raw hospital ratings data from the CSV file in the 'data/' folder.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data.
    """
    try:
        logging.info('Started data extraction')
        # Path to the raw CSV file in the 'data/' folder
        file_path = 'data/Hospital General Ratings.csv'
        
        # Load the dataset
        hosp_df = pd.read_csv(file_path, encoding='latin1')
        
         # Ensure the 'data/extracted' directory exists
        os.makedirs('data/extracted', exist_ok=True)
        
        # Save the extracted data to the 'data/extracted/' folder
        extracted_file_path = 'data/extracted/hospital_general_ratings.csv'
        hosp_df.to_csv(extracted_file_path, index=False)
        
        logging.info(f'Data extraction completed successfully and saved to {extracted_file_path}')
        return hosp_df
    except Exception as e:
        logging.error(f'Error during data extraction: {e}')
        raise
