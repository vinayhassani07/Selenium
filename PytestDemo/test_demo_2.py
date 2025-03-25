import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do no  match"


def test_addGreet():
    a = 4
    b = 6
    assert a + 2 == b, "Addition is matching "



