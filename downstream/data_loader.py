import pandas as pd

def load_data():
    # Load CSV datasets
    original_data = pd.read_csv("path/to/original_dataset.csv")
    contaminated_data = pd.read_csv("path/to/contaminated_dataset.csv")
    repaired_data = pd.read_csv("path/to/repaired_dataset.csv")

    return original_data, contaminated_data, repaired_data
