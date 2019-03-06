import os
import csv
import collections

total_votes=0
Votes = collections.Counter()
election_data = os.path.join(r'C:\Users\sohlb\OneDrive\Desktop\NUCHI201902DATA1\Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv')
with open(election_data) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
        Votes[row[2]] += 1
        total_votes+=1

Khan_pct = round(Votes['Khan']/(total_votes)*100)
Correy_pct = round(Votes['Correy']/(total_votes)*100)
Li_pct = round(Votes['Li']/(total_votes)*100)
OTooley_pct = round(Votes["O'Tooley"]/(total_votes)*100)

print("Election Results \n ------------------------------------")
print("Total Votes: "+ "{:,}".format(total_votes))       
print('Khan number of votes: %s' % Votes['Khan'] + " (" + str(Khan_pct) + "%)")
print('Correy number of votes: %s' % Votes['Correy']+ " (" + str(Correy_pct) + "%)")
print('Li number of votes: %s' % Votes['Li'] + " (" + str(Li_pct) + "%)")
print("O'Tooley number of votes: %s" % Votes["O'Tooley"]+ " (" + str(OTooley_pct) + "%)")
print("------------------------------------")
print("Winner: Khan")
print("------------------------------------")
# #print(Votes.most_common())
# #print(Votes)

T = Votes["O'Tooley"]

output_file = os.path.join("PyPoll_output.txt")
with open(output_file, 'w') as text_file:
    final_output = (

    f'Election Results\n'
    f'------------------------------------\n'
    f"Total Votes: {total_votes}\n"
    f'Khan number of votes: {Votes["Khan"]}   {str(Khan_pct)}%\n'
    f'Correy number of votes: {Votes["Correy"]}   {str(Correy_pct)}%\n'
    f'Li number of votes: {Votes["Li"]} {str(Li_pct)}%\n'
    f'OTooley number of votes: {T} {str(OTooley_pct)}%\n'
    f'------------------------------------\n'
    f'Winner: Khan'
    f'------------------------------------\n'
)
    print(final_output)
    writer = csv.writer(text_file)
    writer.writerow(final_output)


#print(round(Votes['Khan']/(total_votes)*100))
#print(Khan_pct)
#Winner = highest pct.  if Khan_pct > Correy_pc. or list pcts.  list.max?
#Candidate_List = [Khan_pct,Correy_pct,Li_pct,OTooley_pct]
#print(max(Candidate_List))


#Vote_Percentages: {
#    "Khan": Khan_pct, "Correy": Correy_pct, "Li": Li_pct, "O'Tooley": OTooley_pct}
#print(max(Vote_Percentages))
#print(Candidate_dict)

#film = {"title": "Interstellar",
#        "revenues": {"United States": 360, "China": 250, "United Kingdom": 73}}
#print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")

#FINAL_OUTPUT = (
#    'Election Results \n'
#     "------------------------------------ \n"
#    "Total Votes: "+ "{:,}\n".format(total_votes)  
#    'Khan number of votes: %s' % Votes['Khan'] + " (" + str(Khan_pct) + "%)\n"
#    'Correy number of votes: %s' % Votes['Correy']+ " (" + str(Correy_pct) + "%)\n"
#     'Li number of votes: %s' % Votes['Li'] + " (" + str(Li_pct) + "%)\n"
#     "O'Tooley number of votes: %s" % Votes["O'Tooley"]+ " (" + str(OTooley_pct) + "%)\n"
#     "------------------------------------\n"
#     "Winner: Khan")
# print(FINAL_OUTPUT)

#Final_Analysis = (total_votes, Votes['Khan'], Khan_pct, Votes['Correy'], Correy_pct, Votes['Li'], Li_pct, Votes["O'Tooley"], OTooley_pct)
#print("Winner:" + Winner + "!")