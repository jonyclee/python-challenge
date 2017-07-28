import os
import csv

# Pathways
root_path = os.path.join(os.getcwd(), "..")
instruction_path = os.path.join(root_path , "Instructions")
poll_path = os.path.join(instruction_path , "PyPoll")
data_path = os.path.join(poll_path , 'raw_data')
election_path = os.path.join(data_path , 'election_data_2.csv')

# List of global variables
global total_votes
total_votes = 0

global cand
cand = []

global vote
vote = []

global winner
winner = ''

global winner_vote
winner_vote = 0

global data
data = []

# Opens csv file
with open(election_path , 'r+') as election:

    # Store data into a list
    temp = []
    for row in election:
        row = row.rstrip('\n')
        temp = row.split(',')
        data.append(temp)
        total_votes += 1

    # Stores unique values of candidates
    for i in range(1,len(data)):
        if data[i][2] not in cand:
            cand.append(data[i][2])

    for i in range(0,len(cand)):
        vote.append(0)

    # Run basic analysis
    for i in range(1,len(data)):
        for j in range(0,len(cand)):
            if data[i][2] == cand[j]:
                vote[j] += 1

    total_votes -= 1

    # Checks who is the winner
    for i in range(0,len(cand)):
        if vote[i] > winner_vote:
            winner_vote = vote[i]
            winner = cand[i]

election.close()

# Output
print('Election Results')
print('-------------------------')
print('Total Votes: ' , total_votes)
print('-------------------------')
for i in range(0,len(cand)):
    print(cand[i] , ': ' , round((vote[i] / total_votes) * 100 , 1) , '% (' , vote[i] , ')')
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')

# Save results into a txt file
f = open('result.txt' , 'w+')

f.write('Election Results\n')
f.write('-------------------------\n')
f.write(('Total Votes: ' + str(total_votes)) + '\n')
f.write('-------------------------\n')
for i in range(0,len(cand)):
    f.write((cand[i] + ': ' + str(round((vote[i] / total_votes) * 100 , 1)) + '% (' + str(vote[i]) + ')'))
f.write('-------------------------\n')
f.write(('Winner: ' + str(winner) + '\n'))
f.write('-------------------------\n')

f.close()
