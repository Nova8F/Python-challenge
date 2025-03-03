# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
data = file_to_load
# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast


Ballot_id=0

County=0 

Candidate=0
 
Candidate_votes=0

# Define lists and dictionaries to track candidate names and vote counts
total_votes= []
Candidate= []
Candidate_votes = {}
Candidate_percentages = {}  

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        # there is a issue with the code total_votes += 1 its not iterable. need ti fix it
        total_votes += 1
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in Candidate:
            Candidate.append(candidate_name)
            Candidate_votes[candidate_name] = 0
            Candidate_percentages[candidate_name] = 0

        # Add a vote to the candidate's count
    Candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name, votes in Candidate_votes.items():

        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        print(f"{candidate_name}: {vote_percentage:.2f}% ({votes})")
        txt_file.write(f"{candidate_name}: {vote_percentage:.2f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print(f"Winner: {winning_candidate}")
    print(f"Winning Vote Count: {winning_count}")

    # Save the winning candidate summary to the text file
    txt_file.write(f"\nWinner: {winning_candidate}\n")
    txt_file.write(f"Winning Vote Count: {winning_count}\n")