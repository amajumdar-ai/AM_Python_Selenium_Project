import pytest


@pytest.mark.skip
def test_testcase1():
    print("testcase1")

def test_testcase2():
    print("testcase2")

@pytest.mark.xfail
def test_testcase3():
    a=2
    b=2
    assert a!=b

@pytest.mark.xfail
def test_testcase4():
    a=2
    b=2
    assert a==b

