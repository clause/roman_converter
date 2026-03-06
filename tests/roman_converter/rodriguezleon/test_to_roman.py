from types import ModuleType

def test_to_roman(impl: ModuleType):
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    assert impl.to_roman(58) == "LVIII"
    assert impl.to_roman(1994) == "MCMXCIV"
    assert impl.to_roman(3999) == "MMMCMXCIX"