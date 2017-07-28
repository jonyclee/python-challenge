import os
import csv

# Pathways
root_path = os.path.join(os.getcwd(), "..")
instruction_path = os.path.join(root_path , "Instructions")
bank_path = os.path.join(instruction_path , "PyBank")
data_path = os.path.join(bank_path , 'raw_data')
bank1_path = os.path.join(data_path , 'budget_data_1.csv')

# List of global variables
global month
month = 0

global rev
rev = 0

global change
change = 0

global date1
date1 = ""

global date2
date2 = ""

global max_increase
max_increase = 0

global min_decrease
min_decrease = 0

global data
data = []

# Opens csv file
with open(bank1_path , 'r+') as bank1:

    # Stores data into a list
    temp = []
    for row in bank1:
        row = row.rstrip('\n')
        temp = row.split(',')
        data.append(temp)
        month += 1

    # Runs analysis
    for i in range(1,len(data)):
        rev += int(data[i][1])
        if int(data[i][1]) > max_increase:
            max_increase = int(data[i][1])
            date1 = data[i][0]
        if int(data[i][1]) < min_decrease:
            min_decrease = int(data[i][1])
            date2 = data[i][0]

    month -= 1
    change = round((rev / len(data)-1 ) , 2)

bank1.close()

# Output
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' , month)
print('Total Revenue: $' , rev)
print('Average Revenue Change: $' , change)
print('Greatest Increase in Revenue: ' , date1 , ' ($' , max_increase , ')')
print('Greatest Decrease in Revenue: ' , date2 , ' ($' , min_decrease , ')')
print('----------------------------\n')

# Save results into a txt file
f = open("analysis.txt" , 'w+')

f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write('Total Months: ' + str(month) + '\n')
f.write('Total Revenue: $' + str(rev) + '\n')
f.write('Average Revenue Change: $' + str(change) + '\n')
f.write('Greatest Increase in Revenue: ' + str(date1) + ' ($' + str(max_increase) + ')\n')
f.write('Greatest Decrease in Revenue: ' + str(date2) + ' ($' + str(min_decrease) + ')\n')
f.write('----------------------------\n')

f.close()
