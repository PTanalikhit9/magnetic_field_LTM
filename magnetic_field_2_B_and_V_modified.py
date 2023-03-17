
import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the rectangular magnet
length = 10.0
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

# Calculate the magnetic field and potential at each grid point
for i in range(len(x)):
    for j in range(len(z)):
        # Distances from the corners of the magnet
        dx1 = x[i] + length / 2
        dz1 = z[j] + height / 2
        dx2 = x[i] - length / 2
        dz2 = z[j] + height / 2
        dx3 = x[i] - length / 2
        dz3 = z[j] - height / 2
        dx4 = x[i] + length / 2
        dz4 = z[j] - height / 2

        # Magnetic field components
        Bx[i, j] = magnetization * (np.arctan(dz1 * dx1 / (dx1 ** 2 + dz1 ** 2)) -
                                    np.arctan(dz2 * dx2 / (dx2 ** 2 + dz2 ** 2)) +
                                    np.arctan(dz3 * dx3 / (dx3 ** 2 + dz3 ** 2)) -
                                    np.arctan(dz4 * dx4 / (dx4 ** 2 + dz4 ** 2)))
        Bz[i, j] = magnetization * (np.arctan(dz1 / dx1) - np.arctan(dz2 / dx2) +
                                    np.arctan(dz3 / dx3) - np.arctan(dz4 / dx4))

        # Magnetic potential
        V[i, j] = magnetization * (np.log(np.sqrt(dx1 ** 2 + dz1 ** 2)) -
                                   np.log(np.sqrt(dx2 ** 2 + dz2 ** 2)) +
                                   np.log(np.sqrt(dx3 ** 2 + dz3 ** 2)) -
                                   np.log(np.sqrt(dx4 ** 2 + dz4 ** 2)))

# Create the plot
fig, ax = plt.subplots()

# Plot the magnetic potential as a colormap
c = ax.pcolormesh(X, Z, V, cmap='coolwarm', shading='auto')
fig.colorbar(c, ax=ax, label='Magnetic Potential')

# Plot the magnetic field as small arrows
ax.quiver(X, Z, Bx, Bz, color='k', minlength=0.1, pivot='middle', scale=40)

# Set plot labels
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('Side View of Magnetic Field and Potential of a Rectangular Magnet')

plt.show()
