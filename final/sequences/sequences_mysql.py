#!/usr/bin/env python3

"""
This program imports sequence data (fasta format) into MySQL.
"""
import sys
import os
import mysql.connector
from Bio import SeqIO


def main():

	#Ask user for file and check if it exists
	file = input("Enter file: ")
	try:
		fsock = open(file)
		fsock.close()
		
	except IOError:
		print ("The file does not exist.")
		sys.exit()

	#simple check for format of file
	for line in open(file):
		if line.startswith('>'):
			break
		else:
			print("Error: file not in fasta format.")
			sys.exit()

	
	coded_name = input("Enter coded name for patient: ")

	#Establish a MySQL connection
	database = mysql.connector.connect(user='sjone215', password=$PASSWORD, host='localhost', database='sjone215_hypermutants')

	#Get the cursor, which is used to traverse the database, line by line
	cursor = database.cursor()

	#Create the INSERT INTO sql query
	query = """INSERT IGNORE INTO sequence_info (sequence_id, sequence, coded_name) VALUES (%s, %s, %s)"""

	#open fasta file and get id and sequence for each entry
	with open(file, "rU") as handle:
		count = 0
		for record in SeqIO.parse(handle, "fasta"):
			sequence_id, sequence = str(record.id), str(record.seq)

			#Assign values from each record
			values = (sequence_id, sequence, coded_name)

			count = count + 1

			#Execute query	
			cursor.execute(query, values)

	#Close the cursor
	cursor.close()

	#Commit the transaction
	database.commit()

	#Close the database connection
	database.close()

	#Print results
	print("I just imported " + str(count) + " sequences to MySQL.")

if __name__ == '__main__':
	main()

    
