# type: ignore
# flake8: noqa

import os
import sys

import ray
from ray import tune
from sacred import Experiment

# add project path to sys.path for easy import
file_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(file_dir, ".."))
sys.path.append(root_dir)

if not ray.is_initialized():
    ray.init(num_cpus=4)


def wrapper_sacred_inner_experiment(config, reporter):
    # need to append path here again cause ray tune won't find it otherwise (No module named src)
    sys.path.append(root_dir)

    # import needs to be here because sacred projects aren't pickle-able but tune needs to be pickable
    from src.sacred_experiment import inner_experiment

    inner_experiment.run(config_updates=config)


hyper_ex: Experiment = Experiment("hyper_ex")
# add an observer here if you'd like to


@hyper_ex.main
def hyper_param_tuning():
    hyper_params = {"max_depth": tune.grid_search([1])}

    tune.run(wrapper_sacred_inner_experiment,
             config=hyper_params,
             resources_per_trial=tune.PlacementGroupFactory([{
                 "CPU": 1,
                 "GPU": 0
             }, {
                 "CPU": 1
             }]))


if __name__ == "__main__":
    hyper_ex.run_commandline()
