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
