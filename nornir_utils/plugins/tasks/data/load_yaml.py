import ruamel.yaml
from nornir.core.task import Result, Task


def load_yaml(task: Task, file: str) -> Result:
    """Load a yaml file.

    Arguments:
        task: Nornir task object, provided automatically when the task is run
        file: path to the yaml file to load

    Examples:
        Simple example::

            > nr.run(task=load_yaml,
                     file="mydata.yaml")

    Returns:
        Result object with the following attributes set:
          * result (``dict``): dictionary with the contents of the file

    """
    with open(file, "r") as f:
        yml = ruamel.yaml.YAML(typ="safe")
        data = yml.load(f)

    return Result(host=task.host, result=data)
