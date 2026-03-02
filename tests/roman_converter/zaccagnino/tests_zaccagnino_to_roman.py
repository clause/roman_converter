from types import ModuleType


def test_to_roman1(impl: ModuleType):
    assert impl.to_roman1(1) == "I"
    assert impl.to_roman1(52) == "LII"
    assert impl.to_roman1(176) == "CLXXVI"
    assert impl.to_roman1(1256) == "MCCLVI"
    assert impl.to_roman1(3999) == "MMMCMXCIX"

def test_arabic_to_roman_greedy(impl: ModuleType):
    assert impl.arabic_to_roman_greedy(1) == "I"
    assert impl.arabic_to_roman_greedy(52) == "LII"
    assert impl.arabic_to_roman_greedy(176) == "CLXXVI"
    assert impl.arabic_to_roman_greedy(1256) == "MCCLVI"
    assert impl.arabic_to_roman_greedy(3999) == "MMMCMXCIX"

def test_arabic_to_roman_table(impl: ModuleType):
    assert impl.arabic_to_roman_table(1) == "I"
    assert impl.arabic_to_roman_table(52) == "LII"
    assert impl.arabic_to_roman_table(176) == "CLXXVI"
    assert impl.arabic_to_roman_table(1256) == "MCCLVI"
    assert impl.arabic_to_roman_table(3999) == "MMMCMXCIX"