import sys
from os.path import expanduser, abspath

GIT_DIR = "~/Documents/MA_4064"
sys.path.append(abspath(expanduser(GIT_DIR + '/lib')))

import numerical_integration as integrate
import plot
from time import time

PART = 2
WRITE = True

dt = 0.05
t_final = 100
t = 0
y = [3500, 1800, 2400]

huron = [[t, y[0]]]
erie = [[t, y[1]]]
ontario = [[t, y[2]]]
reached = [False, False, False]

def great_lakes_q2(y):
    H, E, O = y

    dH = 25 - 0.11 * H
    dE = 0.11 * H - 0.36 * E
    dO = 0.36 * E - 0.12 * O

    return dH, dE, dO

def great_lakes_q3(y):
    H, E, O = y

    dH = (25 if t < 10 else 0) - 0.11 * H
    dE = 0.11 * H - 0.36 * E
    dO = 0.36 * E - 0.12 * O

    return dH, dE, dO

def great_lakes_q4(y):
    H, E, O = y

    dH = -0.11 * H
    dE = 25 + 0.11 * H - 0.36 * E
    dO = 0.36 * E - 0.12 * O

    return dH, dE, dO

def great_lakes(y):
    if PART == 3:
        return great_lakes_q3(y)
    elif PART == 4:
        return great_lakes_q4(y)
    else:
        return great_lakes_q2(y)


for step in range(int((t_final - t) / dt)):
    t, y = integrate.euler(great_lakes, t, y, dt) 
    huron.append([t, y[0]])
    erie.append([t, y[1]])
    ontario.append([t, y[2]])

    if y[0] <= 0.08 * huron[0][1] and not reached[0]:
       print(f"Huron at 8% ({y[0]}) after {round(t, 6)} years")
       reached[0] = True
    if y[1] <= 0.08 * erie[0][1] and not reached[1]:
       print(f"Erie at 8% ({y[1]}) after {round(t, 6)} years")
       reached[1] = True
    if y[2] <= 0.08 * ontario[0][1] and not reached[2]:
       print(f"Ontario at 8% ({y[2]}) after {round(t, 6)} years")
       reached[2] = True

print(y)

plot.plot_data(f"Great Lakes Euler's method\nStep size: {dt}, Initial condtion: t = {huron[0][0]} H = {huron[0][1]} E = {erie[0][1]} O = {ontario[0][1]}\n" + r"$t_{final}$" + f" = {t_final}", "Time (years)", "Pollutant (tons)", ["Lake Huron", "Lake Erie", "Lake Ontario"], [huron, erie, ontario], save=WRITE, file_name=f"../plots/Great_Lakes_q{PART}.png")

time_data = [point[0] for point in huron]
huron_data = [point[1] for point in huron]
erie_data = [point[1] for point in erie]
ontario_data = [point[1] for point in ontario]

plot.export_data(f"../data/Great_Lakes_q{PART}.csv", ["Time (years)", "Lake Huron", "Lake Erie", "Lake Ontario"], [time_data, huron_data, erie_data, ontario_data])
