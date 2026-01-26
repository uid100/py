#!/usr/bin/env python3

# Cuyamaca College CS-119
# Demo of string.isnumeric()

# variables
str_input = ""
num_input = 0

#Data validation example. Loop until the user enters a number
str_input = input("Enter a number: ")

# Note the isnumeric() method is limited to integers
while str_input.isnumeric() == False:
    str_input = input("Enter a number: ")

num_input = float(str_input)

print("The validated number is " + str(num_input))