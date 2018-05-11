import os
import csv

#create variable for the path to the csv doc
file_path = os.path.join(".","election_data_2.csv")

#create a variable for storing the total votes
total_votes = 0

#create an object that reads the doc
with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

#Write code to calculate the number of votes cast
    for voter in reader:
        total_votes = total_votes +1
print(total_votes)

#Find the number of unique vote-getters and create a list of candidates
candidates = []
canditate_info = csv.DictReader(open(file_path, 'r'))
for (row) in canditate_info:
    can_name = row["Candidate"]
    if not can_name in candidates:
        candidates.append(can_name)
print(candidates)

#loop through the csv file to count the total number of votes for each candidate
votes_4_candidate = []      #create variable to list the number of votes each candidate received. I know this is way easier with pandas, but I'm practicing loops and interations
vote_counter = 0    #create a variable to count the number in the loop
for i in range(0, len(candidates)): #create a loop analyze the csv file and count the number of votes received by each candidate
    vote_counter = 0
    canditate_info = csv.DictReader(open(file_path, 'r'))
    for (row) in canditate_info:
        if row["Candidate"] == candidates[i]:
            vote_counter = vote_counter +1
        else:
            next
    votes_4_candidate.append(vote_counter)
print(votes_4_candidate)

#calculate the percent of the vote that each candidate received
percent_votes = []
for i in range(0, len(candidates)):
    c_percent_v = (float(votes_4_candidate[i]) / float(total_votes)) * 100
    percent_votes.append(round(c_percent_v, 2))
print(percent_votes)

#find winner
winner = ()
for i in range(0, len(candidates)):
    if votes_4_candidate[i] == max(votes_4_candidate):
        winner = candidates[i]
print(winner)

#print the analysis to the terminal
print('Election Results')
print('---------------------')
print(f'Total Votes: {total_votes}')
print('---------------------')
for i in range(0,len(candidates)):
    print(candidates[i] + ":  " + str(percent_votes[i]) + "%  (" + str(votes_4_candidate[i]) + ")")
print('---------------------')
print(f'Winner: {winner}')
print('---------------------')


#Write results to to text file
election_results_file = open("election_results.txt", "w")
election_results_file.write("Elections Results\n")
election_results_file.write("---------------------\n")
election_results_file.write(f'Total Votes: {total_votes}\n')
election_results_file.write("---------------------\n")
for i in range(0,len(candidates)):
    election_results_file.write(candidates[i] + ":  " + str(percent_votes[i]) + "%  (" + str(votes_4_candidate[i]) + ")\n")
election_results_file.write("---------------------\n")
election_results_file.write(f'Winner: {winner}')
election_results_file.write("\n---------------------")
