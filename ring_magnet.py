
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
            charge_x_outer = outer_radius * np.cos(angle)
            charge_z_outer_north = outer_radius * np.sin(angle) + height / 2
            charge_z_outer_south = outer_radius * np.sin(angle) - height / 2

            charge_x_inner = inner_radius * np.cos(angle)
            charge_z_inner_north = inner_radius * np.sin(angle) + height / 2
            charge_z_inner_south = inner_radius * np.sin(angle) - height / 2

            # Calculate the distances from the charges
            dx_outer = x[i] - charge_x_outer
            dz_outer_north = z[j] - charge_z_outer_north
            dz_outer_south = z[j] - charge_z_outer_south

            dx_inner = x[i] - charge_x_inner
            dz_inner_north = z[j] - charge_z_inner_north
            dz_inner_south = z[j] - charge_z_inner_south

            # Magnetic field components
            Bx[i, j] += magnetization / num_charges * (
                (dz_outer_south - dz_inner_south) / (dx_outer ** 2 + dz_outer_south ** 2) -
                (dz_outer_north - dz_inner_north) / (dx_outer ** 2 + dz_outer_north ** 2)
            )
            Bz[i, j] += magnetization / num_charges * (
                (dx_outer - dx_inner) / (dx_outer ** 2 + dz_outer_south ** 2) -
                (dx_outer - dx_inner) / (dx_outer ** 2 + dz_outer_north ** 2)
            )

            # Magnetic potential
            V[i, j] += magnetization / num_charges * (
                np.log(np.sqrt(dx_outer ** 2 + dz_outer_south ** 2)) -
                np.log(np.sqrt(dx_outer ** 2 + dz_outer_north ** 2))
            )

# Create the plot
fig, ax = plt.subplots()

# Plot the magnetic potential as a colormap
c = ax.pcolormesh(Z, X, V, cmap='coolwarm', shading='auto')
fig.colorbar(c, ax=ax, label='Magnetic Potential')

# Plot the magnetic field as small arrows
# Use a stride to reduce arrow density
stride = 2
ax.quiver(Z[::stride, ::stride], -X[::stride, ::stride], Bz[::stride, ::stride], -Bx[::stride, ::stride], color='k', minlength=0.5, pivot='middle', scale=10)

# Draw the magnet's boundary
magnet_outer_boundary = plt.Circle((0, 0), outer_radius, linewidth=1, edgecolor='r', facecolor='none')
magnet_inner_boundary = plt.Circle((0, 0), inner_radius, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(magnet_outer_boundary)
ax.add_patch(magnet_inner_boundary)

# Set plot labels
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('Side View of Magnetic Field and Potential of a Circular Ring Magnet')

# Set aspect ratio to 'equal' to preserve the shape of the magnet
ax.set_aspect('equal')

# Show the plot
plt.show()
