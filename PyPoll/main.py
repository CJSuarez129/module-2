import os
import csv

pypollcsv=os.path.join('Resources','election_data.csv')

candidate1_votes = 0
candidate2_votes = 0  
candidate3_votes = 0 
Total = 0
winner_name = ""
        
with open(pypollcsv) as PyPollcsvfile:
    PyPollcsvreader = csv.reader(PyPollcsvfile, delimiter=',')
    header = next(PyPollcsvfile, None)

    for row in PyPollcsvreader:
        Total +=1
        if row[2] == "Charles Casper Stockham":
            candidate1_votes +=1
        elif row[2] =="Diana DeGette":
            candidate2_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            candidate3_votes += 1

 
    if (candidate1_votes > candidate2_votes) and (candidate1_votes > candidate3_votes):
                winner_name = "Charles Casper Stockham"
    elif (candidate2_votes > candidate1_votes) and (candidate2_votes > candidate3_votes):
                winnerName = "Diana DeGette"
    else:
        winner_name = "Raymon Anthony Doane"

        print(f"Election Results")
print("------------------------------\n")
print(f"Total Votes: {Total}\n")
print("------------------------------\n")
print(f"Charles Casper Stockham: {round((candidate1_votes/Total),5)*100}% ({candidate1_votes})\n")
print(f"Diana DeGette: {round((candidate2_votes/Total),5)*100}% ({candidate2_votes})\n")
print(f"Raymon Anthony Doane: {round((candidate3_votes/Total),3)*100}% ({candidate3_votes})\n")
print("------------------------------\n")
print(f"Winner: {winner_name}\n")
print("------------------------------\n")

pypoll_output = os.path.join("Analysis","election_data.txt")

with open(pypoll_output, "w",newline="") as output_file:
    print(f"Election Results", file=output_file)
    print("------------------------------\n", file=output_file)
    print(f"Total Votes: {Total}\n", file=output_file)
    print("------------------------------\n", file=output_file)
    print(f"Charles Casper Stockham: {round((candidate1_votes/Total),5)*100}% ({candidate1_votes})\n", file=output_file)
    print(f"Diana DeGette: {round((candidate2_votes/Total),5)*100}% ({candidate2_votes})\n", file=output_file)
    print(f"Raymon Anthony Doane: {round((candidate3_votes/Total),3)*100}% ({candidate3_votes})\n", file=output_file)
    print("------------------------------\n", file=output_file)
    print(f"Winner: {winnerName}\n", file=output_file)
    print("------------------------------\n", file=output_file)