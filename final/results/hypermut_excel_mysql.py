#!/usr/bin/env python3

"""
This program imports Hypermut data from Excel into MySQL 
File must be in xls format
"""
import sys
import os
import mysql.connector
import xlrd


def main():

	#Ask user for file and check if it exists
	file = input("Enter file: ")
	try:
		fsock = open(file)
		fsock.close()

	except IOError:
		print ("The file does not exist.")
		sys.exit()

	#Open the workbook and define the worksheet
	try:
		book = xlrd.open_workbook(file)
	except xlrd.XLRDError:
		print("File must be in xls or xlsx format.")
		sys.exit()

	#Access the first sheet of excel file
	sheet = book.sheet_by_index(0)

	#Establish a MySQL connection
	database = mysql.connector.connect(user='sjone215', password=$PASSWORD, host='localhost', database='sjone215_hypermutants')

	#Get the cursor, which is used to traverse the database, line by line
	cursor = database.cursor()

	#Create the INSERT INTO sql query
	query = """INSERT IGNORE INTO hypermut (sequence_id, muts, potential_muts, controls, potential_cons, rate_ratio, fisher_pvalue) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

	#Create a for loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
	for r in range(1, sheet.nrows):
		sequence_id = sheet.cell(r,0).value
		muts = sheet.cell(r,1).value
		potential_muts = sheet.cell(r,2).value
		controls = sheet.cell(r,3).value
		potential_cons = sheet.cell(r,4).value
		rate_ratio = sheet.cell(r,5).value
		fisher_pvalue = sheet.cell(r,6).value

		#Assign values from each row
		values = (sequence_id, muts, potential_muts, controls, potential_cons, rate_ratio, fisher_pvalue)

		#Execute query	
		cursor.execute(query, values)


	#Close the cursor
	cursor.close()

	#Commit the transaction
	database.commit()

	#Close the database connection
	database.close()

	#Print results
	columns = str(sheet.ncols)
	rows = str(sheet.nrows)

	print("I just imported " + columns + " columns and " + rows + " rows to MySQL.")

if __name__ == '__main__':
	main()

    
