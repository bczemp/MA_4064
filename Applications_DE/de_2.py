import matplotlib.pyplot as plt
import numpy as np
import csv
from copy import deepcopy
from math import e, ceil, sin, cos, pi

PLOT_MODE = ["display"]
SAVE_DATA = True
PART = 5

class State():
    def __init__(self, time, rabbits, foxes):
        self.time = time
        self.rabbits = rabbits
        self.foxes = foxes

initial_state = State(0, 200, 50)
end = 200
dt = 1
k1 = 0.05
k2 = 0.001
k3 = 0.0002
k4 = 0.03
k5 = 0.06


def fox_step(state, dt): 
    next_foxes = state.foxes + (k3 * (state.foxes * state.rabbits) - k4 * state.foxes - k5 * state.foxes) * dt

    return next_foxes

def rabbit_step(state, dt):
    next_rabbits = state.rabbits + (k1 * state.rabbits - k2 * (state.foxes * state.rabbits) - k5 * state.rabbits) * dt

    return next_rabbits

def simulate(initial_state, end_time, dt):
    if PART != 7:
        global k5
        k5 = 0

    states = [deepcopy(initial_state)]

    for step in range(round((end_time - initial_state.time) / dt)):
        if PART == 6 and states[-1].time == 51:
            global k1
            k1 = 0.03
        next_time = states[-1].time + dt
        next_foxes = fox_step(states[-1], dt)
        next_rabbits = rabbit_step(states[-1], dt)

        states.append(State(next_time, next_rabbits, next_foxes))

    return states

def make_plot(states, title, plot_name):
    fig, axes = plt.subplots()
    
    rabbits = np.array([(state.time, state.rabbits) for state in states])
    foxes = np.array([(state.time, state.foxes) for state in states])
    rabbits_x, rabbits_y = rabbits.T
    foxes_x, foxes_y = foxes.T

    axes.set_title(title)
    axes.set_xlabel("Time")
    axes.set_ylabel("Population")

    axes.plot(rabbits_x, rabbits_y, label="Rabbits")
    axes.plot(foxes_x, foxes_y, label="Foxes")

    axes.legend()
    if "display" in PLOT_MODE: plt.show()
    if "save" in PLOT_MODE: fig.savefig("plots/"+plot_name)

    return fig

def write_data(data, name):
    with open("data/"+name, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(["Time", "Rabbits", "Foxes"])

        for state in data:
            csv_writer.writerow([state.time, state.rabbits, state.foxes])

def compute_avg(data, end):
    foxes = 0
    rabbits = 0
    total = 0

    for state in data:
        if state.time > end: break
        foxes += state.foxes
        rabbits += state.rabbits
        total += 1

    return foxes/total, rabbits/total

def main():
    data = simulate(initial_state, end, dt)
    make_plot(data, "Predator Prey", f"de2_{PART}.png")
    if SAVE_DATA: write_data(data, f"de2_{PART}.csv")
    print(f"Average of fox and rabbit populations: {compute_avg(data, 165)}")
    print(f"Final foxes: {data[-1].foxes} Final rabbits: {data[-1].rabbits}")

if __name__ == "__main__": main()
