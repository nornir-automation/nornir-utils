"""Tests for the echo_data task."""

from nornir.core import Nornir

from nornir_utils.plugins.tasks.data import echo_data


def test_echo_data(nr: Nornir) -> None:
    """Echo back the kwargs passed to the task."""
    result = nr.run(echo_data, my_var="asd", other="value")

    assert len(result) > 0
    for r in result.values():
        assert r.result == {"my_var": "asd", "other": "value"}
