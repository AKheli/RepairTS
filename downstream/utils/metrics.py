from sklearn.metrics import f1_score, mean_squared_error, accuracy_score

def calculate_f1(y_true, y_pred):
    return f1_score(y_true, y_pred, average='weighted')

def calculate_rmse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred, squared=False)

def calculate_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)
