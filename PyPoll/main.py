import csv

csvfile = "C:/Users/Student/OneDrive/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(csvfile, 'r') as file:
    csvreader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment total number of votes
        total_votes += 1
        
        # Count votes for each candidate
        candidate_name = row['Candidate']
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
            
        # Update winner
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Output the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Write results to a text file
with open("electionoutput.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner['name']}\n")
    file.write("-------------------------\n")
