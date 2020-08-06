# Date: August 2020
# Description: This Python Script reads budget_data.csv and prints results of financial analysis
# Author: Ken Ho

import pandas as pd

DataFolder = 'DataFiles/'
FileName = 'budget_data.csv'
budget_df = pd.read_csv(DataFolder + FileName)

budget_df['Changes_Profit/Loss'] = 0
for idnx in range(len(budget_df)):
    if idnx != 0:
        budget_df.loc[budget_df.index==idnx, 'Changes_Profit/Loss'] = \
            budget_df[budget_df.index==idnx]['Profit/Losses'].item() -  budget_df[budget_df.index==(idnx-1)]['Profit/Losses'].item()

# Get Total Number of months included in dataset
noMonths = len(budget_df.Date.unique())

# Get Net amount of "Profit/Losses" over the entire period
netProfitLosses = budget_df['Profit/Losses'].sum()

# Get Average of Changes in Profit/Losses, round to two decimal places
budgetMean = round(budget_df['Changes_Profit/Loss'].sum()/(len(budget_df)-1),2)

# The greatest increase in profit (date and amount) over the entire period
maxChangeProfit = int(budget_df['Changes_Profit/Loss'].max())
maxChangeProfitDate = budget_df[budget_df['Changes_Profit/Loss'] == maxChangeProfit]['Date'].item()

# The greatest decrease in losses (date and amount) over the entire period
maxChangeLosses = int(budget_df['Changes_Profit/Loss'].min())
maxChangeLossesDate = budget_df[budget_df['Changes_Profit/Loss'] == maxChangeLosses]['Date'].item()

# Print results
print('Financial Analysis')
print('-'*50)

print('Total Months: ' + str(noMonths))
print('Total: $' + str(netProfitLosses))
print('Average Change: $' + str(budgetMean))
print('Greatest Increase in Profits: ' + maxChangeProfitDate + ' $(' + str(maxChangeProfit) + ')')
print('Greatest Decrease in Profits: ' + maxChangeLossesDate + ' $(' + str(maxChangeLosses) + ')')

