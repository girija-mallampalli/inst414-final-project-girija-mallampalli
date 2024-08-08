# importing necessary libraries
import pandas as pd

# Dataset used on Medicare.gov for hospital quality comparison
hosp_df = pd.read_csv('Hospital_General_Ratings.csv', encoding = 'latin1')

# Define the new folder path
new_folder_path = 'data/extracted'

# Check if the folder exists, if not, create it
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Define the full file path including the filename
file_path = os.path.join(new_folder_path, 'Hospital_General_Ratings.csv')

# Export the DataFrame to the specified file
hosp_df.to_csv(file_path, index=False)
