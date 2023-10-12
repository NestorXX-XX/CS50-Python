from twttr import shorten

def test_shorten():
    assert shorten("Hola") == "Hl"
    assert shorten("MACACO") == "MCC"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("CS50") == "CS50"
    assert shorten("hola QUE TAL") == "hl Q TL"
    assert shorten("hola, QUE TAL") == "hl, Q TL"
