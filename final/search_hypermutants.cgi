#!/usr/local/bin/python3

import mysql.connector
import cgi, cgitb
import json
import os
from collections import defaultdict
import re
from scipy import stats

"""
This script connects to MySQL and searches for the selected patient and selected tool, Hyperfreq
or Hypermut. A table is displayed on a website with results of the number of hypermutants corresponding to each tissue.
The total number of sequences for the selected patient and total number of hypermutants is also displayed.
"""

def main():

	print("Content-Type: application/json\n\n")
	form = cgi.FieldStorage()

	#retrieve data from fields
	patient = form.getvalue('patient')
	
	if form.getvalue('hyper_tool'):
		hyper_tool = form.getvalue('hyper_tool')
	else:
		hyper_tool = "Not set"

	if form.getvalue('frame'):
		frame = form.getvalue('frame')
	else:
		frame = "Not entered"
       
	#connects to hypermutants database in MySQL
	conn = mysql.connector.connect(user='sjone215', password='Hepatitis89!', host='localhost', database='sjone215_hypermutants', charset='utf8', use_unicode=True)

	#cursor object allows you to issue commands
	curs = conn.cursor()

	#create dictionary 'variables'
	entries = []
	entries2 = []
	all_entries = []
	full_entries = []
	orf = []
	results = []
		
	if hyper_tool in ['hyperfreq', 'hypermut']:
	
		if hyper_tool == 'hyperfreq':

			#query to find patient and tissue type and to count hypermutants
			qry1 = """SELECT s.tissue, if(count(h.hypermutant='True')>=1,sum(h.hypermutant='True'),0) as count_hyper 
				FROM sequence_info s JOIN hyperfreq h on s.sequence_id=h.sequence_id 
				WHERE s.coded_name = %s GROUP by s.tissue"""
		

			#query to find total hypermutants for selected patient
			qry2 = """SELECT count(h.hypermutant) as total_hyper 
				FROM sequence_info s JOIN hyperfreq h on s.sequence_id=h.sequence_id 
				WHERE s.coded_name = %s and h.hypermutant = 'True'"""

			#query to find total sequences for selected patient
			qry3 = """SELECT count(s.sequence_id) as total_seq 
				FROM sequence_info s 
				WHERE s.coded_name = %s"""

			#query to find number of tissue samples by type
			qry4 = """SELECT s.tissue, count(s.tissue) as total_tissue 
				FROM sequence_info s 
				WHERE s.coded_name = %s GROUP by s.tissue"""

			#query to find the id, tissue, date, hypermutant
			qry5 = """SELECT s.sequence_id, s.tissue, DATE_FORMAT(s.date, "%m/%d/%Y") as new_date
				FROM sample_info s JOIN hyperfreq h on s.sequence_id=h.sequence_id 
				WHERE h.hypermutant = 'True' and s.coded_name = %s"""
			
			qry6 = """SELECT o.sequence_id , AVG(o.length) as average, MAX(o.length) as max, MIN(o.length) as min, count(o.orf_id) as count  
				FROM open_reading_frame o JOIN hyperfreq h on h.sequence_id=o.sequence_id JOIN sequence_info s on h.sequence_id =  s.sequence_id 
				WHERE s.coded_name like %s and o.frame = %s and h.hypermutant = 'True' GROUP by o.sequence_id"""

			#execute first query
			curs.execute(qry1, (patient, ))

			#put results in entries
			for (tissue, count_hyper) in curs:
				count_hyper = int(re.findall('\d+', str(count_hyper))[0])
				entry = {"tissue":tissue, "count_hyper":count_hyper}
				entries.append(entry)

			#execute second query
			curs.execute(qry2, (patient, ))
			
			#store total hypermutants
			for (total_hyper) in curs:
				total_hyper = int(re.findall('\d+', str(total_hyper))[0])
	
			#execute third query
			curs.execute(qry3, (patient,))
	
			#store total count
			for (total_seq) in curs:
				total_seq = int(re.findall('\d+', str(total_seq))[0])

			#execute fourth query
			curs.execute(qry4, (patient,))

			#store total count
			for (tissue, total_tissue) in curs:
				entry2 = {"tissue":tissue, "total_tissue":total_tissue}
				entries2.append(entry2)
			
			#merge entries1 and entries2 and sort by tissue
			d = defaultdict(dict)
			for l in (entries, entries2):
				for elem in l:
					d[elem['tissue']].update(elem)
			all_entries = sorted(list(d.values()), key=lambda k: k['tissue'].lower())
			
			#execute fifth query
			curs.execute(qry5, (patient,))

			#store results of all hypermutants
			for (sequence_id, tissue, new_date) in curs:
				entry3 = {"sequence_id": sequence_id, "tissue": tissue, "new_date":new_date}
				full_entries.append(entry3)

			#execute sixth query
			curs.execute(qry6, (patient, frame))
			
			for (sequence_id, average, max, min, count) in curs:
				entry4 = {"sequence_id": sequence_id, "average":str(average), "max":max, "min":min, "count":count}
				orf.append(entry4)
			
			orf = sorted(orf, key=lambda k: ['sequence_id'])

			
			results = {'total_hyper':total_hyper, 'total_seq':total_seq,'matches':all_entries, 'full_matches': full_entries, 'orf': orf}
	

		elif hyper_tool == 'hypermut':

			#query to find patient and tissue type and to count hypermutants
			qry1 = """SELECT s.tissue, if(count(h.hypermutant='True') >=1,sum(h.hypermutant='True'),0) as count_hyper
				FROM sequence_info s JOIN hypermut h on s.sequence_id=h.sequence_id
				WHERE s.coded_name = %s GROUP by s.tissue"""
			

			#query to find total hypermutants for selected patient
			qry2 = """SELECT count(h.hypermutant) as total_hyper
				FROM sequence_info s JOIN hypermut h on s.sequence_id=h.sequence_id
				WHERE s.coded_name = %s and h.hypermutant = 'True'"""

			#query to find total sequences for selected patient
			qry3 = """SELECT count(s.sequence_id) as total_seq
				FROM sequence_info s
				WHERE s.coded_name = %s"""

			#query to find number of tissue samples by type
			qry4 = """SELECT s.tissue, count(s.tissue) as total_tissue
				FROM sequence_info s
				WHERE s.coded_name = %s GROUP by s.tissue"""
                        
			#query to find the id, tissue, date, hypermutant
			qry5 = """SELECT s.sequence_id, s.tissue, DATE_FORMAT(s.date, "%m/%d/%Y") as new_date 
				FROM sample_info s JOIN hyperfreq h on s.sequence_id=h.sequence_id  
				WHERE h.hypermutant = 'True' and s.coded_name = %s"""
                
			#query to find open reading frames
			qry6 = """SELECT o.sequence_id , AVG(o.length) as average, MAX(o.length) as max, MIN(o.length) as min, count(o.orf_id) as count
				FROM open_reading_frame o JOIN hypermut h on h.sequence_id=o.sequence_id JOIN sequence_info s on h.sequence_id=s.sequence_id
                                WHERE s.coded_name like %s and o.frame = %s and h.hypermutant = 'True' GROUP by o.sequence_id"""
                
			#execute first query
			curs.execute(qry1, (patient, ))

			#put results in entries
			for (tissue, count_hyper) in curs:
				count_hyper = int(re.findall('\d+', str(count_hyper))[0])
				entry = {"tissue":tissue, "count_hyper":count_hyper}
				entries.append(entry)
                        
			#execute second query
			curs.execute(qry2, (patient, ))
                                
			#store total hypermutants
			for (total_hyper) in curs:
				total_hyper = int(re.findall('\d+', str(total_hyper))[0])

			#execute third query
			curs.execute(qry3, (patient,)) 
			
			#store total count
			for (total_seq) in curs:
				total_seq = int(re.findall('\d+', str(total_seq))[0])
                                
			#execute fourth query
			curs.execute(qry4, (patient,))

			#store total count
			for (tissue, total_tissue) in curs:
				entry2 = {"tissue":tissue, "total_tissue":total_tissue}
				entries2.append(entry2)

			#merge entries1 and entries2 and sort by tissue
			d = defaultdict(dict)
			for l in (entries, entries2):
				for elem in l:
					d[elem['tissue']].update(elem)
			all_entries = sorted(list(d.values()), key=lambda k: k['tissue'].lower())

			#execute fifth query
			curs.execute(qry5, (patient,))

			#store results of all hypermutants
			for (sequence_id, tissue, new_date) in curs:
				entry3 = {"sequence_id": sequence_id, "tissue": tissue, "new_date":new_date}
				full_entries.append(entry3)

			#execute sixth query
			curs.execute(qry6, (patient, frame))
                        
			for (sequence_id, average, max, min, count) in curs:
				entry4 = {"sequence_id": sequence_id, "average":str(average), "max":max, "min":min, "count":count}
				orf.append(entry4)

			orf = sorted(orf, key=lambda k: ['sequence_id'])

			results = {'total_hyper':total_hyper, 'total_seq':total_seq,'matches':all_entries, 'full_matches':full_entries, 'orf':orf}


	else:
		#find matches and mismatches for table
		qry1 = """select f.sequence_id as sequence_id, m.hypermutant as mut_hyper, f.hypermutant as freq_hyper, m.hypermutant = f.hypermutant as is_match 
			from hyperfreq f JOIN hypermut m on f.sequence_id = m.sequence_id 
			JOIN sequence_info on f.sequence_id = sequence_info.sequence_id 
			where sequence_info.coded_name = %s order by sequence_id"""

		#query to find total hypermutants for selected patient
		qry2 = """SELECT count(h.hypermutant) as total_hyper
			FROM sequence_info s JOIN hyperfreq h on s.sequence_id=h.sequence_id
			WHERE s.coded_name = %s and h.hypermutant = 'True'"""
	

		#query to find total hypermutants for selected patient
		qry3 =  """SELECT count(h.hypermutant) as total_hyper
			FROM sequence_info s JOIN hypermut h on s.sequence_id=h.sequence_id
			WHERE s.coded_name = %s and h.hypermutant = 'True'"""

		#query to find total sequences for selected patient
		qry4 = """SELECT count(s.sequence_id) as total_seq
			FROM sequence_info s
			WHERE s.coded_name = %s"""

		#execute first query
		curs.execute(qry1, (patient, ))

		match_count=0

		for(sequence_id, mut_hyper, freq_hyper, is_match) in curs:
			if is_match == 1:
				is_match = "Match"
				match_count+=1
			else:
				is_match = "Mismatch"
			entry = {"sequence_id": sequence_id, "mut_hyper": mut_hyper, "freq_hyper": freq_hyper, "is_match": is_match}
			entries.append(entry)	

		entries = sorted(entries, key=lambda k: ['sequence_id'])
		
		#execute second query
		curs.execute(qry2, (patient, ))

		for(total_hyper) in curs:
			total_freq = int(re.findall('\d+', str(total_hyper))[0])

		#execute third query
		curs.execute(qry3, (patient, ))

		for(total_hyper) in curs:
			total_mut = int(re.findall('\d+', str(total_hyper))[0])

		#execute fourth query
		curs.execute(qry4, (patient, ))

		for(total_seq) in curs:
			total_seq = int(re.findall('\d+', str(total_seq))[0])
		
		#to find fisher pvalue comparing the two tools
		oddratio, fisher_pvalue = stats.fisher_exact([[total_mut,(total_seq-total_mut)], [total_freq, total_seq-total_freq]])
		
		results = {"fisher_pvalue":fisher_pvalue, "match_count":match_count, "total_seq": total_seq, "total_mut": total_mut,"total_freq": total_freq,"matches":entries}
	
	#commit changes and close
	conn.close()
	
	print(json.dumps(results))


if __name__== '__main__':
	main()


