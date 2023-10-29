import pytest
import source.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_string():
    result = my_functions.add("I like ", "food")
    assert result == "I like food"
def test_devide():
    result = my_functions.devide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.devide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.devide(10, 5)
    assert result == 2


@pytest.mark.skip(reason ="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3


@pytest.mark.xfail(reason="We know we can't devide by zero")
def test_devide_by_zero_broke():
    my_functions.devide(4, 0)
