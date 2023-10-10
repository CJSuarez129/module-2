# module-3-python
 pybank mainpy

  importing csv
  
 import os
import csv

  setting path

csvpath = os.path.join("Resources","budget_data.csv")

  setting lists and variables

months=[]
changes=[]


TotalProfitLoss=0
CurrentPL=0
LastProfitLoss=0
TotalProfitChange=0
MonthCount = 0
PLChange= 0

  opening csv
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 set header
    header= next(csvfile)

finding neccessary values

    for row in csv_reader:

    
        MonthCount += 1

        CurrentPL = int(row[1])
        TotalProfitLoss += CurrentPL

        if (MonthCount ==1) :
            LastProfitLoss = CurrentPL

            continue

        else: 
            months.append(row[0])
            PLChange = CurrentPL - LastProfitLoss
            changes.append(PLChange)
            LastProfitLoss =CurrentPL

ChangeSum= sum(changes)
AverageChange= round(ChangeSum/(MonthCount-1),2)

  finding max and min and change values
  
max_change= max(changes)
max_loss= min(changes)
max_change_index=changes.index(max_change)
max_loss_index=changes.index(max_loss)
best_month= months[max_change_index]
worst_month=months[max_loss_index]  


  printing values to terminal
  
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {MonthCount}\n")
print(f"Total: ${TotalProfitLoss}\n")
print(f"Average Change: ${AverageChange}/n")
print(f"Greatest Increase in Profits: {best_month} (${max_change})\n")
print(f"Greatest Decrease in Losses: {worst_month} (${max_loss})\n")

  exporting results
  
newbudget_file= os.path.join("Anlysis", "budget_data.txt")
with open(newbudget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {MonthCount}\n")
    outfile.write(f"Total:  ${TotalProfitLoss}\n")
    outfile.write(f"Average Change:  ${AverageChange}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${max_loss})\n")

    PyPoll mainpy

    importing csv and paths
import os
import csv

pypollcsv=os.path.join("Resources","election_data.csv")

 setting variables
 
candidate1_votes = 0
candidate2_votes = 0  
candidate3_votes = 0 
Total = 0
winner_name = ""


        opening csv
with open(pypollcsv) as PyPollcsvfile:
    PyPollcsvreader = csv.reader(PyPollcsvfile, delimiter=',')
    header = next(PyPollcsvfile, None)
    
creating for loop to find canditate vote count
    for row in PyPollcsvreader:
        Total +=1
        if row[2] == "Charles Casper Stockham":
            candidate1_votes +=1
        elif row[2] =="Diana DeGette":
            candidate2_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            candidate3_votes += 1

 if, elif, else to display canditate winner
    if (candidate1_votes > candidate2_votes) and (candidate1_votes > candidate3_votes):
                winner_name = "Charles Casper Stockham"
    elif (candidate2_votes > candidate1_votes) and (candidate2_votes > candidate3_votes):
                winnerName = "Diana DeGette"
    else:
        winner_name = "Raymon Anthony Doane"
printing results
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

 outputting results to .txt file
 
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
