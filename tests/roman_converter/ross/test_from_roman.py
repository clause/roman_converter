from types import ModuleType

# Base Case Coverage
def test_from_roman_base(impl: ModuleType):
    # uses all letters at least once
    assert impl.from_roman("MCDXLVII") == 1447

def test_from_roman_thousands(impl: ModuleType):
    # Change thousands value
    assert impl.from_roman("MMCDXLVII") == 2447

def test_from_roman_hundreds(impl: ModuleType):
    # Change hundreds value
    assert impl.from_roman("MDXLVII") == 1547

def test_from_roman_tens(impl: ModuleType):
    # Change tens value
    assert impl.from_roman("MCDXXVII") == 1427

def test_from_roman_ones(impl: ModuleType):
    # Change ones value
    assert impl.from_roman("MCDXLIX") == 1449

def test_from_roman_lbound(impl: ModuleType):
    # Lower boundary
    assert impl.from_roman("I") == 1

def test_from_roman_ubound(impl: ModuleType):
    # Upper boundary
    assert impl.from_roman("MMMCMXCIX") == 3999
