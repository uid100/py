#!/usr/bin/env python3

# Estimate pi using the Monte Carlo method

import random
from xml.etree.ElementTree import PI
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import math

def get_points(n):
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
    return inside_x, inside_y, outside_x, outside_y

def draw_plot(fig, ax, n):
    ax.clear()

    inside_x, inside_y, outside_x, outside_y = get_points(n)

    inside_count = len(inside_x)
    pi_est = 4 * inside_count / n

    ax.scatter(inside_x, inside_y, s=1, label="Inside")
    ax.scatter(outside_x, outside_y, s=1, label="Outside")

    err = calculate_error(pi_est, math.pi)
    ax.set_title(f"Estimate of pi: {pi_est:.6f} (Error: {err:.2f}%)")
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_aspect('equal')
    ax.legend()

    fig.canvas.draw_idle()

def calculate_error(actual, expected):
    return abs(actual - expected) / expected * 100

def random_plot(num_samples=100):
    fig, ax = plt.subplots( figsize=(6,6) )
    plt.subplots_adjust(left=0.30)

    draw_plot(fig, ax, num_samples)
    
    ax_radio = plt.axes([0.05, 0.4, 0.15, 0.2])
    radio = RadioButtons(ax_radio, ('100', '1000', '10000', '100000', '1000000'))
    
    radio.on_clicked(lambda label: draw_plot(fig, ax, int(label)))
    plt.show()

if __name__ == "__main__":
    random_plot()
