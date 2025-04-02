# author: abijoor
# Effort to move gui code from matlab to python
# 
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime, timedelta
import os
import pandas as pd
from scipy.io import loadmat

# Define the folder path containing CSV files
folder_path = "C:/Users/yb3247/Documents/GitHub/ITEP_load_repo/Sensitivity Dataset/csv"  # Replace with your folder path

# Initialize an empty dictionary to store DataFrames
csv_data = {}
devices = {}

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):  # Check if the file is a CSV
        file_path = os.path.join(folder_path, file_name)
        
        # Load the CSV into a DataFrame and save it into the dictionary
        csv_data[file_name] = pd.read_csv(file_path)
        # Add the device list to the dictionary using file_name as the key
        devices[os.path.splitext(file_name)[0]] = os.path.splitext(file_name)[0]

device_list = list(devices)
# print(f"all files=  '{device_list}' ")

print(f"Loaded {len(csv_data)} CSV files.")

nan2zero = True  # or False, depending on the condition
for file_name, df in csv_data.items():
    # Check the second row (index 1) and replace NaN with 0
    df.iloc[1] = df.iloc[1].fillna(0)  # Replace NaN with 0 in the second row only

    if nan2zero:
        # Replace NaN with 0 in the DataFrame
        df.fillna(0, inplace=True)
    else:
        # Replace NaN with the previous value in the same column
        df.fillna(method='ffill', inplace=True)

    column_length = len(df['time_s']) -1  #multiply with 15 to get total time in sec.
   # print(f"Processed '{file_name}' , length = '{column_length}'")
   # print(df.head())  # Print the first few rows to verify
    # df.to_csv(f"modified_{file_name}", index=False)  # Saves with a prefix "modified_"

def convert_to_seconds(time_str):
    # Split the input string by ':'
    hours, minutes = map(int, time_str.split(":"))
    
    # Convert hours and minutes to seconds
    total_seconds = (hours * 3600) + (minutes * 60)
    
    return total_seconds

