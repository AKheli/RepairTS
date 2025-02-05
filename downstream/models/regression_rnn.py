import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from sklearn.model_selection import train_test_split
from utils.metrics import calculate_rmse

def run_rnn_regression(original_data, contaminated_data, repaired_data):
    X = original_data.drop('target', axis=1).values
    y = original_data['target'].values

    # Split datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build RNN model
    model = Sequential([
        GRU(64, activation='relu', input_shape=(X_train.shape[1], 1)),
        Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    rmse = calculate_rmse(y_test, y_pred)
    print(f"RNN Regression RMSE: {rmse}")
    pd.DataFrame({"rmse": [rmse]}).to_csv("results/regression_results.csv", index=False)
