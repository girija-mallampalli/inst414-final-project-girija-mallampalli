import pandas as pd
import data.extracted
import etl.transform

# Load cleaned data into a new CSV
hosp_df_cleaned.to_csv('Hospital_General_Ratings_Cleaned.csv', index=False)

