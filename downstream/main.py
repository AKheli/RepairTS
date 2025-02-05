import os
from data_loader import load_data
from models.classification_xgboost import run_xgboost_classification
from models.regression_rnn import run_rnn_regression
from models.forecasting_transformer import run_transformer_forecasting

if __name__ == "__main__":
    # Load original, contaminated, and repaired datasets
    original_data, contaminated_data, repaired_data = load_data()

    # Run downstream evaluations
    print("Running XGBoost Classification...")
    run_xgboost_classification(original_data, contaminated_data, repaired_data)

    print("Running RNN Regression...")
    run_rnn_regression(original_data, contaminated_data, repaired_data)

    print("Running Transformer Forecasting...")
    run_transformer_forecasting(original_data, contaminated_data, repaired_data)
