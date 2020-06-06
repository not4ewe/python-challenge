

import os
import csv

election_csv=os.path.join("Resources","election_data.csv")

#variable
votes = []
    #county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    #read each row
    for row in csvreader:
        votes.append(int(row[0]))
        #county.append(row[1])
        candidates.append(row[2])

    #VOTE COUNT
    total_votes = (len(votes))
    #print(total_votes)

    #Votes by Person
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
    #print(khan_votes)
    #print(correy_votes)
    #print(li_votes)
    #print(otooley_votes)
    
    
    #Percentages
    khan_percent = round(((khan_votes / total_votes) * 100), 3)
    correy_percent = round(((correy_votes / total_votes) * 100), 3)
    li_percent = round(((li_votes / total_votes) * 100), 3)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 3)
    #print(khan_percent)
    #print(correy_percent)
    #print(li_percent)
    #print(otooley_percent)
    
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

        #Print Statements

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