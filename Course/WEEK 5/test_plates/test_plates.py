from plates import is_valid

def test_must_start_with_at_least_two_letters():
    assert is_valid("1S50") == False
    assert is_valid("CS50") == True
    assert is_valid("1S50") == False
    assert is_valid("0S50") == False

def test_maximum_of_6_characters_letters_or_numbers_and_a_minimum_of_2_characters():
    assert is_valid("CS50") == True
    assert is_valid("CS501090") == False
    assert is_valid("CS001090") == False

def test_No_periods_spaces_or_punctuation_marks_are_allowed():
    assert is_valid("CS50") == True
    assert is_valid("CS.50") == False

def test_Numbers_cannot_be_used_in_the_middle_of_a_plate_they_must_come_at_the_end():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS5 0") == False
    assert is_valid("CSá0") == False
