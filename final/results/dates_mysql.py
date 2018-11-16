#!/usr/bin/env python3

"""
This program imports sequence data from Excel into MySQL.
This data includes sequence ID, tissue type, date of collection.
File must be in xls format
"""
import sys
import os
import mysql.connector
import xlrd
import datetime

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
	query = """INSERT IGNORE INTO sample_info (sequence_id, tissue, date) VALUES (%s, %s, %s)"""

	#Create a for loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
	for r in range(0, sheet.nrows):
		sequence_id = sheet.cell(r,0).value
		tissue = sheet.cell(r,1).value

		#convert excel date to MySQL format
		exceltime = sheet.cell(r,3).value
		time_tuple = xlrd.xldate_as_tuple(exceltime,0)
		date = datetime.datetime(*time_tuple)
		
		#Assign values from each row
		values = (sequence_id, tissue, date)

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

    
