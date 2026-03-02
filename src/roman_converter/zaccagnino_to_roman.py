def to_roman1(arabic: int) -> str:
    if not 0 < arabic < 4000:
        return "Input must be between 1 and 3999"
        
    roman_mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""
    for value, numeral in roman_mapping:
        count = arabic // value
        result += numeral * count
        arabic %= value
        
    return result

def arabic_to_roman_greedy(n: int) -> str:
    """Greedy mapping implementation. Supports 1..3999."""
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n <= 0 or n >= 4000:
        raise ValueError("n must be between 1 and 3999")
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    res = []
    for val, sym in vals:
        count, n = divmod(n, val)
        res.append(sym * count)
        if n == 0:
            break
    return "".join(res)


def arabic_to_roman_table(n: int) -> str:
    """Table-driven implementation using digit breakdown. Supports 1..3999."""
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n <= 0 or n >= 4000:
        raise ValueError("n must be between 1 and 3999")
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return (
        thousands[(n // 1000) % 10]
        + hundreds[(n // 100) % 10]
        + tens[(n // 10) % 10]
        + ones[n % 10]
    )








