import csv

csv_path = "PyBank/Resources/budget_data.csv"

def average(numbers):
    return sum(numbers) / len(numbers)

# Variables
profits = []
months = 0
revchange = []
prevprofitloss = None
greatestincrease = {"Date": "", "Profit/Losses": 0}
greatestdecrease = {"Date": "", "Profit/Losses": 0}

# Open csv
with open(csv_path, 'r') as file:
    csvreader = csv.DictReader(file)
    
    # Read rows in data
    for row in csvreader:
        currentloss = int(row["Profit/Losses"])
        profits.append(currentloss)
        months += 1
        
        # Calculate change in profit/losses
        if prevprofitloss is not None:
            change = currentloss - prevprofitloss
            revchange.append(change)
        
            # Calculate greatest increase and decrease
            if len(revchange) >= 2:  
                if change > greatestincrease["Profit/Losses"]:
                    greatestincrease["Date"] = row["Date"]
                    greatestincrease["Profit/Losses"] = change
                
                if change < greatestdecrease["Profit/Losses"]:
                    greatestdecrease["Date"] = row["Date"]
                    greatestdecrease["Profit/Losses"] = change
        
        prevprofitloss = currentloss  

# Average of revchange
revaverage = average(revchange) 

# Print
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${revaverage:.2f}")
print(f"Greatest Increase in Profits: {greatestincrease['Date']} (${greatestincrease['Profit/Losses']})")
print(f"Greatest Decrease in Profits: {greatestdecrease['Date']} (${greatestdecrease['Profit/Losses']})")

# Write to text file
with open("output.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${sum(profits)}\n")
    file.write(f"Average Change: ${revaverage:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatestincrease['Date']} (${greatestincrease['Profit/Losses']})\n")
    file.write(f"Greatest Decrease in Profits: {greatestdecrease['Date']} (${greatestdecrease['Profit/Losses']})\n")
