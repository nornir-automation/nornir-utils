import os

from nornir.core.inventory import Host


def load_credentials(host: Host, username: str | None = None, password: str | None = None) -> None:
    """Add credentials to a host.

    Meant to be used as a transform function, in which case Nornir calls it once for
    every host in the inventory. The credentials are taken from the `username` and
    `password` arguments, falling back to the `NORNIR_USERNAME` and `NORNIR_PASSWORD`
    environment variables when those arguments aren't given.

    Args:
        host: Host to add the credentials to
        username: Device username
        password: Device password

    """
    username = username if username is not None else os.getenv("NORNIR_USERNAME")
    if username is not None:
        host.username = username
    password = password if password is not None else os.getenv("NORNIR_PASSWORD")
    if password is not None:
        host.password = password
