#!/usr/bin/env python3

# Cuyamaca College CS-119
# For loop demo definite loop with a known number of iterations

# variables and constants
MAX_ITEMS = 10
count = 1
total = 0 # Just for fun, let's keep a running total of the numbers

# Note the use of the range() method to control the loop
for count in range(MAX_ITEMS):
    total = total + count # accumulate a running total
    print(str(count), end=' ')
    
# output - after the loop ends, display the total
print("\nTotal = " + str(total)) 

# another variation on the range function
total = 0
count = 1

# This time, we also specify start and step value in the range() method
for count in range(1, MAX_ITEMS + 1, 1):
    total = total + count # accumulate a running total
    print(str(count), end=' ')
    
# output - after the loop ends, display the total
print("\nTotal = " + str(total)) 