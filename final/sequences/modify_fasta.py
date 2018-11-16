#!/usr/local/bin/python3

import sys
import os

"""
The purpose of this script to eliminate any "-" characters as they prevent SeqIO 
from translating a DNA sequence.
"""

fasta = input("File: ")
new_file = fasta.split('.fasta')[0] + '_modified.fasta'
outfile = open(new_file, 'w')
file = open(fasta)
for line in file:
	if line.startswith('>'):
		outfile.write(line)
		continue
	else:
		outfile.write(line.replace("-",""))
file.close()
outfile.close()

