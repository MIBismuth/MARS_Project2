import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.interpolate import griddata
from scipy.optimize import curve_fit

# Read the DataFrame from a CSV file
df = pd.read_csv('sim_results_passengers.csv')

# Display the DataFrame to ensure it has been read correctly
print(df.head())

# Extract the columns for the x, y, and z axes
x = df['numSecurity'].values
y = df['passengers_num'].values
z = df['avg_time'].values

# Define the fitting function
def fitting_func(X, a, b, c):
    x, y = X
    return (a * y) / x + b * y + c 

# Initial guesses for the parameters
initial_guesses = [0, 40, 1]

# Perform the fit
popt, pcov = curve_fit(fitting_func, (x, y), z, p0=initial_guesses)

# Create a grid of values
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Generate the fitted surface
zi_fit = fitting_func((xi, yi), *popt)

# Interpolate the z values on the grid for the original data
zi = griddata((x, y), z, (xi, yi), method='linear')

# Create the figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original data surface (commented out for clarity)
# surf = ax.plot_surface(xi, yi, zi, cmap='viridis', alpha=0.5, label='Original Data')

# Plot the fitted surface
fit_surf = ax.plot_surface(xi, yi, zi_fit, cmap='plasma', alpha=0.5, label='Fitted Surface')

# Plot the actual data points as red dots
ax.scatter(x, y, z, c='r', marker='o', label='Data Points')

# Add a color bar which maps values to colors for the fitted surface
fig.colorbar(fit_surf, ax=ax, shrink=0.5, aspect=5)

# Set labels
ax.set_xlabel('Number of Security')
ax.set_ylabel('Number of Passengers')
ax.set_zlabel('Average Max Time')

# Add a title
ax.set_title('Average Max Time-to-Gate as a Function of Security and Passengers')

# Add the fitted expression and parameters as a label
fitted_expr = f"Fitted Expression: z = ({popt[0]:.2f}*y) / x + {popt[1]:.2f}*y + {popt[2]:.2f}"
ax.text2D(0.05, 0.95, fitted_expr, transform=ax.transAxes)

# Show plot
plt.show()

# Print the fitting parameters
print(f"Fitting parameters: a = {popt[0]}, b = {popt[1]}, c = {popt[2]}")

