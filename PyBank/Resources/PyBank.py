#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


import os
import csv

dir = os.path.dirname(__file__)
text_file=os.path.join("budget_analysis.txt")

file_path = os.path.join(dir, "budget_data.csv")

with open(file_path) as file:
    data = csv.reader(file)
    col_names = next(data)
    
    row_ct = 2
    month_ct = 0
    net_profit = 0
    prev_profit = 0
    sum_changes = 0
    newlist = []
    Average_change=0

    for row in data:
        curr_date = str(row[0])
        curr_profit = int(row[1])

        # print(f'prev_profit: {prev_profit}')
        # print(f'curr_profit: {curr_profit}')
        # print(f'sum_changes: {sum_changes}')
      

        if row_ct == 2:
            prev_profit = curr_profit

        if row_ct > 2: 
            change_profit = curr_profit - prev_profit
            newlist.append(change_profit)
            sum_changes= sum_changes + change_profit


        month_ct += 1
        net_profit = net_profit+ int(row[1])
        row_ct += 1
average_ch=sum(newlist)/len(newlist)
max(newlist)
min(newlist)

print(month_ct)
print(net_profit)
print(sum_changes/month_ct)
print(newlist)
print(average_ch)
print(max(newlist))
print(min(newlist))

with open(text_file, "w") as txt_file:
    txt_file.write(f'Total: $ {net_profit}\n' ) 
    txt_file.write(f'Average Change: $ {average_ch}\n' )