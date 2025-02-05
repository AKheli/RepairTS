import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from utils.metrics import calculate_accuracy

class TransformerModel(nn.Module):
    def __init__(self, input_dim, num_heads, num_layers, output_dim):
        super(TransformerModel, self).__init__()
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=input_dim, nhead=num_heads)
        self.transformer = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        x = self.transformer(x)
        return self.fc(x)

def run_transformer_forecasting(original_data, contaminated_data, repaired_data):
    X = torch.tensor(original_data.drop('target', axis=1).values, dtype=torch.float32)
    y = torch.tensor(original_data['target'].values, dtype=torch.float32)

    # DataLoader for batching
    dataset = TensorDataset(X, y)
    data_loader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Define and train the model
    model = TransformerModel(input_dim=X.shape[1], num_heads=4, num_layers=2, output_dim=1)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    for epoch in range(50):
        for X_batch, y_batch in data_loader:
            optimizer.zero_grad()
            y_pred = model(X_batch)
            loss = criterion(y_pred.squeeze(), y_batch)
            loss.backward()
            optimizer.step()

    # Predict and evaluate
    y_pred = model(X).detach().numpy()
    accuracy = calculate_accuracy(y, y_pred.round())
    print(f"Transformer Forecasting Accuracy: {accuracy}")
    pd.DataFrame({"accuracy": [accuracy]}).to_csv("results/forecasting_results.csv", index=False)
