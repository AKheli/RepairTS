import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from utils.metrics import calculate_f1

def run_xgboost_classification(original_data, contaminated_data, repaired_data):
    X = original_data.drop('target', axis=1)
    y = original_data['target']
    
    # Split datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Hyperparameter tuning grid
    param_grid = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5, 7]
    }

    # Train model and evaluate
    model = XGBClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Evaluate and print F1-score
    f1 = calculate_f1(y_test, y_pred)
    print(f"XGBoost Classification F1-score: {f1}")
    pd.DataFrame({"f1_score": [f1]}).to_csv("results/classification_results.csv", index=False)
