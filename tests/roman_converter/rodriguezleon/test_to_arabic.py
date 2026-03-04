from types import ModuleType

def test_to_arabic(impl: ModuleType):
    assert impl.to_arabic("I") == 1
    assert impl.to_arabic("IV") == 4
    assert impl.to_arabic("IX") == 9
    assert impl.to_arabic("LVIII") == 58
    assert impl.to_arabic("MCMXCIV") == 1994
    assert impl.to_arabic("MMMCMXCIX") == 3999