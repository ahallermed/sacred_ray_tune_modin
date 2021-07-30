# type: ignore
# flake8: noqa

import modin.pandas as pd
import ray
from ray import tune

if not ray.is_initialized():
    ray.init(num_cpus=4)


def inner_experiment(max_depth):
    # to actually use the max_depth config
    print(max_depth)

    X = pd.DataFrame({"a": [1, 2, 3, 4], "b": [4, 3, 2, 1]})

    # this line breaks everything
    Z = X + X


def hyper_param_tuning():
    hyper_params = {"max_depth": tune.grid_search([1])}

    tune.run(inner_experiment,
             config=hyper_params,
             resources_per_trial=tune.PlacementGroupFactory([
                 {
                     "CPU": 1,
                     "GPU": 0
                 },
             ], ))


if __name__ == "__main__":
    hyper_param_tuning()
