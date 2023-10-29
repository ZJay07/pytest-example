import pytest
import source.my_functions as my_functions

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
    with pytest.raises(ZeroDivisionError):
        my_functions.devide(10, 0)

