import pytest

from pyest.conftest import setup


@pytest.mark.usefixtures("setup")

class TestFixture:

  def test_1(self):
    print("First test")
  def test_2(self):
    a=1
    b=2
    assert a != b