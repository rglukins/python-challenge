import os
import csv
import string

#create variable for the path to the csv doc
file_path = os.path.join(".","election_data_1.csv")

#create variables for analyzing the data
total_votes = 0
candidates = []

#create an object that reads the doc
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #Write code to calculate the number of votes cast
    for voter in reader:
       total_votes = total_votes +1
#print(total_votes)

canditate_info = csv.DictReader(open(file_path, 'r'))   #create an object the reads the election data
for (row) in canditate_info:         #identify the candidates who received votes
    can_name = row["Candidate"]
    if not can_name in candidates:
        candidates.append(can_name)
print(candidates)

votes_4_c = []
vote_counter = 0

#print(votes_per_c)

for i in range(0, len(candidates)):
    vote_counter = 0
    canditate_info = csv.DictReader(open(file_path, 'r'))
    for (row) in canditate_info:
        if row["Candidate"] == candidates[i]:
            vote_counter = vote_counter +1
        else:
            next
    votes_4_c.append(str(vote_counter))

print(votes_4_c)


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

#find winner



#Write results to to text file
election_results_file = open("election_results.txt", "w")
election_results_file.write("Elections Results\n")
election_results_file.write("___________________\n")
election_results_file.write(f'Total Votes: {total_votes}\n')
election_results_file.write("___________________\n")
for i in range(0, len(election_results)):
    #print(election_results[i])
    text = str(election_results[i])
    cleaned_text= text.strip(string.punctuation)
    election_results_file.write(cleaned_text +'\n')
election_results_file.write("___________________\n")
