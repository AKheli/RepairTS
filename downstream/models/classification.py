import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
import xgboost as xgb

def run_classification(original_data, repaired_data):
    original_df = pd.read_csv(original_data)
    repaired_df = pd.read_csv(repaired_data)
    features = [col for col in original_df.columns if col != "target"]

    X_train, X_test, y_train, y_test = train_test_split(
        repaired_df[features], repaired_df["target"], test_size=0.2, random_state=42
    )

    # Hyperparameters tuned using grid search
    params = {
        "max_depth": 6,
        "learning_rate": 0.05,
        "n_estimators": 200,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "objective": "binary:logistic",
    }

    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Classification Results: F1-Score: {f1:.4f}, Accuracy: {accuracy:.4f}")
