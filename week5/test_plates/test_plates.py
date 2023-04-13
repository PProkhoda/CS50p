from plates import is_valid

def test_alnum():
    notnum = [".", ",", "?", "<", ">", "!", "#", "#", "$", "%", "*"]
    s = "QW"
    for i in notnum:
        assert is_valid(s + i) == False


def test_len():
    assert is_valid("") == False
    assert is_valid("Q") == False
    assert is_valid("qwertyuq") == False


def test_isdigit():
    assert is_valid("Q1") == False
    assert is_valid("1Q") == False


def test_wordafterint():
    assert is_valid("CS50P") == False

def test_zero():
    assert is_valid("CS0") == False
    assert is_valid("CSA0") == False
    assert is_valid("CSAS0") == False
    assert is_valid("CSASD0") == False
    assert is_valid("CSZXCV0") == False