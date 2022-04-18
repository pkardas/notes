from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from packaging.version import parse

from src import (
    Card,
    CardsDB,
    api,
)


@pytest.mark.skip(reason="card doesn't support comparison yet")
def test_less_than_skip():
    assert Card("a task") < Card("b task")


@pytest.mark.skipif(
    parse(api.__version__).major < 2,
    reason="Card comparison not supported in 1.x"
)
def test_less_than_skipif():
    assert Card("a task") < Card("b task")


@pytest.mark.xfail(
    parse(api.__version__).major < 2,
    reason="Card comparison not supported in 1.x"
)
def test_less_than_xfail():
    assert Card("a task") < Card("b task")


@pytest.mark.xfail(reason="XPASS demo")
def test_xpass():
    assert Card("a task") == Card("a task")


@pytest.mark.xfail(reason="strict demo", strict=True)
def test_xpass_strict():
    assert Card("a task") == Card("a task")

