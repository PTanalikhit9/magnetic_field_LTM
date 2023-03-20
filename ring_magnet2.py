
import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the circular ring magnet
outer_radius = 5.0
inner_radius = 4.0
height = 4.0

# Define the strength of the magnetization
magnetization = 1.0

# Define the grid for the magnetic field and potential calculations
x = np.linspace(-15, 15, 100)
z = np.linspace(-15, 15, 100)
X, Z = np.meshgrid(x, z)
