#Import Budget Data csv
import os
import csv

csv_path = "C:/Users/Student/OneDrive/Desktop/Start_code.zip/Starter_Code/PyBank/Resources"



#open csv
with open(csv_path, mode = 'r') as csvfile:
    csvreader =csv.reader(csvfile)

    for row in csvreader:
        print(row) 
