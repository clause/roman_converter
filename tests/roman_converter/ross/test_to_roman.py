from types import ModuleType

# Base Case Coverage
def test_to_roman_base(impl: ModuleType):
    # uses all letters at least once
    assert impl.to_roman(1447) == "MCDXLVII"

def test_to_roman_thousands(impl: ModuleType):
    # Change thousands value
    assert impl.to_roman(2447) == "MMCDXLVII"

def test_to_roman_hundreds(impl: ModuleType):
    # Change hundreds value
    assert impl.to_roman(1547) == "MDXLVII"

def test_to_roman_tens(impl: ModuleType):
    # Change tens value
    assert impl.to_roman(1427) == "MCDXXVII"

def test_to_roman_ones(impl: ModuleType):
    # Change ones value
    assert impl.to_roman(1449) == "MCDXLIX"

def test_to_roman_lbound(impl: ModuleType):
    # Lower boundary
    assert impl.to_roman(1) == "I"

def test_to_roman_ubound(impl: ModuleType):
    # Upper boundary
    assert impl.to_roman(3999) == "MMMCMXCIX"