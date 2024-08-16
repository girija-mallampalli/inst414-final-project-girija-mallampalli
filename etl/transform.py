import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder
from etl import extract


def transform(hosp_df):
    try:
        logging.info('Started data transformation')
        hosp_df_cleaned = hosp_df[['State', 'Readmission national comparison', 'Patient experience national comparison', 
                                   'Effectiveness of care national comparison', 'Timeliness of care national comparison', 
                                   'Efficient use of medical imaging national comparison']]
        hosp_df_cleaned = hosp_df_cleaned.replace('Not Available', pd.NA)
        hosp_df_cleaned = hosp_df_cleaned.dropna()

        # Encode categorical variables
        label_encoder = LabelEncoder()
        columns_to_encode = ['Effectiveness of care national comparison', 'Readmission national comparison', 
                             'Timeliness of care national comparison', 'Efficient use of medical imaging national comparison', 
                             'Patient experience national comparison']
        for column in columns_to_encode:
            hosp_df_cleaned[column] = label_encoder.fit_transform(hosp_df_cleaned[column].astype(str))

        logging.info('Data transformation completed successfully')
        return hosp_df_cleaned
    except Exception as e:
        logging.error(f'Error during data transformation: {e}')
        raise
