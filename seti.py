def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    quotient = decimal_number
    binary_code = []
    while quotient != 0:
        if quotient % 2 == 1:
            binary_code.append(1)
            quotient = quotient//2
        else:
            binary_code.append(0)
            quotient = quotient//2
    binary_code.reverse()
    return binary_code


def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    base_binary = [0, 1]
    code_binary = []
    code_binary[:0] = str(binary_digits)
    n = len(code_binary)
    b = len(base_binary)
    sum = 0

    for i in range(n):
        sum += (2**i)*int(code_binary[n-1-i])
        
    return(sum) 


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    remainder = decimal_number
    base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    code = []
    while remainder != 0:
        code.append(base[remainder % destination_base])
        remainder = remainder//destination_base
    return code[::-1]


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    base_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    code = []
    code_to_convert = []
    sum = 0
    code_to_convert[:0] = str(digits)
    code_to_convert = code_to_convert[::-1]
    for i in range(len(code_to_convert)):
        dig = code_to_convert[i]
        if dig.isdigit():
            dig = int(dig)
        else:
            dig = base_num[base.index(dig)]
        sum += dig*(original_base**i)
    n = len(code_to_convert)
    return sum

digits_in_string = [2, 16, 9, 11]

def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    base_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

    converted = []
    if base > 16:
        raise ValueError
    for j in digits:
        if j > base-1:
            raise ValueError         
    for i in range(len(digits_in_string)):
            converted.append(base_num[digits_in_string[i]])
    return converted

def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    converted_digit = decimal_to_base(base_to_decimal(original_digits, original_base), destination_base)
    return converted_digit

print(digits_as_string(digits_in_string, 16))