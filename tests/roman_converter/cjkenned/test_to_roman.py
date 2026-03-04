from types import ModuleType
import pytest


def test_to_roman(impl: ModuleType):
    
    # Subtractive Cases 
    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    
    # Repetative 
    assert impl.to_roman(3) == "III"
    
    # Upper bound 
    assert impl.to_roman(3999) == "MMCMXCIX"
    
    # Invalid calls 
    with pytest.raises(ValueError):
        impl.to_roman(4001)
    with pytest.raises(ValueError):
        impl.to_roman(0)
    
