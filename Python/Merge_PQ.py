# author : abijoor
# To merge differnt P and Q values of loads measured in EnergyLab2.0
import pandas as pd
import glob
import os


print("Info: starting.")
# Specify the folder containing the CSV files
folder_path = 'C:/Users/yb3247/Downloads/GitData'  # your folder path

# Get a list of all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
print("Info: read csv.")

# Ensure there are at least two CSV files to process
if len(csv_files) < 2:
    print("Error: Not enough CSV files in the folder to merge.")
else:
    # Select the first two CSV files
    file1, file2 = csv_files[0], csv_files[1]

    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Select only the first three columns of the first CSV and specific columns from the second CSV
    df1_selected = df1.iloc[:, 0:3]  # First 3 columns from df1
    df2_selected = df2.iloc[:, 1:4]  # Columns 2-4 from df2

    # Check if both files have the same number of rows before merging
    if len(df1_selected) == len(df2_selected):
        # Concatenate the columns of df1 with the selected columns of df2
        merged_df = pd.concat([df1_selected, df2_selected], axis=1)

        # Generate a name for the merged output file
        file1_name = os.path.splitext(os.path.basename(file1))[0]
        file2_name = os.path.splitext(os.path.basename(file2))[0]
        merged_filename = os.path.join(folder_path, f"merged_{file1_name}_{file2_name}.csv")

        # Save the merged result to the new CSV file
        merged_df.to_csv(merged_filename, index=False)
        print(f"Files merged successfully with 7 columns. Saved as '{merged_filename}'.")
    else:
        print("Error: The two CSV files have a different number of rows and cannot be merged directly.")
