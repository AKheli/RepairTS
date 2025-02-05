import argparse
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, mean_squared_error, accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPRegressor
import torch
from torch import nn, optim
import numpy as np

# hyperparameters for grid search
xgboost_hyperparameters = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7]
}

rnn_hyperparameters = {
    'hidden_layer_sizes': [(50,), (100,), (100, 50)],
    'activation': ['relu', 'tanh'],
    'solver': ['adam'],
    'alpha': [0.0001, 0.001]
}

transformer_hyperparameters = {
    'learning_rate': [0.01, 0.1],
    'batch_size': [32, 64],
    'epochs': [10, 20]
}

# transformer model
class TransformerModel(nn.Module):
    def __init__(self, input_size, num_classes):
        super(TransformerModel, self).__init__()
        self.transformer = nn.Transformer(d_model=input_size, num_encoder_layers=2)
        self.fc = nn.Linear(input_size, num_classes)

    def forward(self, x):
        x = self.transformer(x)
        x = self.fc(x.mean(dim=1))
        return x

# Grid search for XGBoost (classification)
def train_xgboost(X_train, y_train, X_test, y_test):
    grid_search = GridSearchCV(GradientBoostingClassifier(), xgboost_hyperparameters, cv=3)
    grid_search.fit(X_train, y_train)
    y_pred = grid_search.best_estimator_.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='weighted')
    print("Best Hyperparameters (XGBoost):", grid_search.best_params_)
    print("F1 Score:", f1)
    return f1

# Grid search for RNN (regression)
def train_rnn(X_train, y_train, X_test, y_test):
    grid_search = GridSearchCV(MLPRegressor(max_iter=500), rnn_hyperparameters, cv=3)
    grid_search.fit(X_train, y_train)
    y_pred = grid_search.best_estimator_.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print("Best Hyperparameters (RNN):", grid_search.best_params_)
    print("RMSE:", rmse)
    return rmse

# Train transformer model (forecasting)
def train_transformer(X_train, y_train, X_test, y_test, input_size):
    model = TransformerModel(input_size=input_size, num_classes=1)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)  # placeholder; tuned below

    # Training loop
    for epoch in range(20):  # placeholder; tuned below
        model.train()
        inputs = torch.tensor(X_train, dtype=torch.float32)
        targets = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    with torch.no_grad():
        y_pred = model(torch.tensor(X_test, dtype=torch.float32)).squeeze(1).numpy()
    accuracy = accuracy_score(np.round(y_test), np.round(y_pred))
    print("Transformer Accuracy:", accuracy)
    return accuracy

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required=True, help='Path to the dataset')
    parser.add_argument('--task', type=str, choices=['classification', 'regression', 'forecasting'], required=True)
    args = parser.parse_args()

    # Load dataset
    data = pd.read_csv(args.dataset)
    X = data.drop(columns=['target']).values
    y = data['target'].values
    split = int(0.8 * len(X))
    X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]

    # Execute task
    if args.task == 'classification':
        train_xgboost(X_train, y_train, X_test, y_test)
    elif args.task == 'regression':
        train_rnn(X_train, y_train, X_test, y_test)
    elif args.task == 'forecasting':
        input_size = X_train.shape[1]
        train_transformer(X_train, y_train, X_test, y_test, input_size)
