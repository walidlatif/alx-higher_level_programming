def roman_to_int(roman_string):
    total_sum = 0
    index = 0
    if roman_string is not None:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                          'C': 100, 'D': 500, 'M': 1000}
        numeral_order = list(roman_numerals.keys())
        length = len(roman_string)
        for char in roman_string:
            if char in roman_numerals:
                if char in 'IXC':
                    if index < length - 1 and numeral_order[index + 1] in 'VXLCDM':
                        total_sum += roman_numerals[numeral_order[index + 1]] - roman_numerals[char]
                    else:
                        total_sum += roman_numerals[char]
                        index += 1              
    return total_sum
