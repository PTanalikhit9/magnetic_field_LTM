
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

# Initialize the magnetic field and potential arrays
Bx = np.zeros_like(X)
Bz = np.zeros_like(Z)
V = np.zeros_like(X)

# Number of charges on the magnet's surface
num_charges = 1000

# Calculate the magnetic field and potential at each grid point
for i in range(len(x)):
    for j in range(len(z)):
        for k in range(num_charges):
            # Calculate the angle of the charges
            angle = k * 2 * np.pi / num_charges

            # Calculate the position of the charges
            charge_x = outer_radius * np.cos(angle)
            charge_z_north = outer_radius * np.sin(angle) + height / 2
            charge_z_south = outer_radius * np.sin(angle) - height / 2

            # Calculate the distances from the charges
            dx = x[i] - charge_x
            dz_north = z[j] - charge_z_north
            dz_south = z[j] - charge_z_south

            # Magnetic field components
            Bx[i, j] += magnetization / num_charges * (dz_south / (dx ** 2 + dz_south ** 2) - dz_north / (dx ** 2 + dz_north ** 2))
            Bz[i, j] += magnetization / num_charges * (dx / (dx ** 2 + dz_south ** 2) - dx / (dx ** 2 + dz_north ** 2))

            # Magnetic potential
            V[i, j] += magnetization / num_charges * (np.log(np.sqrt(dx ** 2 + dz_south ** 2)) - np.log(np.sqrt(dx ** 2 + dz_north ** 2)))

