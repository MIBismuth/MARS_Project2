import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

numS = 3
# Read the DataFrame from a CSV file
df = pd.read_csv('sim_results_passengers.csv')

# Filter the DataFrame to include only rows where numAllPass = 3
df_filtered = df[df['numSecurity'] == numS]

# Display the filtered DataFrame to ensure it has been filtered correctly
print(df_filtered.head())

# Extract the columns for the x and y axes
x = df_filtered['passengers_num']
y = df_filtered['avg_time']

# Define the function to fit
def func(x, a, b):
    return a*x + b

# Perform the curve fitting
popt, pcov = curve_fit(func, x, y)

# Extract the fitting parameters
a, b = popt
print(f"Fitted parameters: a = {a}, b = {b}")

# Generate x values for the fitted function
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = func(x_fit, a, b)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label=f'Fitted Function: $a*x + b$\n$a = {a:.3f}$, $b = {b:.3f}$')

# Add labels and title
plt.xlabel('Number of Passengers')
plt.ylabel('Average Max Time')
plt.title(f'Average Max Time as a Function of Number of Passengers (numSecurity={numS}, numAllPass = 3)')
plt.legend()

# Show plot
plt.show()

