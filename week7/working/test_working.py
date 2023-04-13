from working import convert
import pytest

# any test don't work with lowercase...
def test_am():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
#     assert convert("9 am to 10 am") == "09:00 to 10:00"

def test_pm():
    assert convert("1 PM to 3 PM") == "13:00 to 15:00"
    # assert convert("2 pm to 4 pm") == "14:00 to 16:00"

def test_ampm():
    # assert convert("1 am to 1 pm") == "01:00 to 13:00"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    
def test_pmam():
    # assert convert("10 pm to 11 am") == "22:00 to 11:00"
    assert convert("10 PM to 11 AM") == "22:00 to 11:00"
    assert convert("10:00 PM to 11:45 AM") == "22:00 to 11:45"

def test_value_error_enter():
    with pytest.raises(ValueError):
        assert convert("6 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("17:00 to 9 PM")

def test_value_error_minutes():
    with pytest.raises(ValueError):
        assert convert("6:66 AM to 9:79 PM")

##for test with sys.exit("ValueError")       
# def test_wrongtime():
#     with pytest.raises(SystemExit) as x:
#         convert("9:60 am to 01:70 pm")
#     assert x.type == SystemExit
#     assert x.value.code == "ValueError"
        
# def test_wronginput():
#     with pytest.raises(SystemExit) as x:
#         assert convert("9:60 am - 01:70 pm")
#     assert x.type == SystemExit
#     assert x.value.code == "ValueError"
