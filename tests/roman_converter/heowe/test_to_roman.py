from types import ModuleType


# Basic numerals
def test_1(impl: ModuleType):
    assert impl.to_roman(1) == "I"


def test_5(impl: ModuleType):
    assert impl.to_roman(5) == "V"


def test_10(impl: ModuleType):
    assert impl.to_roman(10) == "X"


def test_50(impl: ModuleType):
    assert impl.to_roman(50) == "L"


def test_100(impl: ModuleType):
    assert impl.to_roman(100) == "C"


def test_500(impl: ModuleType):
    assert impl.to_roman(500) == "D"


def test_1000(impl: ModuleType):
    assert impl.to_roman(1000) == "M"


# Subtractive notation
def test_4(impl: ModuleType):
    assert impl.to_roman(4) == "IV"


def test_9(impl: ModuleType):
    assert impl.to_roman(9) == "IX"


def test_40(impl: ModuleType):
    assert impl.to_roman(40) == "XL"


def test_90(impl: ModuleType):
    assert impl.to_roman(90) == "XC"


def test_400(impl: ModuleType):
    assert impl.to_roman(400) == "CD"


def test_900(impl: ModuleType):
    assert impl.to_roman(900) == "CM"


# Repetition
def test_2(impl: ModuleType):
    assert impl.to_roman(2) == "II"


def test_3(impl: ModuleType):
    assert impl.to_roman(3) == "III"


def test_20(impl: ModuleType):
    assert impl.to_roman(20) == "XX"


def test_30(impl: ModuleType):
    assert impl.to_roman(30) == "XXX"


def test_300(impl: ModuleType):
    assert impl.to_roman(300) == "CCC"


def test_3000(impl: ModuleType):
    assert impl.to_roman(3000) == "MMM"


# Compound numerals
def test_14(impl: ModuleType):
    assert impl.to_roman(14) == "XIV"


def test_42(impl: ModuleType):
    assert impl.to_roman(42) == "XLII"


def test_99(impl: ModuleType):
    assert impl.to_roman(99) == "XCIX"


def test_399(impl: ModuleType):
    assert impl.to_roman(399) == "CCCXCIX"


def test_1994(impl: ModuleType):
    assert impl.to_roman(1994) == "MCMXCIV"


def test_2024(impl: ModuleType):
    assert impl.to_roman(2024) == "MMXXIV"


def test_3999(impl: ModuleType):
    assert impl.to_roman(3999) == "MMMCMXCIX"


# Misc values
def test_58(impl: ModuleType):
    assert impl.to_roman(58) == "LVIII"


def test_621(impl: ModuleType):
    assert impl.to_roman(621) == "DCXXI"


def test_1776(impl: ModuleType):
    assert impl.to_roman(1776) == "MDCCLXXVI"


def test_2421(impl: ModuleType):
    assert impl.to_roman(2421) == "MMCDXXI"
