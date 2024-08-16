import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder
from data import extracted

# Setting up logging
logging.basicConfig(filename='data/logs/transform.log', level=logging.DEBUG, 
                    format='%(asctime)s %(message)s')

def transform():
    try:
        logging.info('Started data transformation')
        hosp_df = pd.read_csv('data/extracted/hosp_df.csv')
        hosp_df_cleaned = hosp_df[['State', 'Readmission national comparison', 
                                   'Patient experience national comparison', 
                                   'Effectiveness of care national comparison', 
                                   'Timeliness of care national comparison', 
                                   'Efficient use of medical imaging national comparison']]
        hosp_df_cleaned = hosp_df_cleaned.replace('Not Available', pd.NA)
        hosp_df_cleaned = hosp_df_cleaned.dropna()

        # Encode categorical variables
        label_encoder = LabelEncoder()
        columns_to_encode = ['Effectiveness of care national comparison', 
                             'Readmission national comparison', 
                             'Timeliness of care national comparison', 
                             'Efficient use of medical imaging national comparison', 
                             'Patient experience national comparison']
        for column in columns_to_encode:
            hosp_df_cleaned[column] = label_encoder.fit_transform(hosp_df_cleaned[column].astype(str))
        
        logging.info('Data transformation completed successfully')

        # Save the transformed DataFrame
        os.makedirs('data/transformed', exist_ok=True)
        hosp_df_cleaned.to_csv('data/transformed/hosp_df_cleaned.csv', index=False)
        logging.info('Transformed data saved successfully')
        
        return hosp_df_cleaned
    except Exception as e:
        logging.error(f'Error during data transformation: {e}')
        raise
