# RepairTS

RepairTS is a comprehensive benchmark for evaluating anomaly repair techniques in time series datasets. It supports both upstream and downstream evaluation, enabling users to measure and compare the performance of various algorithms under different contamination scenarios. With RepairTS, users can inject anomalies, repair data, and analyze results using a diverse set of datasets, repair techniques, and metrics.

---

## Prerequisites

- **Operating System**: Ubuntu 22 or compatible derivatives.
- **Python**: Python 3.9 and pip.
- **Java**: Required for the SCREEN algorithm (e.g., `openjdk-17-jre`).
---

## Build Instructions

1. Install Python and pip:
```bash
sudo apt install python3.9-dev
sudo apt install python3.9-venv
sudo apt install python3-pip
```

2. create a activate a virtual environment

```bash
python3.9 -m venv venv
source venv/bin/activate
```

3. install the requirements for the Benchmark

```bash
pip3 install --upgrade pip
pip3 install -r install_dependencies.txt
```

4. install Java for the SCREEN algorithm

```bash
sudo apt install openjdk-17-jre
```

___

## Dataset 

- Download and Decompress Datasets: 
  ```bash
  sudo sh install_datasets.sh
  ```

- The data must be in CSV format.
- The data will be located in the `data/test/` folder.

___


## Upstream Evaluation

```bash
python3 repair.py -d dataset -a anomaly_type -scen scenario_type -alg algorithm
```


### Arguments

| dataset      | anomaly_type | algorithm | 
|--------------|--------------|-----------| 
| italyair       | shift        | kfilter   |
| humidity     | distortion   | screen    |
| elec         | outlier      | imr       |
| beijingair   | all          | screen    |
| electricity  |              | scr       |
| eth_h1       |              | all       |
| physionet_2012     |              |           |
| physionet_2019     |              |           |
| pems         |              |           |
| all          |              |           |


### Results

All results and plots will be saved in the `Results` folder. 
- Accuracy results for all algorithms will be stored by scenario, dataset, and anomaly type in: `Results/.../.../precision/error/`. 
- Runtime results for all algorithms will be saved in: `Results/.../.../runtime/`. 
- Plots showing anomalous parts of the time series and their repairs will be saved in: `Results/.../precision/repair/`.

### Examples


```
# 1. Run a single algorithm (SCR) on a single dataset (physionet19) and one type of anomaly (shift and outlier)
python3 repair.py -d physionet19 -scen a_size -a shift,outlier -alg scr


# 2. Two algorithms (screen, rpca) on two datasets (physionet_2012, elec) and two anomalies (shift, outlier)
python3 repair.py -d physionet12 -scen a_rate -a shift,outlier -alg screen

# 3. Run the full benchmark (all algorithms, datasets, scenarios, and anomalies)
python3 repair.py -d all -scen all -a all -alg all
```

___


## Downstream Evaluation

The downstream evaluation assesses the effectiveness of repaired time series data on practical tasks, including classification, regression, and forecasting. This evaluation ensures that repairs not only restore data quality but also improve the performance of real-world applications. The implementation is available under the `downstream/` folder, containing code for loading datasets, training models, and reporting task-specific metrics.

---

### Tasks and Models

- **Classification**: Uses the XGBoost classifier, suitable for structured data and robust to noisy features.
- **Regression**: Utilizes GRU-based Recurrent Neural Networks (RNNs) to capture sequential dependencies in time series.
- **Forecasting**: Employs Transformer-based models for multi-step predictions by leveraging long-range dependencies.

---

### Running the Downstream Pipeline

The downstream evaluation script trains a model on original, contaminated, and repaired datasets, and compares performance.

**Command:**
```bash
cd downstream/
```

**Command:**
```bash
python3 downstream_evaluation.py --dataset dataset_name --task task_name --repaired_path path_to_repaired_data
```

**Arguments:**

| Argument         | Description                                         |
|------------------|-----------------------------------------------------|
| `--dataset`      | The dataset to evaluate (e.g., `elec`, `humidity`).  |
| `--task`         | The downstream task (`classification`, `regression`, or `forecasting`). |
| `--repaired_path`| Path to the repaired dataset.                       |

---

### Example Usage

**Classification Task:**  
```bash
python3 downstream_evaluation.py --dataset electricity --task classification --repaired_path data/repaired/electricity.csv
```

**Regression Task:**  
```bash
python3 downstream_evaluation.py --dataset humidity --task regression --repaired_path data/repaired/humidity.csv
```

**Forecasting Task:**  
```bash
python3 downstream_evaluation.py --dataset eth_h1 --task forecasting --repaired_path data/repaired/eth_h1.csv
```

---

### Model-Specific Details and Hyperparameter Tuning

1. **XGBoost for Classification**
   - **Model Description**: XGBoost is a gradient-boosting algorithm known for its efficiency in handling noisy and structured data. It builds an ensemble of decision trees iteratively.
   - **Metrics**: F1-score is used to evaluate the model’s classification performance.
   - **Tuned Hyperparameters**:
     - `max_depth`: Controls the maximum depth of the trees.
     - `learning_rate`: Learning rate to prevent overfitting.
     - `n_estimators`: Number of trees in the ensemble.
     - `gamma`: Minimum loss reduction required to make a split.
   - **Optimization Method**: Grid search is used to select the best hyperparameters by maximizing the F1-score.

2. **GRU-based RNN for Regression**
   - **Model Description**: GRU-based RNNs are well-suited for capturing sequential patterns and dependencies in time series data while avoiding vanishing gradient issues.
   - **Metrics**: Root Mean Squared Error (RMSE) is used to measure prediction accuracy.
   - **Tuned Hyperparameters**:
     - `hidden_units`: Number of GRU units in each layer.
     - `dropout_rate`: Dropout rate to prevent overfitting.
     - `batch_size`: Number of samples per training batch.
     - `learning_rate`: Learning rate for the optimizer.
   - **Optimization Method**: Hyperparameters are tuned using grid search with validation sets to minimize RMSE.

3. **Transformer for Forecasting**
   - **Model Description**: Transformers leverage self-attention mechanisms to model both local and global dependencies, making them suitable for long-range predictions in time series.
   - **Metrics**: Accuracy is used to assess forecasting performance over prediction windows.
   - **Tuned Hyperparameters**:
     - `num_layers`: Number of encoder/decoder layers.
     - `attention_heads`: Number of attention heads per layer.
     - `dropout_rate`: Dropout rate for regularization.
     - `learning_rate`: Learning rate for the optimizer.
   - **Optimization Method**: Hyperparameters are tuned using a combination of grid search and validation sets to optimize forecasting accuracy.

---

### Output Metrics

The downstream evaluation reports the following task-specific metrics:

| Task            | Metric             | Description                                   |
|-----------------|--------------------|-----------------------------------------------|
| Classification  | F1-score           | Evaluates precision and recall balance.      |
| Regression      | RMSE               | Measures the deviation between predicted and actual values. |
| Forecasting     | Accuracy           | Measures the percentage of correct predictions over the forecast window. |

The final performance metrics are saved in the `Results/downstream/` directory, organized by dataset and task.


