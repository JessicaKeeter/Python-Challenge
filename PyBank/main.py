import csv

csv_path = "PyBank/Resources/budget_data.csv"

def average(numbers):
    return sum(numbers) / len(numbers)

# Variables
profits = []
months = 0
revchange = []
revaverage = 0
greatestincrease = {"date": "", "amount": float("-inf")}
greatestdecrease = {"date": "", "amount": float("inf")}
prevprofitloss = None

# Open csv
with open(csv_path, 'r') as file:
    csvreader = csv.DictReader(file)
    next(csvreader) 

    # Read rows in data
    for row in csvreader:
        profits.append(int(row['Profit/Losses']))
        months += 1
        
        # Calculate change in profit/losses
        profitloss = int(row['Profit/Losses'])
        if prevprofitloss is not None:
            change = profitloss - prevprofitloss
            revchange.append(change)
        
        prevprofitloss = profitloss

    # Average of revchange
    revaverage = average(revchange) if revchange else 0

    # Calculate greatest increase and decrease
    if revchange:  # Check if revchange is not empty
        for change, row in zip(revchange, csvreader):
            if change > greatestincrease["amount"]:
                greatestincrease['date'] = row['Date']
                greatestincrease["amount"] = change

            if change < greatestdecrease["amount"]:
                greatestdecrease['date'] = row['Date']
                greatestdecrease["amount"] = change

# Print
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${revaverage:.2f}")
print(f"Greatest Increase in Profits: {greatestincrease['date']} (${greatestincrease['amount']})")
print(f"Greatest Decrease in Profits: {greatestdecrease['date']} (${greatestdecrease['amount']})")

# Write to text file
with open("output.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${sum(profits)}\n")
    file.write(f"Average Change: ${revaverage:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatestincrease['date']} (${greatestincrease['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatestdecrease['date']} (${greatestdecrease['amount']})\n")
