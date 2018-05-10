import os
import csv

#create variable for the path to the csv doc
file_path = os.path.join(".","election_data_1.csv")

#create variables for analyzing the data
total_votes = 0
candidates = []

#create an object that reads the doc
with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

#Write code to calculate the number of votes cast
    for voter in reader:
        total_votes = total_votes +1
print(total_votes)

canditate_info = csv.DictReader(open(file_path, 'r'))
for (row) in canditate_info:
    can_name = row["Candidate"]
    if not can_name in candidates:
        candidates.append(can_name)
print(candidates)

votes_4_c = []      #create variable to list the number of votes each candidate received. I know this is way easier with pandas, but I'm practicing loops and interations
vote_counter = 0    #create a variable to count the number in the loop
for i in range(0, len(candidates)): #create a loop analyze the csv file and count the number of votes received by each candidate
    vote_counter = 0
    canditate_info = csv.DictReader(open(file_path, 'r'))
    for (row) in canditate_info:
        if row["Candidate"] == candidates[i]:
            vote_counter = vote_counter +1
        else:
            next
    votes_4_c.append(str(vote_counter))

percent_votes = []
for i in range(0, len(candidates)):
    c_percent_v = (float(votes_4_c[i]) / float(total_votes)) * 100
    percent_votes.append(str(c_percent_v) +"%")
#print(percent_votes)

election_results = []
for i in range(0, len(candidates)):
    name = candidates[i]
    percent_received = percent_votes[i]
    votes_received = votes_4_c[i]
    election_results.append({
        "Candidate": name,
        "Percent of Vote": percent_received,
        "Total Votes Recieved": votes_received
    })
    #print(candidates[i], percent_votes[i], votes_4_c[i])
    print(election_results)