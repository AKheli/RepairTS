import os
from models.classification import run_classification
from models.regression import run_regression
from models.forecasting import run_forecasting

DATA_PATH = "./datasets"

def main():
    run_classification(
        original_data=os.path.join(DATA_PATH, "original/classification.csv"),
        repaired_data=os.path.join(DATA_PATH, "repaired/classification.csv"),
    )
    run_regression(
        original_data=os.path.join(DATA_PATH, "original/regression.csv"),
        repaired_data=os.path.join(DATA_PATH, "repaired/regression.csv"),
    )
    run_forecasting(
        original_data=os.path.join(DATA_PATH, "original/forecasting.csv"),
        repaired_data=os.path.join(DATA_PATH, "repaired/forecasting.csv"),
    )

if __name__ == "__main__":
    main()
