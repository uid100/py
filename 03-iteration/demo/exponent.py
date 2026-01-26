#!/usr/bin/env python3

# Palomar College CSIT-175
# variables and constants

number = 0
exponent = 0
result = 1

# input - get number and exponent
number = int(input("Enter a number: "))
exponent = int(input("Enter the exponent: "))

# calculate exponent using the exponent operator
result = number ** exponent
    
print("The result is " + str(result))