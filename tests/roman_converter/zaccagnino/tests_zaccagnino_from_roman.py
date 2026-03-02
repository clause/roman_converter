from types import ModuleType

def test_roman_to_int_comparison(impl: ModuleType):
    assert impl.roman_to_int_comparison("I") == 1
    assert impl.roman_to_int_comparison("IV") == 4
    assert impl.roman_to_int_comparison("XXVI") == 26
    assert impl.roman_to_int_comparison("MDCLXVI") == 1666
    assert impl.roman_to_int_comparison("MMMCMXCIX") == 3999

def romanToInt_reverse(impl: ModuleType):
    assert impl.romanToInt_reverse("I") == 1
    assert impl.romanToInt_reverse("IV") == 4
    assert impl.romanToInt_reverse("XXVI") == 26
    assert impl.romanToInt_reverse("MDCLXVI") == 1666
    assert impl.romanToInt_reverse("MMMCMXCIX") == 3999

def test_romanToInt_replace(impl: ModuleType):
    assert impl.romanToInt_replace("I") == 1
    assert impl.romanToInt_replace("IV") == 4
    assert impl.romanToInt_replace("XXVI") == 26
    assert impl.romanToInt_replace("MDCLXVI") == 1666
    assert impl.romanToInt_replace("MMMCMXCIX") == 3999