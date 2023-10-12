from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("HeLlO") == 0

def test_h():
    assert value("Hey") == 20
    assert value("How are you doing?") == 20
    assert value("hi") == 20

def test_nothing():
    assert value("What's up?") == 100
    assert value("Wey") == 100
    assert value("fasfdsafsdaf") == 100

