# Dyllan Sowers and Ethan Curley
# CIS 224 Project 1

import math;


def convert_to_decimal(n):
    while n > 1:
        n = n/10
    return n
# Converts a floating point number to binary
def convert_float_binary(n):
    # Left and right of decimal point
    left, right = str(n).split(".")
    left = int(left)
    right = int(right)

    # Convert left portion to binary and remove "0b"
    returnValue = bin(left).lstrip("-0b")

    # Return if right portion is 0 (n is a whole number)
    if right == 0:
        return returnValue
    
    # append "." for decimal
    returnValue += "."

    # Convert to precision 100
    for i in range(100):
        if(len(str((convert_to_decimal(right)) * 2).split(".")) > 1):
            left, right = str((convert_to_decimal(right)) * 2).split(".")
        # break if exact
        else: 
            break
        right = int(right)
        returnValue += left

    return returnValue


# Calculates the sign bit
def calculate_sign_bit(n):
    if n < 0:
        return 1
    return 0

# Converts binary to mantissa/fraction and exponent
def normalize_binary(bin):
    exponent = bin.index(".") - 1 
    # all chars after first with '.' removed
    mantissa = bin.replace(".", "")[1:]
    return str(exponent), mantissa


def calculate_exponent_biased(expo):
    exponentBits = 8
    expo = float(expo)
    return convert_float_binary(math.pow(2, exponentBits - 1) - 1 + expo)
    

def IEEE754_rep(sign, biased_expo, fraction):
    # append 0's if fraction does not use all 23 bits
    for i in range(len(fraction), 22): 
        fraction += "0"
    return (str(sign) + "-" + biased_expo + "-" + fraction)

def main():
    floatNum = -85.125
    binary = convert_float_binary(floatNum)
    signBit = calculate_sign_bit(floatNum)
    exponent, mantissa = normalize_binary(binary)
    biasedExponent = calculate_exponent_biased(exponent)
    representationIEEE = IEEE754_rep(signBit, biasedExponent, mantissa)

    print("The Binary representation of the number is :", binary)

    if signBit == 0:
        print("The sign is positive with a sign bit :", signBit)
    else:
        print("The sign is negative with a sign bit :", signBit)

    print("Mantissa:", mantissa, "exponent:", exponent)

    print("The exponent is", exponent, "and biased exponent is :", biasedExponent)

    print("The IEEE 754 single precision for", floatNum, "is :", representationIEEE)



main()
