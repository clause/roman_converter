from types import ModuleType


# Basic numerals
def test_I(impl: ModuleType):
    assert impl.from_roman("I") == 1


def test_V(impl: ModuleType):
    assert impl.from_roman("V") == 5


def test_X(impl: ModuleType):
    assert impl.from_roman("X") == 10


def test_L(impl: ModuleType):
    assert impl.from_roman("L") == 50


def test_C(impl: ModuleType):
    assert impl.from_roman("C") == 100


def test_D(impl: ModuleType):
    assert impl.from_roman("D") == 500


def test_M(impl: ModuleType):
    assert impl.from_roman("M") == 1000


# Subtractive notation
def test_IV(impl: ModuleType):
    assert impl.from_roman("IV") == 4


def test_IX(impl: ModuleType):
    assert impl.from_roman("IX") == 9


def test_XL(impl: ModuleType):
    assert impl.from_roman("XL") == 40


def test_XC(impl: ModuleType):
    assert impl.from_roman("XC") == 90


def test_CD(impl: ModuleType):
    assert impl.from_roman("CD") == 400


def test_CM(impl: ModuleType):
    assert impl.from_roman("CM") == 900


# Repetition
def test_II(impl: ModuleType):
    assert impl.from_roman("II") == 2


def test_III(impl: ModuleType):
    assert impl.from_roman("III") == 3


def test_XX(impl: ModuleType):
    assert impl.from_roman("XX") == 20


def test_XXX(impl: ModuleType):
    assert impl.from_roman("XXX") == 30


def test_CCC(impl: ModuleType):
    assert impl.from_roman("CCC") == 300


def test_MMM(impl: ModuleType):
    assert impl.from_roman("MMM") == 3000


# Compound numerals
def test_XIV(impl: ModuleType):
    assert impl.from_roman("XIV") == 14


def test_XLII(impl: ModuleType):
    assert impl.from_roman("XLII") == 42


def test_XCIX(impl: ModuleType):
    assert impl.from_roman("XCIX") == 99


def test_CCCXCIX(impl: ModuleType):
    assert impl.from_roman("CCCXCIX") == 399


def test_MCMXCIV(impl: ModuleType):
    assert impl.from_roman("MCMXCIV") == 1994


def test_MMXXIV(impl: ModuleType):
    assert impl.from_roman("MMXXIV") == 2024


def test_MMMCMXCIX(impl: ModuleType):
    assert impl.from_roman("MMMCMXCIX") == 3999


# Misc values
def test_LVIII(impl: ModuleType):
    assert impl.from_roman("LVIII") == 58


def test_DCXXI(impl: ModuleType):
    assert impl.from_roman("DCXXI") == 621


def test_MDCCLXXVI(impl: ModuleType):
    assert impl.from_roman("MDCCLXXVI") == 1776


def test_MMCDXXI(impl: ModuleType):
    assert impl.from_roman("MMCDXXI") == 2421
