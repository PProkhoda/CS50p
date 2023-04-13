import re
from numb3rs import validate

def test_cat():
    assert validate("AdaDs") == False
    assert validate("1.1.1.AdaDs") == False
    assert validate("1.1.AdaDs.1") == False
    assert validate("1.AdaDs.1.1") == False
    
    
def test_256():
    assert validate("256.256.1000.1000") == False

def test_notgood():
    assert validate("1921.168.1.1") == False
    assert validate("75.456.76.65") == False
    assert validate("192.168.1111.1") == False
    assert validate("192.168.1.1111") == False

def test_norm():
    assert validate("192.168.1.1") == True

def test_nonpoint():
    assert validate("1/1/1/1") == False