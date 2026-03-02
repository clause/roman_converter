from types import ModuleType


def test_to_roman(impl: ModuleType):
    assert impl.to_roman(4) == "IV"
