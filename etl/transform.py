import data.extracted
import pandas as pd

# Cleaning the Data

# Selecting only columns necessary for analysis
hosp_df_cleaned = hosp_df[['State', 'Readmission national comparison', 'Patient experience national comparison', 'Effectiveness of care national comparison', 'Timeliness of care national comparison', 'Efficient use of medical imaging national comparison']]

# Replacing "Not Available" with null to drop the values
hosp_df_cleaned = hosp_df_cleaned.replace('Not Available', pd.NA)
hosp_df_cleaned = hosp_df_cleaned.dropna()

# returning cleaned dataframe
hosp_df_cleaned
