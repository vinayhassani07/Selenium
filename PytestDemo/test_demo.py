import pytest


def test_firstProgram():
    print("Hello")


@pytest.mark.smoke
def test_secondGreet():
    print("Good Morning")
