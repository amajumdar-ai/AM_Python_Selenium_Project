import pytest


@pytest.fixture(scope="class")
def setup():
    print("setup is done")
    yield
    print("teardown is done")