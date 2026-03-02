from types import ModuleType


def test_to_roman1(impl: ModuleType):
    assert impl.to_roman1(1) == "I"
    assert impl.to_roman1(50) == "L"
    assert impl.to_roman1(100) == "C"
    assert impl.to_roman1(1000) == "M"
    assert impl.to_roman1(3999) == "MMMCMXCIX"

def test_arabic_to_roman_greedy(impl: ModuleType):
    assert impl.arabic_to_roman_greedy(1) == "I"
    assert impl.arabic_to_roman_greedy(50) == "L"
    assert impl.arabic_to_roman_greedy(100) == "C"
    assert impl.arabic_to_roman_greedy(1000) == "M"
    assert impl.arabic_to_roman_greedy(3999) == "MMMCMXCIX"

def test_arabic_to_roman_table(impl: ModuleType):
    assert impl.arabic_to_roman_table(1) == "I"
    assert impl.arabic_to_roman_table(50) == "L"
    assert impl.arabic_to_roman_table(100) == "C"
    assert impl.arabic_to_roman_table(1000) == "M"
    assert impl.arabic_to_roman_table(3999) == "MMMCMXCIX"