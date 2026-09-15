import json

from nornir.core.task import Result, Task


def load_json(task: Task, file: str) -> Result:
    """Load a json file.

    Arguments:
        task: Nornir task object, provided automatically when the task is run
        file: path to the json file to load

    Examples:
        Simple example::

            > nr.run(task=load_json,
                     file="mydata.json")

    Returns:
        Result object with the following attributes set:
          * result (``dict``): dictionary with the contents of the file

    """
    with open(file, "r") as f:
        data = json.loads(f.read())

    return Result(host=task.host, result=data)
