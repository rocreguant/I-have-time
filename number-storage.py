#!/usr/bin/env python
# coding: utf8
__author__ = 'roc'


import numpy as np
import os
from os import listdir
from os.path import isfile, join

import json
import csv
import sqlite3
import h5py #pip install h5py



#generated 4 rows with number_of_floats data
def data_generation(number_of_floats):
	ret = np.ndarray((number_of_floats, 4))
	for i in range(number_of_floats):
		ret[i] = np.random.uniform( -10, 10, 4 )
	return ret


#standard text saving
def save_text_file(data):
	f = open('text.txt', 'w')
	for el in data:	
		f.write(str(el).strip('[]'))
		f.write('\n')
	f.close()
	return True


#saving with json files
def save_json(data):
	f = open('json.json', 'w')
	j=json.dumps(data.tolist())
	json.dump(j, f)
	f.close()
	return True

#saving numbers on csv
def save_csv(data):
	with open('csv.csv', 'w') as csvfile:
		fieldnames = ['Col_A', 'Col_B', 'Col_C', 'Col_D']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		for el in data:
			writer.writerow({'Col_A': str(el[0]), 'Col_B': str(el[1]),'Col_C': str(el[2]),'Col_D': str(el[3])})
	return True


#Tab Separated Values (TSV)
def save_tsv(data):
	with open('tsv.tsv', 'w') as tsvfile:
		writer = csv.writer(tsvfile, delimiter='\t')
		for el in data:
				writer.writerow(el)
	return True
	
	

#save data in sqlite
def save_sqlite(data):
	conn = sqlite3.connect('data.sqlite3')
	cur = conn.cursor()

	cur.execute('DROP TABLE IF EXISTS Data ')
	cur.execute('CREATE TABLE Data (Col_A REAL, Col_B REAL, Col_C REAL, Col_D REAL)')
	for el in data:
		cur.execute('INSERT INTO Data VALUES ('+str(el[0])+', '+str(el[1])+', '+str(el[2])+', '+str(el[3])+')')
	conn.commit()
	conn.close()

#save the data in a hdf file
def save_hdf(data):
	h = h5py.File('data.hdf5', 'w')
	dset = h.create_dataset('data', data=data)

#check the file size
def show_file_size():
	mypath = '.'
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	for fil in onlyfiles:
		statinfo = os.stat(fil)
		print 'name '+str(fil)
		print 'size: '+str(statinfo.st_size)
		print ' '
	print onlyfiles

##############################
#
# Main
#
##############################


data = data_generation(100000)
save_text_file(data)
save_csv(data)
save_json(data)
save_csv(data)
save_tsv(data)
save_sqlite(data)
save_hdf(data)
show_file_size()
print 'Done'


#or just checking the table http://pandas.pydata.org/pandas-docs/stable/io.html#performance-considerations
