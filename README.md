# inst414-final-project-girija-mallampalli

## Project Title: Optimizing Patient Inflow and Outflow Using Hospital Ratings
Overview:
This project aims to optimize patient inflow and outflow in hospitals by analyzing hospital quality data. By understanding the factors that impact patient experience and care effectiveness, hospitals can enhance their operational efficiency, reduce patient wait times, and improve overall healthcare delivery. The project utilizes data science techniques, including data extraction, cleaning, transformation, categorical encoding, and random forest regression, to derive actionable insights from hospital quality metrics.


## Data Sources
The data used in this project is sourced from publicly available hospital quality datasets:
Link: 

## Code Package Structure
etl/:
* extract.py: Extract data from CSV files.
              Handle encoding issues and load data into pandas DataFrames.
  
* transform.py: Clean the data by selecting relevant columns and handling missing values.
                Encode categorical variables to prepare the data for analysis.
  
* load.py: Script for loading cleaned data into a new csv

analysis/:
* model.py: Use Random Forest Regressor to model the relationship between hospital quality metrics and patient experience.
            Train the model using a portion of the dataset and evaluate it on a test set.

* evaluation.py: Calculate performance metrics such as Mean Squared Error (MSE) and R-squared (R²) to assess the model's accuracy.
                 Compare the model's predictions with actual values to identify key areas for hospital improvement.

vis/:
* visualization.py: Generate visualizations, such as correlation matrices and feature importance plots, to better understand the data and model results.
Save visualizations as PNG files for reporting and analysis.

main.py: Main script to run the entire process (data cleaning, encoding, model training).
requirements.txt: List of required Python packages.

### Getting Started
Prerequisites
Python 3.x
Required Python libraries listed in requirements.txt.

### Installation
Clone the repository to your local machine.
Navigate to the project directory.

Install the required Python packages using:
pip install -r requirements.txt

#### Run the extraction, transformation, and loading processes:
python scripts/extract.py
python scripts/transform.py
python scripts/load.py

#### Train the model and evaluate its performance:
python scripts/model.py
python scripts/evaluate.py

#### Generate and save visualizations:
python scripts/visualizations.py

#### Results
The project outputs include:
Model Performance Metrics: Saved in data/outputs/metrics.csv.
Visualizations: Saved in data/visualizations/ as PNG files.
Logs: Detailed logs of each process are stored in data/logs/.

#### Conclusion
By analyzing hospital quality metrics, this project provides insights into key factors affecting patient inflow and outflow. The results can help hospitals optimize their operations, leading to improved patient experiences and better resource management.

License
This project is licensed under the MIT License - see the LICENSE file for details.

