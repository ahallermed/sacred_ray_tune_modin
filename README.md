# Sacred ray tune modin

There is a wrapping sacred experiment, that includes the tuning. This tuning executes a separate single sacred experiment several times with different config parameters.

This example is as simple as possible to demonstrate usage and functionality.

**INFO** No transformation of dicts, lists, etc. needed anymore from sacred to tune. If you encounter any issues, use config = dict(config) for ray configurations.

## Installation

Install anaconda/miniconda.

```bash
conda env create -f environment.yml
conda activate srtm
```

## Usage

Single sacred experiment:

```bash
python src/sacred_experiment.py
```

sacred, ray tune and modin:

```bash
python src/hyper_param_tuning.py
```

ray tune and modin but no sacred:

```bash
python src/no_sacred_hyper_param_tuning.py
```

## Issues if not taken into account

If not adding resources per trail to tune.run as parameter:

```python
        resources_per_trial=tune.PlacementGroupFactory([{
            "CPU": 1,
            "GPU": 0
        }, {
            "CPU": 1
        }],
```

Hereby, the first CPU entry is for the training wrapper itself and the second entry with CPU is the one is for the additional workers (see [ray  docu on PlacementGroupFactory](https://docs.ray.io/en/master/tune/api_docs/internals.html#ray.tune.utils.placement_groups.PlacementGroupFactory)).  
**NOTE: Both "CPU"-keys need to be in capital letters, it won't work with small letters.**

Otherwise you would get for both minimal programs such an error and the program freezes with this message:

```log
2021-07-29 16:18:25,092 INFO services.py:1245 -- View the Ray dashboard at http://127.0.0.1:8265
2021-07-29 16:18:26,174 WARNING function_runner.py:544 -- Function checkpointing is disabled. This may result in unexpected behavior when using checkpointing features or certain schedulers. To enable, set the train function arguments to be `func(config, checkpoint_dir=None)`.
== Status ==
Memory usage on this node: 10.0/16.0 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/4 CPUs, 0/0 GPUs, 0.0/4.58 GiB heap, 0.0/2.29 GiB objects
Result logdir: /Users/my_user/ray_results/inner_experiment_2021-07-29_16-18-26
Number of trials: 1/1 (1 PENDING)
+------------------------------+----------+-------+-------------+
| Trial name                   | status   | loc   |   max_depth |
|------------------------------+----------+-------+-------------|
| inner_experiment_d6e11_00000 | PENDING  |       |           1 |
+------------------------------+----------+-------+-------------+


(pid=59545) {'max_depth': 1}
(pid=59545) UserWarning: Distributing <class 'dict'> object. This may take some time.
2021-07-29 16:18:45,176 WARNING worker.py:1189 -- The actor or task with ID 812e469ffd1e2cd19dd93ea3c2031e301de8d37a2f05c200 cannot be scheduled right now. It requires {CPU_group_66872d0e95ae651141be809e6099336d: 1.000000} for placement, but this node only has remaining {3.000000/4.000000 CPU, 4.582132 GiB/4.582132 GiB memory, 2.291066 GiB/2.291066 GiB object_store_memory, 0.000000/1.000000 CPU_group_0_66872d0e95ae651141be809e6099336d, 1.000000/1.000000 node:192.168.178.27, 0.000000/1.000000 CPU_group_66872d0e95ae651141be809e6099336d}
. In total there are 1 pending tasks and 0 pending actors on this node. This is likely due to all cluster resources being claimed by actors. To resolve the issue, consider creating fewer actors or increase the resources available to this Ray cluster. You can ignore this message if this Ray cluster is expected to auto-scale or if you specified a runtime_env for this task or actor because it takes time to install.
```

this is valid for:

Operating Systems:  
Linux 64bit  
Mac 64bit  

Different package versions:  
modin: [0.10.1, 0.10.0, 0.9.1]  
ray: [1.3.0, 1.4.0, 1.5.0] and nightly 2.0.0.dev0 from 2021/07/29 for MacOS.  
