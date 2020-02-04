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

    # Convert left portion to binary and remove "0b", append "." for decimal
    returnValue = bin(left).lstrip("0b") + "."

    # Convert to precision 100
    for i in range(100):
        if(len(str((convert_to_decimal(right)) * 2).split(".")) > 1):
            left, right = str((convert_to_decimal(right)) * 2).split(".")
        else: # break if exact
            break
        right = int(right)
        returnValue += left

        
    return returnValue


# Calculates the sign bit
def calculate_sign_bit(n):
    if n > 0:
        return 1
    return 0

# Converts binary to mantissa/fraction and exponent
def normalize_binary(bin):
    return

def calculate_biased_exponent(expo):
    return

def IEEE754_rep(sign, biased_expo, fraction):
    return

def main():
    floatNum = 85.125
    print("{:f} converted to binary is {}".format(floatNum, convert_float_binary(floatNum)))
main()
