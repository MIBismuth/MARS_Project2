import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sim_results_schengen.csv")

# Splitting the DataFrame based on the schengen column
df_schengen_1 = df[df['schengen'] == 1]
df_schengen_0 = df[df['schengen'] == 0]

# Plotting avg_time as a function of passengers_num for schengen 1 and schengen 0
plt.figure(figsize=(10, 6))
plt.plot(df_schengen_1['passengers_num'], df_schengen_1['avg_time'], marker='o', linestyle='-', label='Schengen 1')
plt.plot(df_schengen_0['passengers_num'], df_schengen_0['avg_time'], marker='o', linestyle='-', label='Schengen 0')
plt.xlabel('Number of Passengers')
plt.ylabel('Average Time')
plt.title('Average Time as a Function of Number of Passengers for Schengen 1 and Schengen 0')
plt.legend()
plt.grid(True)
plt.show()

