#Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

election_csv=os.path.join("Resources","election_data.csv")

#variable
votes = []
candidates = []
khan = []
correy = []
li = []
otooley = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header row first
    csv_header = next(csvfile)
    
    #read each row
    for row in csvreader:
        votes.append(int(row[0]))
        # A complete list of candidates who received votes
        candidates.append(row[2])

    # The total number of votes cast
    total_votes = (len(votes))
    
    # The total number of votes each candidate won
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)    
    
    # The percentage of votes each candidate won
    khan_percent = round(((khan_votes / total_votes) * 100), 3)
    correy_percent = round(((correy_votes / total_votes) * 100), 3)
    li_percent = round(((li_votes / total_votes) * 100), 3)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 3)
    
    # The winner of the election based on popular vote.
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

#Print Results
print(f"Election Results") 
print(f"-----------------------------------") 
print(f"Total Votes: {total_votes}") 
print("-----------------------------------") 
print(f"Khan: {khan_percent}% ({khan_votes})") 
print(f"Correy: {correy_percent}% ({correy_votes})") 
print(f"Li: {li_percent}% ({li_votes})") 
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})") 
print(f"-----------------------------------") 
print(f"Winner: {winner}") 
print(f"-----------------------------------")

#Export Results
output_file = os.path.join("Analysis","election_results.txt")
with open(output_file, 'w') as text:

    text.write(f"Election Results" + "\n") 
    text.write(f"-----------------------------------\n") 
    text.write(f"Total Votes: {total_votes}"+ "\n") 
    text.write(f"-----------------------------------\n") 
    text.write(f"Khan: {khan_percent}% ({khan_votes})"+ "\n") 
    text.write(f"Correy: {correy_percent}% ({correy_votes})"+ "\n") 
    text.write(f"Li: {li_percent}% ({li_votes})"+ "\n") 
    text.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})"+ "\n") 
    text.write(f"-----------------------------------\n") 
    text.write(f"Winner: {winner}"+ "\n") 
    text.write(f"-----------------------------------")