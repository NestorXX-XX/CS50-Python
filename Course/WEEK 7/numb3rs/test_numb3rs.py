from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("255.100.255.255") == True
    assert validate("255.255.255.343") == False
    assert validate("255.255.255.cat") == False
    assert validate("255.255.255255") == False
    assert validate("255.255.255.25455") == False
    assert validate("1.1.1.1") == True
