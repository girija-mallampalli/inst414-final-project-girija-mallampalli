import seaborn as sns
import matplotlib.pyplot as plt
import data.outputs

# Correlation matrix
correlation_matrix = hosp_df_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Pairplot to visualize relationships
sns.pairplot(hosp_df_cleaned, vars=[
    'Effectiveness of care national comparison', 
    'Readmission national comparison', 
    'Timeliness of care national comparison', 
    'Efficient use of medical imaging national comparison', 
    'Patient experience national comparison'
])
plt.show()


# Coefficients from Linear Regression
coefficients = pd.DataFrame(lr_model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)

# Feature importance from Random Forest
feature_importance = pd.DataFrame(rf_model.feature_importances_, X.columns, columns=['Importance'])
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print(feature_importance)

# Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=feature_importance.index, y=feature_importance['Importance'])
plt.title('Feature Importance from Random Forest')
plt.show()
