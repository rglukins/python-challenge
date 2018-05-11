#import dependencies
import os
import csv

#create path object
file = "budget_data_2.csv"

#create variables to store the necessary information
list_months = []
total_revenue = 0
revenue_list = []
monthly_changes = []
monthly_increases = []
total_monthly_rev_change = 0

#create reader object for csv file to loop through data and compile lists
with open(file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for (row) in reader:
        current_month = row["Date"]
        current_revenue = int(row["Revenue"])
        list_months.append(current_month)
        revenue_list.append(current_revenue)
        total_revenue = total_revenue + current_revenue

#create list variable and loop for calculating and storing the increases and decreases
for i in range(0, len(revenue_list)-1):
    month_change = revenue_list[i+1] - revenue_list[i]
    monthly_changes.append(month_change)
    total_monthly_rev_change= total_monthly_rev_change + month_change
    
#print analysis to terminal
print("Financial Analysis")
print("------------------")
print(f'Total Months: {len(list_months)}')
print(f"Total Revenue: {total_revenue}")
print(f'Average Revenue Change: {total_monthly_rev_change / len(monthly_changes)}')
print(f'Greatest Increase in Revenue:  {list_months[monthly_changes.index(max(monthly_changes)) + 1]} {max(monthly_changes)}')
print(f'Greatest Decrease in Revenue: {list_months[monthly_changes.index(min(monthly_changes)) + 1]}  {min(monthly_changes)}')

#write analysis results to a txt file
bank_file = open("pyBank_results.txt", "w")
bank_file.write("Financial Analysis\n")
bank_file.write("---------------------\n")
bank_file.write(f'Total Months: {len(list_months)} \n')
bank_file.write(f"Total Revenue: {total_revenue} \n")
bank_file.write(f'Average Revenue Change: {total_monthly_rev_change / len(monthly_changes)}\n')
bank_file.write(f'Greatest Increase in Revenue:  {list_months[monthly_changes.index(max(monthly_changes)) + 1]} {max(monthly_changes)} \n')
bank_file.write(f'Greatest Decrease in Revenue: {list_months[monthly_changes.index(min(monthly_changes)) + 1]}  {min(monthly_changes)} \n')

