import pandas as pd
import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import MinMaxScaler

class TransformerModel(nn.Module):
    def __init__(self, input_dim, hidden_dim=128, nhead=4, num_layers=3):
        super(TransformerModel, self).__init__()
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=nhead)
        self.transformer = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, src):
        out = self.transformer(src)
        return self.fc(out.mean(dim=0))

def run_forecasting(original_data, repaired_data):
    original_df = pd.read_csv(original_data)
    repaired_df = pd.read_csv(repaired_data)

    sequence_length = 10
    data = repaired_df['value'].values
    X, y = [], []

    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length])
        y.append(data[i + sequence_length])

    X, y = np.array(X), np.array(y)
    train_size = int(0.8 * len(X))
    X_train, X_test, y_train, y_test = X[:train_size], X[train_size:], y[:train_size], y[train_size:]

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(1)
    X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(1)
    y_train = torch.tensor(y_train, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32)

    model = TransformerModel(input_dim=sequence_length)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    epochs = 100
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(X_train)
        loss = criterion(output.flatten(), y_train)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        y_pred = model(X_test).flatten()
        accuracy = (torch.sum((y_pred - y_test) ** 2) / len(y_test)).sqrt().item()

    print(f"Forecasting Results: Accuracy: {accuracy:.4f}")
