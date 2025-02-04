import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Dropout

def run_regression(original_data, repaired_data):
    original_df = pd.read_csv(original_data)
    repaired_df = pd.read_csv(repaired_data)

    features = [col for col in repaired_df.columns if col != "target"]
    X_train, X_test, y_train, y_test = train_test_split(
        repaired_df[features].values, repaired_df["target"].values, test_size=0.2, random_state=42
    )

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train).reshape(X_train.shape[0], 1, X_train.shape[1])
    X_test = scaler.transform(X_test).reshape(X_test.shape[0], 1, X_test.shape[1])

    model = Sequential([
        GRU(64, input_shape=(1, len(features)), return_sequences=False),
        Dropout(0.2),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)

    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    y_pred = model.predict(X_test).flatten()
    rmse = np.sqrt(np.mean((y_pred - y_test)**2))

    print(f"Regression Results: RMSE: {rmse:.4f}, MAE: {mae:.4f}")
