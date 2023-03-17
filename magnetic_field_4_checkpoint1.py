
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
        # Distances from the charges
        dz_north = z[j] + height / 2
        dz_south = z[j] - height / 2

        # Magnetic field components
        Bx[i, j] = 0
        Bz[i, j] = magnetization * (dz_north / (x[i] ** 2 + dz_north ** 2) - dz_south / (x[i] ** 2 + dz_south ** 2))

        # Magnetic potential
        V[i, j] = magnetization * (np.log(np.sqrt(x[i] ** 2 + dz_north ** 2)) - np.log(np.sqrt(x[i] ** 2 + dz_south ** 2)))

# Create the plot
fig, ax = plt.subplots()

# Plot the magnetic potential as a colormap
c = ax.pcolormesh(Z, X, V, cmap='coolwarm', shading='auto')
fig.colorbar(c, ax=ax, label='Magnetic Potential')

# Plot the magnetic field as small arrows
# Use a stride to reduce arrow density
stride = 1
ax.quiver(X[::stride, ::stride], Z[::stride, ::stride], Bx[::stride, ::stride], Bz[::stride, ::stride], color='k', minlength=0.1, pivot='middle', scale=40)

# Draw the magnet's boundary
magnet_boundary = plt.Rectangle((-length/5, -height/5), length/2.5, height/2.5, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(magnet_boundary)

# Set plot labels
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('Side View of Magnetic Field and Potential of a Rectangular Magnet')

# Show the plot
plt.show()
