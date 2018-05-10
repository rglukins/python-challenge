import os
import csv

#create variable for the path to the csv doc
file_path = os.path.join(".","election_data_1.csv")

#create variables for analyzing the data
total_votes = 0
candidates = []

#create an object that reads the doc
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    #Write code to calculate the number of votes cast
    #for voter in reader:
     #   total_votes = total_votes +1
#print(total_votes)

canditate_info = csv.DictReader(open(file_path, 'r'))   #create an object the reads the election data
for (row) in canditate_info:         #identify the candidates who received votes
    can_name = row["Candidate"]
    if not can_name in candidates:
        candidates.append(can_name)
print(candidates)

votes_per_c = dict.fromkeys(candidates,0)
print(votes_per_c)
canditate_info = csv.DictReader(open(file_path, 'r'))
for (row) in canditate_info:
    if row["Candidate"] == 
            
