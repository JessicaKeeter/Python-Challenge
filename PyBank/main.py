#Import Budget Data csv

import csv

csv_path = "PyBank\\Resources\\budget_data.csv"

def average(numbers):
    return sum(numbers) / len(numbers)

#variables
profits = []
months = 0
revchange = []
revaverage = 0
greatestincrease = {"date": "", "amount": float("-inf")}
greatestdecrease = {"date": "", "amount": float("inf")}
prevprofitloss = None

#open csv
with open(csv_path, 'r') as file:
    csvreader = csv.DictReader(file)
    next(csvreader) 

#read rows in data
    for rows in csvreader:
        profits.append(int(rows['Profit/Losses']))
        months +=1

#calculating change in profit/losses
profitloss = int(rows['Profit/Losses'])
if prevprofitloss is not None:
    change = profitloss - prevprofitloss
    revchange.append(change)

#Average of revchange
revaverage = average(revchange) if revchange else 0


#Calculating Greatest increase and Decrease
if revchange:  # Check if revchange is not empty
    for change in revchange:
        if change > greatestincrease["amount"]:
            greatestincrease['Date'] = rows['Date']
            greatestincrease["amount"] = change

        if change < greatestdecrease["amount"]:
            greatestdecrease['Date'] = rows['Date']
            greatestdecrease["amount"] = change

prevprofitloss = profitloss

#print 
print ("Financial Anaylsis")
print("-----------------------------------")
print(f"Total Months: {months}")
print(f"Total:${profits}")
print(f"Average Change: ${revaverage: .2f}")
print(f"Greatest Increase: {greatestincrease['date']} (${greatestincrease['amount']})")
print(f"Greatest Increase: {greatestdecrease['date']} (${greatestdecrease["amount"]})")

#text file
with open ("output.txt", "w") as file:
    file.write("Financial Anaylsis\n")
    file.write("-----------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total:${profits}\n")
    file.write(f"Average Change: ${revaverage: .2f}\n")
    file.write(f"Greatest Increase: {greatestincrease['date']} (${greatestincrease['amount']})\n")
    file.write(f"Greatest Increase: {greatestdecrease['date']} (${greatestdecrease["amount"]})\n")
