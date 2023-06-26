import csv

#importing module & subclass to assist with automatically initializes missing keys with the default value of 0
from collections import defaultdict 

#Declaring file location
location = "election_data.csv"

#Declaring variables
total_votes = 0
number_of_votes = defaultdict(int)
list_of_candidates = set()


#Opening and reading the CSV file
with open(location, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

     #Skipping the first header row
    header=next(csv_reader)

    
    for row in csv_reader:
        candidate=row[2]

        #The total number of votes cast
        total_votes += 1

        
        #The total number of votes each candidate won
        number_of_votes[candidate] += 1

        #A complete list of candidates who received votes
        list_of_candidates.add(candidate)


#The percentage of votes each candidate won
percentage_won = {candidate: (votes / total_votes) * 100 for candidate, votes in number_of_votes.items()}

#The winner of the election based on popular vote
winner = max(number_of_votes, key=number_of_votes.get)

# Printing the results in IDE
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
for candidate in list_of_candidates:
    print(f"{candidate}: {percentage_won[candidate]:.3f}% ({number_of_votes[candidate]})")
print("----------------------------------")
print(f"Winner: {winner}")
print("----------------------------------")

# Printing the results in text file
output_file = "election_results.txt"
with open(output_file, 'w') as file:
    file.write("Election Results\n") #Ensuring that the cursor moves to next line before printing the next statement
    file.write("---------------------------------- \n")
    file.write(f"Total Votes: {total_votes} \n")
    file.write("---------------------------------- \n")
    for candidate in list_of_candidates:
        file.write(f"{candidate}: {percentage_won[candidate]:.3f}% ({number_of_votes[candidate]}) \n") #Returning the value upto 3 decimal places
    file.write("---------------------------------- \n")
    file.write(f"Winner: {winner} \n")
    file.write("---------------------------------- \n")