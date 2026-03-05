from bfajps import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(7, 3) == 10
    assert suma(-1, 5) == 4
    assert suma(2, 4) == 6