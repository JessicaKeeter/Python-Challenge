#Import Budget Data csv
import os
import csv

csv_path = "PyBank\\Resources\\budget_data.csv"


#open csv
csvfile = open(csv_path, mode = 'r')
csvreader =csv.reader(csvfile)

for row in csvreader:
      print(row)

      