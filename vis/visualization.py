import os
import pandas as pd
import seaborn as sns
import logging
import matplotlib.pyplot as plt
from data import outputs

def visualize():
    try:
        logging.info('Started visualizations')

        # Load the cleaned data
        hosp_df_cleaned = pd.read_csv('data/loaded/hosp_df_cleaned.csv')

        # Ensure the visualization directory exists
        output_folder = 'data/visualizations'
        os.makedirs(output_folder, exist_ok=True)

        # Correlation matrix
        correlation_matrix = hosp_df_cleaned.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.savefig(os.path.join(output_folder, 'correlation_matrix.png'))
        plt.close()

        # Feature importance from Random Forest
        feature_importance = pd.read_csv('data/outputs/feature_importance.csv')
        plt.figure(figsize=(10, 5))
        sns.barplot(x=feature_importance.index, y=feature_importance['Importance'])
        plt.title('Feature Importance from Random Forest')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, 'feature_importance.png'))
        plt.close()

        # Bar plot of Hospital Ownership
        plt.figure(figsize=(10, 6))
        sns.countplot(data=hosp_df_cleaned, x='Hospital Ownership', palette='viridis')
        plt.title('Count of Hospitals by Ownership Type')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, 'hospital_ownership.png'))
        plt.close()

        # Distribution of Hospital Ratings
        plt.figure(figsize=(10, 6))
        sns.histplot(hosp_df_cleaned['Hospital overall rating'], bins=10, kde=True, color='skyblue')
        plt.title('Distribution of Hospital Overall Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, 'hospital_ratings_distribution.png'))
        plt.close()

        # Scatter plot of Timeliness vs. Patient Experience
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=hosp_df_cleaned, x='Timeliness of care national comparison', y='Patient experience national comparison', hue='Hospital Ownership', palette='deep')
        plt.title('Timeliness of Care vs. Patient Experience by Ownership Type')
        plt.xlabel('Timeliness of Care (Comparison)')
        plt.ylabel('Patient Experience (Comparison)')
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, 'timeliness_vs_patient_experience.png'))
        plt.close()

        logging.info('Visualizations completed successfully')
    except Exception as e:
        logging.error(f'Error during visualizations: {e}')
        raise
    try:
        logging.info('Started visualizations')
        hosp_df_cleaned = pd.read_csv('data/loaded/hosp_df_cleaned.csv')

        # Correlation matrix
        correlation_matrix = hosp_df_cleaned.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.savefig('data/visualizations/correlation_matrix.png')
        plt.close()

        # Feature importance from Random Forest
        feature_importance = pd.read_csv('data/outputs/rf_predictions.csv')
        plt.figure(figsize=(10, 5))
        sns.barplot(x=feature_importance.columns, y=feature_importance['Importance'])
        plt.title('Feature Importance from Random Forest')
        plt.savefig('data/visualizations/feature_importance.png')
        plt.close()

        # Bar plot of Hospital Ownership
        plt.figure(figsize=(10, 6))
        sns.countplot(data=hosp_df, x='Hospital Ownership', palette='viridis')
        plt.title('Count of Hospitals by Ownership Type')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('data/visualizations/hospital_ownership.png')
        plt.close()

        #Save the plot as a PNG file
        ownership_plot_path = os.path.join(output_folder, 'hospital_ownership.png')
        plt.savefig(ownership_plot_path)
        plt.close()  # Close the figure to avoid overlap with subsequent plots

        # Distribution of Hospital Ratings
        plt.figure(figsize=(10, 6))
        sns.histplot(hosp_df['Hospital overall rating'], bins=10, kde=True, color='skyblue')
        plt.title('Distribution of Hospital Overall Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.tight_layout()

        # Save the plot as a PNG file
        ratings_plot_path = os.path.join(output_folder, 'hospital_ratings_distribution.png')
        plt.savefig(ratings_plot_path)
        plt.close()

        # Scatter plot of Timeliness vs. Patient Experience
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=hosp_df, x='Timeliness of care national comparison', y='Patient experience national comparison', hue='Hospital Ownership', palette='deep')
        plt.title('Timeliness of Care vs. Patient Experience by Ownership Type')
        plt.xlabel('Timeliness of Care (Comparison)')
        plt.ylabel('Patient Experience (Comparison)')
        plt.tight_layout()

        # Save the plot as a PNG file
        scatter_plot_path = os.path.join(output_folder, 'timeliness_vs_patient_experience.png')
        plt.savefig(scatter_plot_path)
        plt.close()
    
        logging.info('Visualizations completed successfully')
    except Exception as e:
        logging.error(f'Error during visualizations: {e}')
        raise



print(f'Plots saved in {output_folder}')
