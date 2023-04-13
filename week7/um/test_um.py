from um import count

def test_inword():
    assert count("Ummy") == 0


def test_norm():
    assert count("um um") == 2


def test_ignorecase():
    assert count("Um UM um uM") == 4


def test_punctuation():
    assert count("um, .um um... .um.") == 4
