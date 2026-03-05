def roman_to_int_comparison(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            num -= roman_map[s[i]]
        else:
            num += roman_map[s[i]]
    return num

def romanToInt_reverse(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer, previous_value = 0, 0
    for ch in reversed(s):
        current_value = roman_map[ch]
        if current_value < previous_value:
            integer -= current_value
        else:
            integer += current_value
        previous_value = current_value
    return integer 

def romanToInt_replace(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    return sum(roman_map[x] for x in s)
