import csv

# Initialize variables
total_votes = 0
candidates = {}

# Read the csv file
with open('PyPoll/Resources/election.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        # Update total votes
        total_votes += 1

        # Update candidate votes
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate vote percentages and find the winner
winner = max(candidates, key=candidates.get)
for candidate in candidates:
    percentage = (candidates[candidate] / total_votes) * 100
    candidates[candidate] = [percentage, candidates[candidate]]

# Prepare the analysis
analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, data in candidates.items():
    analysis += f"{candidate}: {data[0]:.3f}% ({data[1]})\n"
analysis += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)


# Print the analysis
print(analysis)

# Output analysis to text file
with open('Pypoll/analysis/output.txt', 'w') as file:
    file.write(analysis)