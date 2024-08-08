import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import analysis.model

#Linear Regression Model Evaluation:
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print(f'Linear Regression MSE: {mse_lr}, R2: {r2_lr}')

# Random Forest Regressor Model Evaluation:
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f'Random Forest MSE: {mse_rf}, R2: {r2_rf}')


# Ensure the directory exists
os.makedirs('data/outputs', exist_ok=True)

# Save metrics to CSV
metrics_df = pd.DataFrame({
    'Model': ['Linear Regression', 'Random Forest'],
    'MSE': [mse_linear, mse_rf],
    'R2': [r2_linear, r2_rf]
})
metrics_df.to_csv('data/outputs/metrics.csv', index=False)

# Plotting and saving charts
plt.figure(figsize=(10, 5))

# Plot for MSE
plt.subplot(1, 2, 1)
plt.bar(metrics_df['Model'], metrics_df['MSE'])
plt.title('Mean Squared Error')
plt.xlabel('Model')
plt.ylabel('MSE')

# Plot for R2
plt.subplot(1, 2, 2)
plt.bar(metrics_df['Model'], metrics_df['R2'])
plt.title('R-squared')
plt.xlabel('Model')
plt.ylabel('R2')

# Save the plot
plt.tight_layout()
plt.savefig('data/outputs/model_performance.png')
plt.show()
