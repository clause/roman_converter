from types import ModuleType

def test_from_roman(impl: ModuleType):
    assert impl.from_roman("I") == 1
    assert impl.from_roman("IV") == 4
    assert impl.from_roman("IX") == 9
    assert impl.from_roman("LVIII") == 58
    assert impl.from_roman("MCMXCIV") == 1994
    assert impl.from_roman("MMMCMXCIX") == 3999