import csv

location = "C:/Users/bambaj/Desktop/Classwork/Challenge 3_Python/PyBank/Resources/budget_data.csv"
output_text_file = "C:/Users/bambaj/Desktop/Classwork/Challenge 3_Python/PyBank/Resources/Financial_analysis.txt"

with open(location, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    
    total_months = 0
    net_total = 0
    average_change = 0
    greatest_increase = 0
    greatest_increase_date = 0
    greatest_decrease = 0
    greatest_decrease_date = 0
    greatest_increase_date = 0
    greatest_decrease_date = 0
    changes = [] #Empty list to store changes
    dates = [] #Empty list to store corresponding dates
    last_profit_loss = 0

    #Skip the header row
    header = next(csv_reader)

    #The net total amount of "Profit/Losses" over the entire period
    for row in csv_reader:
        #print(row)
    #Total number of months in dataset
        total_months += 1

       #Extracting the date and amount
        date = row[0]
        profit_loss = int(row[1])
               
       #The net total amount of "Profit/Losses" over the entire period
        net_total += profit_loss
        
        # Calculate the change in profit/loss from the previous month and store it in the 'changes' list
        if last_profit_loss != 0:
            change = profit_loss - last_profit_loss
            changes.append(change)
            dates.append(date)
        
        last_profit_loss = profit_loss

#Checking if the change list is not empty
if len(changes) > 0:
        #Average changes in Profit/Losses
        average_change = sum(changes) / len(changes)
else:
        average_change = 0
        #Average changes in Profit/Losses
    

#Greatest Increase & decrease in profit
greatest_increase = max(changes)
greatest_decrease = min(changes)

#Extracting date for corresponding Greatest increase/ decrease 
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}") #floating number with only 2 decimal points
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")  


#To export the results to text file
with open(output_text_file, 'w') as file:
    #\n moves to next line
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n") #floating number with only 2 decimal points
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
