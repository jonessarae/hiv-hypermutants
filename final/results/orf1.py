#!/usr/local/bin/python3

"""
This script reads a fasta file, uses SeqIO to generate open reading frames, and
uploads the data into a MySQL database with table name open_reading_frame.
"""

import sys
import os
from Bio import SeqIO
from Bio import Seq
import mysql.connector
import re

def main():

	file = input("Enter file: ")

	try:
		fsock = open(file)
		fsock.close()

	except IOError:
		print ("The file does not exist in current directory.")
		sys.exit()

	#Establish a MySQL connection
	database = mysql.connector.connect(user='sjone215', password='Hepatitis89!', host='localhost', database='sjone215_hypermutants')

	#Get the cursor, which is used to traverse the database, line by line
	cursor = database.cursor()

	#Create the INSERT INTO sql query
	query = """INSERT INTO open_reading_frame (sequence_id, frame, length, aa_seq, sequence_length)
		VALUES (%s, %s, %s, %s, %s)"""

	#NCBI codon table
	table = 1

	#miniumum protein length
	min_pro_len = 1

	with open(file) as handle:
		for record in SeqIO.parse(handle, "fasta"):
			for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
				for frame in range(3):
					length = 3 * ((len(record)-frame) // 3) #Multiple of three
					substring_list = ["TAG", "TAA","TGA"]
					if any(substring in nuc[frame:frame+length] for substring in substring_list):
						for pro in nuc[frame:frame+length].translate(table).split("*"):
							m = re.search('([M]\S+)',str(pro))
							if m:
								pro=m.group(0)	
								if strand == 1:
									sequence_id = str(record.id)
									frame = frame
									length = len(pro)
									pro = pro
									sequence_length = len(record.seq)
									values = [sequence_id, frame, length, pro, sequence_length]

									#Execute query	
									cursor.execute(query, values)
									#print("%s - length %i, strand %i, id %s, frame %i,sequence length %i" % (pro, len(pro), strand, record.id, frame, len(record.seq)))
							else:
								continue
					else:
						continue
						
	#Close the cursor
	cursor.close()

	#Commit the transaction
	database.commit()

	#Close the database connection
	database.close()


if __name__ == '__main__':
	main()