def convert_seconds_to_hm(seconds):
    # Ensure hours do not exceed 24
    hours = (seconds // 3600) % 24  # Convert to hours and limit to 24 hours
    minutes = (seconds % 3600) // 60  # Get the remaining minutes
    
    # Format as hh:mm with leading zero if necessary
    return f"{hours:02}:{minutes:02}"


# Function to calculate the end time based on start time and length of the column
def calculate_end_time(start_time, device_chosen):
    try:
        # Convert start time to datetime object
        start_time_s = convert_to_seconds(start_time)
        
        device_file = csv_data[device_chosen]
        # Calculate end time (start time + (length - 1) * 15 minutes)
        end_time_s = start_time_s + (len(device_file['time_s'])-1)*15
        
        # Convert back to hh:mm format
        end_time = convert_seconds_to_hm(end_time_s)
        return end_time
    except ValueError:
        return "Invalid time"

def device_picker():
    return

# Function to open the second window based on the number of devices
def open_second_window(device_count):
    # Create a new window
    second_window = tk.Toplevel(root)
    second_window.title("Device Setup")
    
    # Create the dropdown and textboxes dynamically based on device count
    for i in range(device_count):
        # Row frame
        row_frame = tk.Frame(second_window)
        row_frame.grid(row=i, padx=10, pady=5)

        # Dropdown for device selection
        device_label = tk.Label(row_frame, text=f"Device {i + 1}:")
        device_label.grid(row=i, column=0)

        device_dropdown = ttk.Combobox(row_frame, values=device_list)
        device_dropdown.grid(row=i, column=1)

        # Textbox for start time
        start_time_label = tk.Label(row_frame, text="Start Time (hh:mm):")
        start_time_label.grid(row=i, column=2)

        start_time_entry = tk.Entry(row_frame)
        start_time_entry.grid(row=i, column=3)
        
        # Display end time
        end_time_label = tk.Label(row_frame, text="End Time:")
        end_time_label.grid(row=i, column=4)

        # Function to calculate end time when start time changes
        def on_start_time_change(event, start_time_entry=start_time_entry):
            start_time = start_time_entry.get()
            print(f"device selected = '{device_dropdown.get()}")
            end_time = calculate_end_time(start_time, device_dropdown.get())
            end_time_label.config(text=f"End Time: {end_time}")
            end_time_label.grid(row=i, column=5)

        start_time_entry.bind("<FocusOut>", on_start_time_change)
        

    # Button to finalize the second window
    finalize_button = tk.Button(second_window, text="Finalize", command=second_window.destroy)
    finalize_button.grid(row=device_count, column=0, columnspan=5, pady=10)

# Function to handle first window selection
def open_first_window():
    # Create the first window
    first_window = tk.Toplevel(root)
    first_window.title("Device Selection")

    # Label for asking how many devices to use
    label = tk.Label(first_window, text="How many devices to use (1-10):")
    label.grid(row=0, column=0, padx=10, pady=10)

    # Dropdown to select number of devices
    device_count_var = tk.StringVar()
    device_count_dropdown = ttk.Combobox(first_window, textvariable=device_count_var, values=list(range(1, 11)))
    device_count_dropdown.grid(row=1, column=0, padx=10, pady=10)
    device_count_dropdown.set("1")  # Default to 1 device

    # Button to open the second window
    next_button = tk.Button(first_window, text="Next", command=lambda: open_second_window(int(device_count_var.get())))
    next_button.grid(row=2, column=0, pady=20)

# Create main Tkinter window
root = tk.Tk()
root.title("Device Setup")

# Button to open the first window
start_button = tk.Button(root, text="Start Setup", command=open_first_window)
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()












if 0:
    class MatProcessorApp:
        def __init__(self, root):
            self.root = root
            self.root.title("MAT Data Processor")

            # Step 1: Select .mat file
            self.select_file_label = tk.Label(root, text="Step 1: Select a .MAT file")
            self.select_file_label.pack(pady=5)

            self.filepath_entry = tk.Entry(root, width=50)
            self.filepath_entry.pack(pady=5)

            self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
            self.browse_button.pack(pady=5)

            self.next_button1 = tk.Button(root, text="Next", state=tk.DISABLED, command=self.device_selection_window)
            self.next_button1.pack(pady=20)

            self.mat_data = None

        def browse_file(self):
            filepath = filedialog.askopenfilename(filetypes=[("MATLAB Files", "*.mat")])
            if filepath:
                self.filepath_entry.delete(0, tk.END)
                self.filepath_entry.insert(0, filepath)
                try:
                    # Load the .mat file
                    self.mat_data = loadmat(filepath)
                    messagebox.showinfo("Success", ".MAT file loaded successfully!")
                    self.next_button1.config(state=tk.NORMAL)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to load .MAT file: {e}")

        def device_selection_window(self):
            self.new_window = tk.Toplevel(self.root)
            self.new_window.title("Step 2: Device Selection")

            tk.Label(self.new_window, text="Select the number of devices:").pack(pady=5)

            # Dropdown (combobox) for selecting the number of devices
            self.device_count_var = tk.StringVar()
            self.device_count_dropdown = ttk.Combobox(
                self.new_window, textvariable=self.device_count_var, state="readonly"
            )
            self.device_count_dropdown['values'] = list(range(1, 11))  # Numbers 1 to 10
            self.device_count_dropdown.pack(pady=5)
            self.device_count_dropdown.current(0)  # Set default value to 1

            self.next_button2 = tk.Button(self.new_window, text="Next", command=self.time_selection_window)
            self.next_button2.pack(pady=20)

        def time_selection_window(self):
            try:
                # Retrieve the selected number of devices
                device_count = int(self.device_count_var.get())
                self.new_window.destroy()  # Close the device selection window

                # Open the time selection window
                time_window = tk.Toplevel(self.root)
                time_window.title("Step 3: Time Selection")

                tk.Label(time_window, text=f"Selected Number of Devices: {device_count}").grid(row=0, column=0, columnspan=2, pady=5)

                # Validate if the .mat file has relevant data
                if not self.mat_data or "KITData_NaN2Prev" not in self.mat_data:
                    messagebox.showerror("Error", "'KITData_NaN2Prev' structure not found in the .MAT file.")
                    return

                # Extract device details from "KITData_NaN2Prev"
                kit_data = self.mat_data.KITData_NaN2Prev
                if isinstance(kit_data, dict):  # Check if it's a dictionary-like structure
                    device_details = list(kit_data.keys())
                else:
                    messagebox.showerror("Error", "'KITData_NaN2Prev' is not a valid structure.")
                    return

                if not device_details:
                    messagebox.showerror("Error", "No devices found in 'KITData_NaN2Prev'.")
                    return

                self.device_start_time_entries = []  # Store references to start time entries for each device
                self.device_end_time_labels = []  # Store references to end time labels for each device

                # Create columns for each device
                for i in range(device_count):
                    # Dropdown for device selection
                    tk.Label(time_window, text=f"Device {i + 1}:").grid(row=i + 1, column=0, sticky="e", padx=5, pady=5)
                    device_var = tk.StringVar()
                    device_dropdown = ttk.Combobox(
                        time_window, textvariable=device_var, values=device_details, state="readonly"
                    )
                    device_dropdown.grid(row=i + 1, column=1, padx=5, pady=5)
                    device_dropdown.current(0)  # Set default selection to the first device

                    # Start time entry
                    tk.Label(time_window, text="Start Time (HH:MM):").grid(row=i + 1, column=2, sticky="e", padx=5, pady=5)
                    start_time_entry = tk.Entry(time_window)
                    start_time_entry.grid(row=i + 1, column=3, padx=5, pady=5)
                    self.device_start_time_entries.append((device_var, start_time_entry))

                    # End time label (calculated automatically)
                    tk.Label(time_window, text="End Time:").grid(row=i + 1, column=4, sticky="e", padx=5, pady=5)
                    end_time_label = tk.Label(time_window, text="N/A")
                    end_time_label.grid(row=i + 1, column=5, padx=5, pady=5)
                    self.device_end_time_labels.append(end_time_label)

                # Submit button
                submit_button = tk.Button(time_window, text="Submit", command=self.process_data)
                submit_button.grid(row=device_count + 1, column=0, columnspan=6, pady=20)

            except ValueError as e:
                messagebox.showerror("Error", str(e))



        def process_data(self):
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get()

            # Placeholder: Add actual processing logic for .mat data if needed
            messagebox.showinfo(
                "Processing Summary",
                f"MAT file processed!\n\nStart Time: {start_time}\nEnd Time: {end_time}\nDevices Selected: {self.device_count_entry.get()}",
            )

    if __name__ == "__main__":
        root = tk.Tk()
        app = MatProcessorApp(root)
        root.mainloop()

