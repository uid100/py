#!/usr/bin/env python3

# Palomar College CSIT-175
# While loop demo definite loop with a fixed number of iterations

# variables and constants
MAX_ITEMS = 10
count = 1

# Make sure the loop body code is indented 4 spaces!
# Also, note the colon (:)
# The Ctrl c key combination will break you out of an endless loop
# Print to the console
while count <= MAX_ITEMS:
    print(count, end=" ")
    count = count + 1 # Be sure to change the loop control variable!
print("\n End of loop printing")