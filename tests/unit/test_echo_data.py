"""Tests for the echo_data task."""

from nornir.core import Nornir

from nornir_utils.plugins.tasks.data import echo_data


class Test:
    """Tests for the echo_data task."""

    def test_echo_data(self, nr: Nornir) -> None:
        """Echo back the kwargs passed to the task."""
        result = nr.run(echo_data, my_var="asd", other="value")

        assert result
        for r in result.values():
            assert r.result == {"my_var": "asd", "other": "value"}
