
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

# Calculate the magnetic field and potential at each grid point
for i in range(len(x)):
    for j in range(len(y)):
        # Distances from the corners of the magnet
        dx1 = x[i] + length / 2
        dy1 = y[j] + width / 2
        dx2 = x[i] - length / 2
        dy2 = y[j] + width / 2
        dx3 = x[i] - length / 2
        dy3 = y[j] - width / 2
        dx4 = x[i] + length / 2
        dy4 = y[j] - width / 2

        # Magnetic field components
        Bx[i, j] = magnetization * (np.arctan(dy1 * dx1 / (dx1 ** 2 + dy1 ** 2)) -
                                    np.arctan(dy2 * dx2 / (dx2 ** 2 + dy2 ** 2)) +
                                    np.arctan(dy3 * dx3 / (dx3 ** 2 + dy3 ** 2)) -
                                    np.arctan(dy4 * dx4 / (dx4 ** 2 + dy4 ** 2)))
        By[i, j] = magnetization * (np.arctan(dy1 / dx1) - np.arctan(dy2 / dx2) +
                                    np.arctan(dy3 / dx3) - np.arctan(dy4 / dx4))

        # Magnetic potential
        V[i, j] = magnetization * (np.log(np.sqrt(dx1 ** 2 + dy1 ** 2)) -
                                   np.log(np.sqrt(dx2 ** 2 + dy2 ** 2)) +
                                   np.log(np.sqrt(dx3 ** 2 + dy3 ** 2)) -
                                   np.log(np.sqrt(dx4 ** 2 + dy4 ** 2)))

# Create the plot
fig, ax = plt.subplots()

# Plot the magnetic potential as a colormap
c = ax.pcolormesh(X, Y, V, cmap='coolwarm', shading='auto')
fig.colorbar(c, ax=ax, label='Magnetic Potential')

# Plot the magnetic field as small arrows
ax.quiver(X, Y, Bx, By, color='k', minlength=0.1, pivot='middle', scale=40)

# Set plot labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Magnetic Field and Potential of a Rectangular Magnet')

plt.show()

