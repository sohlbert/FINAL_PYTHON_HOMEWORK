
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period 
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv
Gross_Margin = 0
Total_Months = 0
Avg = 0
Previous_Value = 0
Changes = []
date = []


budget_data = os.path.join('budget_data.csv')
with open(budget_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   for row in csvreader:
    Total_Months += 1
    Gross_Margin += int(row[1])
    Current_Value = row[1]
    change = (int(Current_Value) - int(Previous_Value))
    Changes.append(change)
    date.append(row[0])
    Previous_Value = row[1]
Changes=Changes[1:]

print("Financial Analysis \n -----------------------------------------------")
print("Total Months:", Total_Months) 
print('Total Margin: ${:,}'.format(Gross_Margin))
print('Avg Change: ${:,}'.format(round(sum(Changes)/len(Changes),2)))
print('Greatest Revenue Increase: ${:,}'.format(max(Changes)) + " in " + str(date[Changes.index(max(Changes))+1]))
print('Greatest Revenue Decrease: ${:,}'.format(min(Changes)) + " in " + str(date[Changes.index(min(Changes))+1]))
print("-----------------------------------------------")

Final_Analysis = (Total_Months, Gross_Margin, round(sum(Changes)/len(Changes),2), str(max(Changes)) + str(date[Changes.index(max(Changes))+1]), str(min(Changes)) + str(date[Changes.index(min(Changes))+1]))

output_file = os.path.join("PyBank_output.txt")
with open(output_file, 'w') as text_file:
    writer = csv.writer(text_file)
    writer.writerow(Final_Analysis)

# Place all of the data found into a summary DataFrame
#summary_table = DataFrame([{"Total Months": Total_Months,
 #                           "Total Margin": Gross_Margin,
  #                          "Average Change": round(sum(Changes)/len(Changes),2),
   #                         "Greatest Increase in Profits": "Answer Here",
    #                        "Greatest Decrease in Profits": "Answer Here"}])
#summary_table
#print(Changes)
#print(date)
#print(str(date[Changes.index(max(Changes))]))
#print(str(date[Changes.index(min(Changes))]))
#print(Changes)
#print("COMMENT OUT BELOW NOTES")
#print((Gross_Margin)/(Total_Months - 1))
#print(sum(Changes))
#print(len(Changes))
#print((Sum_Changes)/(Total_Months-1))
#avg_rev_change = sum(Changes)/len(Changes)
#max_rev_change = max(Changes)
#min_rev_change = min(Changes)    
#max_rev_change_date = str(date[Changes.index(max(Changes))])
#min_rev_change_date = str(date[Changes.index(min(Changes))])
#The average of the changes in "Profit/Losses" over the entire period
###For the PyBank portion of the assignment, 
#the "Average Change" refers to the average difference in "Profit/Losses" 
#between each row. You will not get the right answer if 
#you just take an average of the entire column
#calculate the differences (row2-row1, row3-row2, row4-row3, etc), 
#and then take an average of those values.
#print('Average Change in Margin by Month is: ${:,.2f}'.format(average))


# Place all of the data found into a summary DataFrame
#summary_table = pd.DataFrame([{"Total Months": Total_Months,
 #                             "Total Margin": Gross_Margin,
  #                            "Average Change": round(sum(Changes)/len(Changes),2),
   #                           "Greatest Increase in Profits": "Answer Here",
    #                          "Greatest Decrease in Profits": "Answer Here"}])
#summary_table

# Export file as a CSV, without the Pandas index, but with the header
#budget_data_df.to_csv("PyBank/Sohlberg_PyBank_Homework.csv", index=False, header=True)