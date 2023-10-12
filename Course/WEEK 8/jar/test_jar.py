from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar2 = Jar()
    jar3 = Jar()
    assert jar.deposit(1) == 1
    assert jar2.deposit(11) == 11
    with pytest.raises(ValueError):
        jar3.deposit(13)


def test_withdraw():
    jar = Jar()
    jar2 = Jar()
    jar3 = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar2.deposit(10)
    assert jar2.withdraw(10) == 0
