
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
            charge_x_north = outer_radius * np.sin(angle) + height / 2
            charge_x_south = outer_radius * np.sin(angle) - height / 2
            charge_z = outer_radius * np.cos(angle)

            # Calculate the distances from the charges
            dx_north = x[i] - charge_x_north
            dx_south = x[i] - charge_x_south
            dz = z[j] - charge_z

            # Magnetic field components
            Bx[i, j] += magnetization / num_charges * (dz / (dx_north ** 2 + dz ** 2) - dz / (dx_south ** 2 + dz ** 2))
            Bz[i, j] += magnetization / num_charges * (dx_north / (dx_north ** 2 + dz ** 2) - dx_south / (dx_south ** 2 + dz ** 2))

            # Magnetic potential
            V[i, j] += magnetization / num_charges * (np.log(np.sqrt(dx_north ** 2 + dz ** 2)) - np.log(np.sqrt(dx_south ** 2 + dz ** 2)))

  
# Create the plot
fig, ax = plt.subplots()

# Plot the magnetic potential as a colormap
c = ax.pcolormesh(X, -Z, V, cmap='coolwarm', shading='auto')
fig.colorbar(c, ax=ax, label='Magnetic Potential')

# Plot the magnetic field as small arrows
# Use a stride to reduce arrow density
stride = 2
ax.quiver(X[::stride, ::stride], Z[::stride, ::stride], Bx[::stride, ::stride], Bz[::stride, ::stride], color='k', minlength=0.5, pivot='middle', scale=10)

# Draw the magnet's boundary
# magnet_boundary_north = plt.Rectangle((-outer_radius, height / 2), 2 * outer_radius, outer_radius - inner_radius, linewidth=1, edgecolor='r', facecolor='none')
# magnet_boundary_south = plt.Rectangle((-outer_radius, -height / 2 - (outer_radius - inner_radius)), 2 * outer_radius, outer_radius - inner_radius, linewidth=1, edgecolor='r', facecolor='none')
# ax.add_patch(magnet_boundary_north)
# ax.add_patch(magnet_boundary_south)

# Draw the magnet's boundary
magnet_boundary1 = plt.Rectangle((-outer_radius, -height / 2), (outer_radius - inner_radius), height, linewidth=1, edgecolor='k', facecolor='none')
ax.add_patch(magnet_boundary1)
magnet_boundary2 = plt.Rectangle((inner_radius, -height / 2), (outer_radius - inner_radius), height, linewidth=1, edgecolor='k', facecolor='none')
ax.add_patch(magnet_boundary2)

# Set plot labels
ax.set_xlabel('z')
ax.set_ylabel('x')
ax.set_title('Side View of Magnetic Field and Potential of a Circular Ring Magnet')

# Show the plot
plt.show()
