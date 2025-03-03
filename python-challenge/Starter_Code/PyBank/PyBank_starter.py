# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
average_change_profit =0
great_incre_profit = 0
great_decre_profit =0 
great_incre_dates = float('-inf')
great_decre_dates = float('inf')
previous_profit = None


#  variables to track other necessary financial data

date_list = []
net_change_list = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit = int(first_row[1])
    current_profit = int(first_row[1])
    total_net += current_profit  
   
    # Track the dates
    date_list.append(first_row[0]) 
    


    # Track the total and net change
    net_change = current_profit - previous_profit
    net_change_list.append(net_change)
    previous_profit = current_profit

    # Process each row of data
    for row in reader:
    # Track the total (the code below was added by coplit when correcting an error in the code)
        total_months += 1
    current_profit = int(row[1]) 
    total_net += current_profit

    # Track the net change
    # used the net_change variable to calculate the net change
    net_change = current_profit - previous_profit
    net_change_list.append(net_change)
    previous_profit = current_profit

    # Calculate the greatest increase in profits (month and amount)
    # used if statement to compare the net_change to the great_incre_profit
    if net_change > great_incre_profit:
        great_incre_profit = net_change
        great_incre_month = row[0] 

    # Calculate the greatest decrease in losses (month and amount)
    # used if statement to compare the net_change to the great_decre_profit
    if net_change < great_decre_profit:
        great_decre_profit = net_change
        great_decre_month = row[0]

    # end of the code added by coplit

# Calculate the average net change across the months
average_change_profit = sum(net_change_list) / len(net_change_list)
# Generate the output summary
# used the f-string to format the output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change_profit:.2f}\n"
    f"Greatest Increase in Profits: {great_incre_dates} (${great_incre_profit})\n"
    f"Greatest Decrease in Profits: {great_decre_dates} (${great_decre_profit})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
