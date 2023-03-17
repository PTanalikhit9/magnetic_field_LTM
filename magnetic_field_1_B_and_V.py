
import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the rectangular magnet
length = 10.0
width = 4.0

# Define the strength of the magnetization
magnetization = 1.0

# Define the grid for the magnetic field and potential calculations
x = np.linspace(-15, 15, 100)
y = np.linspace(-15, 15, 100)
X, Y = np.meshgrid(x, y)

# Initialize the magnetic field and potential arrays
Bx = np.zeros_like(X)
By = np.zeros_like(Y)
V = np.zeros_like(X)
