#!/usr/bin/env python3

# import locale to do currency formatting
import locale
locale.setlocale(locale.LC_ALL, 'en-US')

# Cuyamaca College CS-119
# While loop demo indefinite loop unknown number of iterations

# variables and constants
amount = 0.0
total = 0.0 # the variable total works as an accumulator

# priming read to make sure the loop control variable is initialized
amount = float(input("Enter amount: "))


# amount serves as both a sentinel and loop control variable
while amount > 0:
    total = total + amount # accumulate a running total
    amount = float(input("Enter amount: "))

# output - after the loop ends, display the total
print("Total = " + locale.currency(total, grouping=True)) 