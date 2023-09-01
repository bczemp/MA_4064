import matplotlib.pyplot as plt
import numpy as np
from math import e, ceil, sin, cos, pi

PLOT_MODE = ["display", "save"]

k = 1
m = 1
x0 = -1
dt = 0.0005

class State():
    def __init__(self, time, position, velocity):
        self.time = time
        self.position = position
        self.velocity = velocity

def euler_alg(initial, end, step_size): 
    states = [initial]
    current = State(initial.time, initial.position, initial.velocity)

    for x in range(ceil((end-initial.time)/step_size)):
        next_time = current.time + step_size
        next_velocity = round(current.velocity + -k/m * current.position * step_size, 6)
        next_position = round(current.position + current.velocity * step_size, 6)
        current.time = next_time
        current.position = next_position
        current.velocity = next_velocity
        states.append(State(next_time, next_position, next_velocity))
    return states 


def make_plot(states, title, xlabel, ylabel, plot_name="eulerplt.png"):
    fig, axes = plt.subplots()
    
    velocity = np.array([(state.time, state.velocity) for state in states])
    position = np.array([(state.time, state.position) for state in states])
    velocity_x, velocity_y = velocity.T
    position_x, position_y = position.T

    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)

    axes.plot(velocity_x, velocity_y, label="Velocity")
    axes.plot(position_x, position_y, label="Displacement")

    axes.legend()
    if "display" in PLOT_MODE: plt.show()
    if "save" in PLOT_MODE: fig.savefig(plot_name)

    return fig


def main():
    initial_state = State(0, x0, 0)
    end = 30
    step_size = dt
    data = euler_alg(initial_state, end, step_size)

    make_plot(data, f"Spring with k: {k} and mass: {m} starting at {initial_state.position}", "time", "", f"multi_{step_size}.png")
    print(f"{data[-1].position}, {data[-1].velocity}") 


if __name__ == "__main__": main()
