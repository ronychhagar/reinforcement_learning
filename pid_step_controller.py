# -*- coding: utf-8 -*-
"""pid step controller.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14j-CxADrK7nyZG7fMXUYRs6K4OzYAGnC
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the step function
def step_function(x):
    if x < 0.5:
        return 0
    else:
        return 1

# Define PID parameters
Kp = 1.0  # Proportional gain
Ki = 0.2  # Integral gain
Kd = 0.1  # Derivative gain

# Define the setpoint and initial state
setpoint = 1.0
state = 0.0

# Initialize variables
prev_error = 0.0
integral = 0.0
dt = 0.01  # Time step
timesteps = 1000  # Number of timesteps

# Store data for plotting
time = []
output = []
target = []

# Run the PID controller
for _ in range(timesteps):
    error = setpoint - state
    derivative = (error - prev_error) / dt
    integral += error * dt

    control = Kp * error + Ki * integral + Kd * derivative
    state += control * dt

    prev_error = error

    time.append(_ * dt)
    output.append(state)
    target.append(step_function(setpoint))

# Plot the output of the PID controller and target step function
plt.plot(time, output, label='PID Output')
plt.plot(time, target, label='Target Step Function')
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('PID Controller Output vs Target Step Function')
plt.legend()
plt.show()