#!/usr/bin/env python3

# Santa Fe College CSC 1107 - Python Programming
# Your Name Here
# Exercise: MPG Calculator with Tkinter GUI

from tkinter import *

# event handlers or callback functions
# click event handler for the Calculate button
def calculate_mpg():
    # get the user input from the entry widgets
    miles = float(miles_entry.get())
    gallons = float(gallons_entry.get())
    
    # calculate miles per gallon
    mpg = miles / gallons
    # calculate total cost
    cost_per_gallon = float(cost_entry.get())
    total_cost = gallons * cost_per_gallon
    # calculate cost per mile
    cost_per_mile = total_cost / miles
    # update the labels to display the results
    mpg_label.config(text=f"Miles per Gallon: {mpg:.2f}")
    total_cost_label.config(text=f"Total Cost: ${total_cost:.2f}")
    cost_per_mile_label.config( text=f"Cost per Mile: ${cost_per_mile:.2f}" )
    

def exit_program():
    frm.destroy()

# create the main application window, set the title and size
frm = Tk()
frm.title("MPG Calculator")
frm.geometry("450x200")

# configure the grid layout for the form
# add labels, entry widgets, and buttons to the window

# layout for inputs fields
# input fields for miles driven 
miles_label = Label(frm, text="Miles Driven:")
miles_label.grid(row=0, column=0)
miles_entry = Entry(frm, width=8)
miles_entry.grid(row=0, column=1)

# input fields for gallons used
gallons_label = Label(frm, text="Gallons Used:")
gallons_label.grid(row=1, column=0)
gallons_entry = Entry(frm, width=8)
gallons_entry.grid(row=1, column=1)

# input fields for cost per gallon
cost_label = Label(frm, text="Cost per Gallon:")
cost_label.grid(row=2, column=0)
cost_entry = Entry(frm, width=8)
cost_entry.grid(row=2, column=1)


# layout for output fields
# label to display the result
mpg_label = Label(frm, text="Miles per Gallon: ")
mpg_label.grid(row=4, column=0, columnspan=2)


total_cost_label = Label(frm, text="Total Cost: ")
total_cost_label.grid(row=5, column=0, columnspan=2)

cost_per_mile_label = Label(frm, text="Cost per Mile: ")
cost_per_mile_label.grid(row=6, column=0, columnspan=2)


# button to calculate MPG
calculate_button = Button(frm, text="Calculate MPG", command=calculate_mpg)
calculate_button.grid(row=3, column=0)  

# button to exit the program
exit_button = Button(frm, text="Exit", command=exit_program)
exit_button.grid(row=3, column=1)


# start the main event loop
frm.mainloop()

