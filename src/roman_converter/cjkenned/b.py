##################################
# Section 2: More Basic Versions #
##################################

def to_roman(arabic: int) -> str:
    # Found online 
    
    chlist = "VXLCDM"
    rev = [int(ch) for ch in reversed(str(arabic))]
    chlist = ["I"] + [chlist[i % len(chlist)] + "\u0304" * (i // len(chlist))
                    for i in range(0, len(rev) * 2)]

    def period(p: int, ten: str, five: str, one: str) -> str:
        if p == 9:
            return one + ten
        elif p >= 5:
            return five + one * (p - 5)
        elif p == 4:
            return one + five
        else:
            return one * p

    return "".join(reversed([period(rev[i], chlist[i * 2 + 2], chlist[i * 2 + 1], chlist[i * 2])
                            for i in range(0, len(rev))]))

def from_roman(roman: str) -> int:
    # Found online
    
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    arabic_num = 0
    # Iterate through the string up to the second to last character
    for i in range(len(roman) - 1):
        # If current value is less than the next, it's a subtractive case
        if roman_map[roman[i]] < roman_map[roman[i+1]]:
            arabic_num -= roman_map[roman[i]]
        else:
            arabic_num += roman_map[roman[i]]
    
    # Add the value of the last character, which is always added
    arabic_num += roman_map[roman[-1]]
    return arabic_num