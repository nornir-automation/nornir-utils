import os
from nornir.core.inventory import Host


def load_credentials(host: Host, username: str | None = None, password: str | None = None) -> None:
    """
    load_credentials is an transform_functions to add credentials to every host.
    Environment variables `NORNIR_USERNAME` and `NORNIR_PASSWORD` or arguments can be used.

    Args:

        username: Device username
        password: Device password
    """
    username = username if username is not None else os.getenv("NORNIR_USERNAME")
    if username is not None:
        host.username = username
    password = password if password is not None else os.getenv("NORNIR_PASSWORD")
    if password is not None:
        host.password = password
