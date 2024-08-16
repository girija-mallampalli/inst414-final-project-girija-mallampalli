import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import analysis.model
import analysis.evaluation

# Define the folder to save the plots
output_folder = 'output/visualizations'

# Check if the folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Correlation matrix
correlation_matrix = hosp_df_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
correlation_matrix_path = os.path.join(output_folder, 'correlation_matrix.png')
plt.savefig(correlation_matrix_path)
plt.close()

# Pairplot to visualize relationships
sns.pairplot(hosp_df_cleaned, vars=[
    'Effectiveness of care national comparison', 
    'Readmission national comparison', 
    'Timeliness of care national comparison', 
    'Efficient use of medical imaging national comparison', 
    'Patient experience national comparison'
])
pairplot_path = os.path.join(output_folder, 'pairplot.png')
plt.savefig(pairplot_path)
plt.close()

# Feature importance from Random Forest
feature_importance = pd.DataFrame(rf_model.feature_importances_, X.columns, columns=['Importance'])
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print(feature_importance)

# Feature Importance Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=feature_importance.index, y=feature_importance['Importance'])
plt.title('Feature Importance from Random Forest')
feature_importance_path = os.path.join(output_folder, 'feature_importance.png')
plt.savefig(feature_importance_path)
plt.close()

# Bar plot of Hospital Ownership
plt.figure(figsize=(10, 6))
sns.countplot(data=hosp_df, x='Hospital Ownership', palette='viridis')
plt.title('Count of Hospitals by Ownership Type')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a PNG file
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

print(f'Plots saved in {output_folder}')
