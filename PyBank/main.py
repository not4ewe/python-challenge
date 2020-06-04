# Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

import os
import csv

budget_csv=os.path.join("Resources","budget_data.csv")

#create lists for data
profit = []
monthly_change = []
date = []

#variables
month_count = 0
total_profit = 0
initial_profit = 0


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    #read each row
    for row in csvreader:
        month_count = month_count +1
        total_profit = total_profit + int(row[1])

        date.append(row[0])
        profit.append(row[1])

        monthly_change_profits = int(row[1]) - initial_profit
        monthly_change.append(monthly_change_profits)
        initial_profit = int(row[1])


        average_change_profits = (monthly_change_profits/month_count)

        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)

        increase_date= date[monthly_change.index(greatest_increase_profits)]
        decrease_date =date[monthly_change.index(greatest_decrease_profits)]

    print("----------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------")
    print("Total Months: " + str(month_count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")


    #txt_file.write("----------------------------------------")
    #txt_file.write("Financial Analysis")
    #txt_file.write("----------------------------------------")
    #txt_file.write("Total Months: " + str(month_count))
    #txt_file.write("Total Profits: " + "$" + str(total_profit))
    #txt_file.write("Average Change: " + "$" + str(int(average_change_profits)))
    #txt_file.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    #txt_file.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")