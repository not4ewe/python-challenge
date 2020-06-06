

import os
import csv

election_csv=os.path.join("Resources","election_data.csv")

#variable
total_votes = 0
candidates_list = []
candidate_votes = {}
winning_count = 0
winning_candidate = ""

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    #read each row
    for row in csvreader:
        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates_list:

            # Add it to list of candidates in the running
            candidates_list.append(candidate_name)

            # Start tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#print("total_votes:" (total_votes)")





    #print("Financial Analysis")
   # print("----------------------------------------")
   # print("Total Months: " + str(month_count))
   # print("Total Profits: " + "$" + str(total_profit))
   # print("Average Change: " + "$" + str(int(average_change_profits)))
   # print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
   # print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")


    #txt_file.write("----------------------------------------")
    #txt_file.write("Financial Analysis")
    #txt_file.write("----------------------------------------")
    #txt_file.write("Total Months: " + str(month_count))
    #txt_file.write("Total Profits: " + "$" + str(total_profit))
    #txt_file.write("Average Change: " + "$" + str(int(average_change_profits)))
    #txt_file.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    #txt_file.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")