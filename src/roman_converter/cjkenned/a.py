###########################
# Section 1: My Functions # 
###########################

def to_roman(arabic: int) -> str:
    roman_numerals = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1)
    ]
    roman = "" 
    
    # Check for valid input range 
    if arabic <= 0 or arabic > 3999:
        # Value doesn't fit basic roman numeral format 
        raise ValueError("Arabic number must be between 1->3999")
    
    count = 0
    while arabic > 0 and count < len(roman_numerals):
        curr_roman, curr_value = roman_numerals[count]
        
        # Check for subtraction 
        if count + 2 < len(roman_numerals):
            next_roman, next_value = roman_numerals[count + 2]
            
            # Check if it fits 
            if arabic >= curr_value - next_value:
                # Valid, update and decriment arabic 
                roman += next_roman + curr_roman
                arabic -= (curr_value - next_value)
                count += 1
                continue 
        
        # Regular situation 
        
        # Check if valid (Also checking amount (Ex: 3 -> III))
        if (arabic // curr_value) > 0:
            # Valid 
            roman += curr_roman * (arabic // curr_value)
            arabic %= curr_value

        count += 1
    return roman

def from_roman(roman: str) -> int:
    # Define a dict for later use
    roman_numerals = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L":50,
                "C": 100,
                "D": 500,
                "M": 1000
    }
    roman_sub = [1,10,100]  # Valid subtraction is 1,10,100 / I,X,C
    
    cache = 0 
    count = 0
    
    # Split the roman up into letters and loop through it 
    for i in range(len(roman)):
        
        current_value = roman_numerals[roman[i]]
        
        # Check if the variable exists 
        if roman[i] not in roman_numerals:
            raise ValueError("Valid Roman numerals contain I,V,X,L,C,D,M") 

        # Check if the cache value is lower or not 
        if (cache < current_value):
            # Subtraction case Ex: IV
            
            # Need to check if subtraction is valid 
            if cache in roman_sub and cache != 0:
                # Valid subtraction case 
                count = count + (current_value - 2 * cache)
            else:
                # Not valid subtraction cache variable
                raise ValueError("Valid subtraction needs to consist of I,X,C") 
            
        else:
            count = count + current_value
        
        # Update Cache    
        cache = current_value

    # Return the total count
    return count

##############################
# Section 3: Bugged Versions #
##############################


def to_roman_3(arabic: int) -> str:
    # The bug in this version is as follows 
    #   - Doesn't do subtraction
    #   - Takes too big of an input range
    
    roman_numerals = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1)
    ]
    roman = ""
    
    count = 0
    while arabic > 0 and count < len(roman_numerals):
        roman, value = roman_numerals[count]
        
        # Regular situation 
        
        # Check if valid (Also checking amount (Ex: 3 -> III))
        if (arabic // value) > 0:
            # Valid 
            roman += roman * (arabic // value)
            arabic %= value

        count += 1
    return roman 

def from_roman_3(roman: str) -> int:
    #  The bug in this versions is as follows
    #   - Doesn't handle subtraction properly 
    
    # Define a dict for later use
    roman_numerals = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L":50,
                "C": 100,
                "D": 500,
                "M": 1000
    }
    roman_sub = [1,5,50,500]  # Valid subtraction is 1,10,100 / I,X,C
    
    cache = 0 
    count = 0
    
    # Split the roman up into letters and loop through it 
    for i in range(len(roman)):
        
        current_value = roman_numerals[roman[i]]
        
        # Check if the variable exists 
        if roman[i] not in roman_numerals:
            raise ValueError("Valid Roman numerals contain I,V,X,L,C,D,M") 

        # Check if the cache value is lower or not 
        if (cache < current_value):
            # Subtraction case Ex: IV
            
            # Need to check if subtraction is valid 
            if cache in roman_sub and cache != 0:
                # Valid subtraction case 
                count = count + (current_value - 2 * cache)
            else:
                # Not valid subtraction cache variable
                raise ValueError("Valid subtraction needs to consist of I,X,C") 
            
        else:
            count = count + current_value
        
        # Update Cache    
        cache = current_value

    # Return the total count
    return count