from sklearn.metrics import mean_squared_error, r2_score
import data.model

#Linear Regression Model Evaluation:
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print(f'Linear Regression MSE: {mse_lr}, R2: {r2_lr}')
