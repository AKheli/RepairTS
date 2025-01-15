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


## Upstream Evaluation

```bash
# General Execution Command
python3 repair.py -d dataset -a anomaly_type -scen scenario_type -alg algorithm
```

### Examples

```
# 1. Run a single algorithm (SCR) on a single dataset (physionet19) 
# with one scenario (a_size) and one type of anomaly (shift and outlier)
python3 repair.py -d physionet19 -scen a_size -a shift,outlier -alg scr


# 2. Two algorithms (screen, rpca) on two datasets (physionet_2012, elec) with one scenario (a_rate) and two anomalies (shift, outlier)
python3 repair.py -d physionet12 -scen a_rate -a shift,outlier -alg screen

# 3. Run the full benchmark (all algorithms, datasets, scenarios, and anomalies)
python3 repair.py -d all -scen all -a all -alg all
```

### Arguments

| dataset      | anomaly_type | scenario_type | algorithm | 
|--------------|--------------|---------------|-----------| 
| physionet_2012       | shift        | ts_len        | kfilter   |
| humidity     | distortion   | a_size        | screen    |
| elec         | outlier      | a_rate        | imr       |
| beijingair   | all          | ts_nbr        | screen    |
| electricity  |              | cts_nbr       | scr       |
| eth_h1       |              | a_factor      | all       |
| italyair     |              | all           |           |
| pems         |              |               |           |
| physionet_2012 |            |               |           |
| all          |              |               |           |

### Data

- The data must be in CSV format.
- The `-d` argument expects the dataset to be located in the `data` folder.

### Results

All results and plots will be saved in the `Results` folder. 
- Accuracy results for all algorithms will be stored by scenario, dataset, and anomaly type in: `Results/.../.../precision/error/`. 
- Runtime results for all algorithms will be saved in: `Results/.../.../runtime/`. 
- Plots showing anomalous parts of the time series and their repairs will be saved in: `Results/.../precision/repair/`.

### Examples

1. Run a single algorithm (screen) on a single dataset (`physionet_2012`) using one scenario (number of time series) and one anomaly (`shift`):
```bash
python3 repair.py -d physionet_2012 -scen ts_nbr -a shift -alg screen
```

2.	Run two algorithms (screen, rpca) on two datasets (physionet_2012, msd) using one scenario (a_rate) and two anomalies (shift, outlier):   shift,outlier)

```bash
python3 repair.py -d physionet_2012,msd -scen ts_nbr -a shift,outlier -alg screen,rpca
```


___


## Downstream Evaluation


