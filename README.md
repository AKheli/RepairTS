# TSRepair

TSRepair is a comprehensive benchmark for evaluating anomaly repair techniques in time series datasets. It supports both upstream and downstream evaluation, enabling users to measure and compare the performance of various algorithms under different contamination scenarios. With TSRepair, users can inject anomalies, repair data, and analyze results using a diverse set of datasets, repair techniques, and metrics.

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
- The `-d` argument expects the dataset to be located in the `data/test/` folder.

___


## Upstream Evaluation

```bash
# General Execution Command
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


