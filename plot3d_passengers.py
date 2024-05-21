import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.interpolate import griddata

# Read the DataFrame from a CSV file
df = pd.read_csv('sim_results_passengers.csv')

# Display the DataFrame to ensure it has been read correctly
print(df.head())

# Extract the columns for the x, y, and z axes
x = df['numSecurity']
y = df['passengers_num']
z = df['avg_time']

# Create a grid of values
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolate the z values on the grid
zi = griddata((x, y), z, (xi, yi), method='linear')

# Create the figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(xi, yi, zi, cmap='viridis', alpha=0.8)

# Plot the actual data points as red dots
ax.scatter(x, y, z, c='r', marker='o')

# Add a color bar which maps values to colors
fig.colorbar(surf)

# Set labels
ax.set_xlabel('Number of Security')
ax.set_ylabel('Number of Passengers')
ax.set_zlabel('Average Max Time')

# Show plot
plt.show()


