#!/usr/bin/env python3

# Santa Fe College CSC 1107 - Python Programming
# Your Name Here
# Exercise: MPG Calculator with Tkinter GUI

from tkinter import *

# event handlers or callback functions
# click event handler for the Calculate button
def cost_estimate():
    month = int(month_entry.get())
    nights = int(nights_entry.get())
    
    if month in [1, 2, 3]:  # Winter
        rate = 80
    elif month in [4, 5, 6]:  # Spring
        rate = 90
    elif month in [7, 8, 9]:  # Summer
        rate = 120
    elif month in [10, 11, 12]:  # Fall
        rate = 100
    else:
        cost_result_label.config(text="Invalid month")
        return
    
    total_cost = rate * nights
    cost_result_label.config(text=f"${total_cost:.2f}")

def exit_program():
    frm.destroy()

# create the main application window, set the title and size
frm = Tk()
frm.title("Coyote Inn")
frm.geometry("350x250")

welcome_label = Label(frm, text="Welcome to the Coyote Inn!")
welcome_label.grid(row=0, column=0)

month_label = Label(frm, text="Month of Stay (1-12):")
month_label.grid(row=1, column=0)
month_entry = Entry(frm, width=8)
month_entry.grid(row=1, column=1)

nights_label = Label(frm, text="Number of Nights:")
nights_label.grid(row=2, column=0)
nights_entry = Entry(frm, width=8)
nights_entry.grid(row=2, column=1)

cost_label = Label(frm, text="Estimated Cost:")
cost_label.grid(row=3, column=0)
cost_result_label = Label(frm, text="")
cost_result_label.grid(row=3, column=1)

rates_label = Label(frm, text="Room Rates:")
rates_label.grid(row=10, column=0)
winter_rate_label = Label(frm, text="1 - 3 (Jan - Mar): $80/night")
winter_rate_label.grid(row=11, column=0)
spring_rate_label = Label(frm, text="4 - 6 (Apr - Jun): $90/night")
spring_rate_label.grid(row=12, column=0)
summer_rate_label = Label(frm, text="7 - 9 (Jul - Sept): $120/night")
summer_rate_label.grid(row=13, column=0)
fall_rate_label = Label(frm, text="10 - 12 (Oct - Dec): $100/night")
fall_rate_label.grid(row=14, column=0)

calculate_button = Button(frm, text="Calculate Cost", command=cost_estimate)
calculate_button.grid(row=5, column=0)
exit_button = Button(frm, text="Exit", command=exit_program)
exit_button.grid(row=5, column=1)

frm.mainloop()