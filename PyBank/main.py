import csv

# Initialize variables
total_months = 0
net_total = 0
changes = []
prev_profit = None

# Open the CSV file
with open('PyBank/Resources/budget.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  
    first_row = next(csvreader)

    # Process each row
    for row in csvreader:
        date, profit = row
        profit = int(profit)

        # Update total months and net total
        total_months += 1
        net_total += profit

        # Calculate change from previous month
        if prev_profit is not None:
            change = profit - prev_profit
            changes.append(change)

        # Remember profit for next iteration
        prev_profit = profit

# Calculate average change and find greatest increase and decrease
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Prepare the analysis
analysis = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: ${greatest_increase}\n"
    f"Greatest Decrease in Profits: ${greatest_decrease}\n"
)


# Print analysis
print(analysis)


# Write the analysis to a text file 
with open('PyBank/analysis/output.txt', 'w') as file:
    file.write(analysis)




