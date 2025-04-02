# Python codes for handling of data
updated: 01.04.2025

'Merge_PQ.py' merges 2 csv files of same name and similar format to give one final csv file with both P and Q values together.

# python code for GUI
updated: 01.04.2025

GUI implementaion in python similar to the one in MATlab for load sensitivity analysis.
- Check if the folder selected has CSV file.
- Load it all and use the filename as identifier.
- Check the second row (index 1) and replace NaN with 0
- Replace NaN with the previous value in the same column
- Function to open the second window based on the number of devices chosen.
- Function to calculate the end time based on start time and length of the column
- Create the dropdown and textboxes dynamically based on device count, start and calaulate end time.
 
Todo:
    - Use start time and loaded data to generate plot and save it locally.
    - Reactive Load Profile Plot, Aggregated Active and Reactive  Load Sensitivity Plot.