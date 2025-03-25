import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will execute first ")
    yield
    print("I will execute in last ")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created ")
    return ["Vinay", "Hassani", "hassanivinay@gmail.com"]
