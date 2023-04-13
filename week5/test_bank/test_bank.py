from bank import value


def test_h():
    assert value("Hasd ><.,012345678") == 20
    assert value("hasd ><.,012345678") == 20


def test_hello():
    assert value("HELLOasd ><.,012345678") == 0
    assert value("helloasd ><.,012345678") == 0


def test_norm():
    assert value(" .asd ><.,012345678") == 100
    assert value("_elloasd ><.,012345678") == 100
    assert value("0elloasd ><.,012345678") == 100
    assert value("Aelloasd ><.,012345678") == 100