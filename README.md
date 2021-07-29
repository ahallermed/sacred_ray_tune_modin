# Sacred ray tune modin

## Installation

Install anaconda/miniconda.

```bash
conda env create -f environment.yml
conda activate srtm
```

## Issue Reproduction

### No error

```bash
python src/sacred_experiment.py
```

### Error

```bash
python src/hyper_param_tuning.py
```

The program freezes with this message:

```log
2021-07-29 16:03:46,714 INFO services.py:1245 -- View the Ray dashboard at http://127.0.0.1:8265
WARNING - hyper_ex - No observers have been added to this run
INFO - hyper_ex - Running command 'hyper_param_tuning'
INFO - hyper_ex - Started
== Status ==
Memory usage on this node: 9.9/16.0 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/4 CPUs, 0/0 GPUs, 0.0/4.74 GiB heap, 0.0/2.37 GiB objects
Result logdir: /Users/my_user/ray_results/wrapper_sacred_inner_experiment_2021-07-29_16-03-48
Number of trials: 1/1 (1 PENDING)
+---------------------------------------------+----------+-------+-------------+
| Trial name                                  | status   | loc   |   max_depth |
|---------------------------------------------+----------+-------+-------------|
| wrapper_sacred_inner_experiment_cb989_00000 | PENDING  |       |           1 |
+---------------------------------------------+----------+-------+-------------+



(pid=58859) WARNING - inner_experiment - No observers have been added to this run
(pid=58859) INFO - inner_experiment - Running command 'sacred_inner_experiment'
(pid=58859) INFO - inner_experiment - Started
(pid=58859) UserWarning: Distributing <class 'dict'> object. This may take some time.
2021-07-29 16:04:06,780 WARNING worker.py:1189 -- The actor or task with ID d6b29075fef5866577a82b46f6c61400b2d3276f023b15ea cannot be scheduled right now. It requires {CPU_group_d2206d3a3965ae07ecb2e0f43f55b6c7: 1.000000} for placement, but this node only has remaining {3.000000/4.000000 CPU, 4.742377 GiB/4.742377 GiB memory, 2.371188 GiB/2.371188 GiB object_store_memory, 1.000000/1.000000 node:192.168.178.27, 0.000000/1.000000 CPU_group_0_d2206d3a3965ae07ecb2e0f43f55b6c7, 0.000000/1.000000 CPU_group_d2206d3a3965ae07ecb2e0f43f55b6c7}
. In total there are 1 pending tasks and 0 pending actors on this node. This is likely due to all cluster resources being claimed by actors. To resolve the issue, consider creating fewer actors or increase the resources available to this Ray cluster. You can ignore this message if this Ray cluster is expected to auto-scale or if you specified a runtime_env for this task or actor because it takes time to install.
```
