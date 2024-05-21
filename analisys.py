from scipy import stats
import os
import pandas as pd
import statistics


def parser(file_path):

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if (i+1) % 5 == 0:
                yield float(line.strip().split(',')[0])

def process_csv_folder(folder_path):
    # Create an empty DataFrame to store the data
    df = pd.DataFrame(columns=['passengers_num', 'numSecurity', 'numAllPass', 'numShengen', 'max_time', 'avg_time'])

    # List all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for file_name in csv_files:
        # Extract values from file name
        print(file_name)
        file_parts = file_name.split('_')
        passengers_num = int(file_parts[0])
        numSecurity = int(file_parts[1])
        numAllPass = int(file_parts[2])
        numShengen = file_parts[3].split('.')[0]

        max_time = max([time for time in parser(f"{folder_path}/{file_name}")])
        avg_time = statistics.fmean([time for time in parser(f"{folder_path}/{file_name}")])

        # Append data to DataFrame
        df = df.append({'passengers_num': passengers_num,
                        'numSecurity': numSecurity,
                        'numAllPass': numAllPass,
                        'numShengen': numShengen,
                        'max_time': max_time,
                       'avg_time': avg_time,},
                       ignore_index=True)

    df = df.sort_values(by=['numSecurity', 'numAllPass', 'numShengen', 'passengers_num'])
    return df

def process_csv_folder_schengen(folder_path):
    # Create an empty DataFrame to store the data
    df = pd.DataFrame(columns=['passengers_num', 'numSecurity', 'numAllPass', 'numShengen', 'max_time', 'avg_time', 'schengen'])

    # List all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for file_name in csv_files:
        # Extract values from file name
        print(file_name)
        file_parts = file_name.split('_')
        passengers_num = int(file_parts[0])
        numSecurity = int(file_parts[1])
        numAllPass = int(file_parts[2])
        numShengen = file_parts[3].split('.')[0]
        schengen = file_parts[4].split('.')[0]

        max_time = max([time for time in parser(f"{folder_path}/{file_name}")])
        avg_time = statistics.fmean([time for time in parser(f"{folder_path}/{file_name}")])

        # Append data to DataFrame
        df = df.append({'passengers_num': passengers_num,
                        'numSecurity': numSecurity,
                        'numAllPass': numAllPass,
                        'numShengen': numShengen,
                        'max_time': max_time,
                       'avg_time': avg_time,
                        'schengen': schengen},
                       ignore_index=True)

    df = df.sort_values(by=['numSecurity', 'numAllPass', 'numShengen', 'passengers_num'])
    return df

#security simulations
folder_path = 'simulations_security'
result_df = process_csv_folder(folder_path)
output_file = 'sim_results.csv'
result_df.to_csv(output_file, index=False)
print(result_df)


folder_path = 'simulations_passengers'
result_df = process_csv_folder(folder_path)
output_file = 'sim_results_passengers.csv'
result_df.to_csv(output_file, index=False)
print(result_df)

folder_path = 'simulations_schengen'
result_df = process_csv_folder_schengen(folder_path)
output_file = 'sim_results_schengen.csv'
result_df.to_csv(output_file, index=False)
print(result_df)


