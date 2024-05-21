import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Read the DataFrame from a CSV file
df = pd.read_csv('sim_results.csv')

# Display the DataFrame to ensure it has been read correctly
print(df.head())

# Filter the DataFrame to include only rows where numAllPass is 3
filtered_df = df[df['numAllPass'] == 3]

# Display the filtered DataFrame to ensure filtering is correct
print(filtered_df.head())

# Extract the columns for the x and y axes
x = filtered_df['numSecurity']
y = filtered_df['avg_time']

# Define the function to fit
def func(x, a, b):
    return a + b / x

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
plt.plot(x_fit, y_fit, color='blue', label=f'Fitted Function: $a + \\frac{{b}}{{x}}$\n$a = {a:.3f}$, $b = {b:.3f}$')

# Add labels and title
plt.xlabel('Number of Security')
plt.ylabel('Average Max Time-to-gate')
plt.title('Average Max Time-to-gate as a Function of Number of Security (numAllPass = 3, passengers=200)')
plt.legend()

# Show plot
plt.show()

