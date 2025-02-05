import matplotlib.pyplot as plt

def plot_results(y_true, y_pred, task_name):
    plt.figure(figsize=(10, 6))
    plt.plot(y_true, label="True")
    plt.plot(y_pred, label="Predicted", linestyle="--")
    plt.title(f"{task_name} - Prediction vs. Ground Truth")
    plt.legend()
    plt.show()
