# type: ignore
# flake8: noqa

import modin.pandas as pd
import ray
from sacred import Experiment

inner_experiment = Experiment("inner_experiment")
# add an observer here if you'd like to

if not ray.is_initialized():
    ray.init(num_cpus=4)


@inner_experiment.config
def config():
    max_depth = 999


@inner_experiment.main
def sacred_inner_experiment(_run, _seed, max_depth):
    # to actually use the max_depth config
    _run.log_scalar("samples", max_depth)

    X = pd.DataFrame({"a": [1, 2, 3, 4], "b": [4, 3, 2, 1]})

    # this line breaks everything
    Z = X + X


if __name__ == "__main__":
    inner_experiment.run_commandline()
