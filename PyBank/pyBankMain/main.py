import csv

#write analysis data to new text file
file_to_output ="../pyBankAnalysis/analysis.txt"
file_to_load = "../pyBankResources/budget_data.csv"

#variables
total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change_list = []
greatest_increase =["",0]
greatest_decrease = ["", 9999999999999999]
month_of_change = []

		#open file with python
with open(file_to_load)as revenue_data:
	reader = csv.reader(revenue_data)
	header = next(reader)
	firstrow = next(reader)
	total_revenue += int(firstrow[1])
	prev_revenue = int(firstrow[1])
	total_months = total_months + 1	
	for row in reader:
		#total months
		total_months = total_months + 1
		total_revenue = total_revenue + int(row[1])

		#track revenue change
		
		revenue_change = float(row[1]) - prev_revenue
		prev_revenue = float(row[1])
		revenue_change_list = revenue_change_list + [revenue_change]
		month_of_change = month_of_change + [row[0]]

		#greatest increase
		if (revenue_change > greatest_increase[1]):
			greatest_increase[0] = row[0]
			greatest_increase[1] = revenue_change

		#greatest decrease	
		if (revenue_change < greatest_decrease[1]):
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = revenue_change

#average revenue change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
   
output = (

	f"\nFinancial Analysis\n"
	f"----------------------------\n"
	f"Total Months: {total_months}\n"
	f"Total : ${total_revenue:,.2f}\n"
	f"Average Change: ${revenue_avg:,.2f}\n"
	f"Greatest Increase in Profits:{greatest_increase[0]} (${greatest_increase[1]:,.2f})\n"
	f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})\n"
)
#print the output
print(output)

#write to file
with open(file_to_output, 'w')as txt_file:
	txt_file.write(output)
