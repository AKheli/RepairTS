# RepBench

RepBench is a tool for measuring and comparing the performance of algorithms repairing anomalies in datasets. It offers
various algorithms and metrics for evaluating the effectiveness of anomaly repair under different contamination
conditions. Users can introduce different types of anomalies into datasets and use the RepBench web application to view
the data, repair results, and experiment with algorithm parameters.

[**Prerequisites**](#prerequisites) | [**Build**](#build) | [**Repair**](#anomaly-repair) 


# Anomaly Repair

This benchmark implements four different anomaly repair techniques in time series and evaluates their precision and
runtime on various real-world time series datasets using different repair scenarios.

- The benchmark implements the following
  algorithms: [IMR](https://www.vldb.org/pvldb/vol10/p1046-song.pdf), [SCREEN](https://dl.acm.org/doi/pdf/10.1145/2723372.2723730),
  Robust PCA and CDrep.
- All the datasets used in this benchmark can be
  found [here](https://github.com/althausLuca/RepairBenchmark/tree/master/data).
- The full list of repair scenarios can be
  found [here](https://github.com/althausLuca/RepBench/blob/master/testing_frame_work/scenarios/README.md).

___

## Prerequisites

- Ubuntu 22 (including Ubuntu derivatives, e.g., Xubuntu).
- Clone this repository.

___

## Build

install python and pip

```bash
sudo apt install python3-dev
sudo apt install python3-pip
```

create a activate a virtual environment

```bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```

install the requirements for the Benchmark

```bash
pip3 install -r testing_frame_work/testing_framework_requierements.txt
```

Additionaly, to use the SRC algorithm you need Java to run on your system e.g., openjdk-17-jre.

___


## Execution

```bash
python3 repair.py -d dataset -a anomaly_type -scen scenario_type -alg algorithm
```

### Arguments

| dataset  | anonaly_type | scenario_type | algorithm | 
|----------|--------------|---------------|-----------| 
| bafu5k   | shift        | ts_len        | rpca      |
| humidity | distortion   | a_size        | screen    |
| msd1_5   | outlier      | a_rate        | imr       |
| elec     | all          | ts_nbr        | cdrep     |
| all      |              | cts_nbr       | kfilter   |
| all      |              | a_factor      | screen*   |
|          |              | all           | all       |


### Data

- The data has to have a csv format.
- The data argument expects the Data to be in the data folder.

### Results

All results and plots will be added to `Results` folder. The accuracy results of all algorithms will be sequentially
added for each scenario, dataset and anomaly type to: `Results/.../.../precision/error/`. The runtime results of all
algorithms will be added to: `Results/.../.../runtime/`. The plots of some anomaylous parts of the time series together
with its repair will be added to the folder `Results/.../precision/repair/`.

### Examples

1. Run a single algorithm (cdrec) on a single dataset (bafu5k) using one scenario (number of time series) and one
   anomaly (shift)

```bash
python3 repair.py -d bafu5k -scen ts_nbr  -a shift -alg cdrep
```

2. Run two algorithms (cdrec, rpca) on two dataset (bafu5k,msd) using one scenario (a_rate) and two anomalies (
   shift,outlier)

```bash
python3 repair.py  -d bafu5k,msd -scen ts_nbr -a shift,outlier -alg cdrep,rpca
```

3. Run the whole benchmark: all the algorithms , all the dataset on all scenarios with all anomalies (takes ~6 hours)

```bash
python3 repair.py -d all -scen all  -a all -alg all
```

