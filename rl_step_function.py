# -*- coding: utf-8 -*-
"""RL_step_function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sNxVrPIRkscWxKjLqVoSQpA9hzD76B3f
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the step function
def step_function(x):
    if x < 0.5:
        return 0
    else:
        return 1

# Define the Q-learning algorithm
def q_learning_step(Q, state, action, reward, next_state, alpha, gamma):
    # Update Q-value for the current state and action
    Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])

# Initialize Q-table
num_states = 100
num_actions = 2
Q = np.zeros((num_states, num_actions))

# Define the exploration-exploitation tradeoff
epsilon = 0.1

# Set learning parameters
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor

# Define the number of episodes and steps per episode
num_episodes = 10000
max_steps = 100

# Run Q-learning
for episode in range(num_episodes):
    # Initialize the environment
    state = np.random.randint(0, num_states)

    for step in range(max_steps):
        # Choose an action
        if np.random.rand() < epsilon:
            action = np.random.randint(0, num_actions)
        else:
            action = np.argmax(Q[state, :])

        # Execute the action and observe the reward and next state
        if action == step_function(state / (num_states - 1)):
            reward = 1
        else:
            reward = -1

        next_state = np.random.randint(0, num_states)

        # Update Q-values
        q_learning_step(Q, state, action, reward, next_state, alpha, gamma)

        # Update the current state
        state = next_state

        # Check if the goal state is reached
        if state == num_states - 1:
            break

# Test the learned policy
current_state = 0
trajectory = [current_state]

while current_state != num_states - 1:
    action = np.argmax(Q[current_state, :])
    next_state = np.random.randint(0, num_states)
    trajectory.append(next_state)
    current_state = next_state

# Print the learned trajectory
print("Learned trajectory:", trajectory)

# Plot the learned function and target trajectory
x = np.linspace(0, 1, 1000)
y_learned = np.zeros_like(x)

for i in range(len(x)):
    state = int(x[i] * (num_states - 1))
    action = np.argmax(Q[state, :])
    y_learned[i] = action

y_target = np.array([step_function(xi) for xi in x])

plt.plot(x, y_target, label='Target Trajectory')
plt.plot(x, y_learned, label='Learned Function')
plt.xlabel('X')
plt.ylabel('Output')
plt.title('Learned Function vs Target Trajectory')
plt.legend()
plt.show()