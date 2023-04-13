from fuel import gauge, convert
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")
        
def test_value_error():
    with pytest.raises(ValueError):
        assert convert("int")

def test_value_error():
    with pytest.raises(ValueError):
        assert convert("2/1")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    
def test_norm():
    assert convert("1/4") == 25
