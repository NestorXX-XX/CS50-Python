from seasons import check_birthday

def test_date_constructor():
    assert check_birthday("2000-12-12") == True
    assert check_birthday("2000-12-02") == True
