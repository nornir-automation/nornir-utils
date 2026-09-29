from typing import Any

from nornir.core.task import Result, Task


def echo_data(task: Task, **kwargs: Any) -> Result:
    """Echo back the data passed to the task.

    This dummy task is useful in grouped tasks to debug the data passed to tasks.

    Arguments:
        task: Nornir task object, provided automatically when the task is run
        **kwargs: Any <key,value> pair you want

    Returns:
        Result object with the following attributes set:
          * result (``dict``): ``**kwargs`` passed to the task

    """
    return Result(host=task.host, result=kwargs)
