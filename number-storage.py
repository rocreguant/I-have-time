#!/usr/bin/env python
# coding: utf8
__author__ = 'roc'

import numpy as np

#generated 4 rows with number_of_floats data
def data_generation(number_of_floats):
	ret = np.ndarray((number_of_floats, 4))
	for i in range(number_of_floats):
		ret[i] = np.random.uniform( -10, 10, 4 )
	return ret

#standard text saving
def text_file(data):
	f = open('text.txt', 'w')
	for el in data:	
		f.write(str(el).strip('[]'))
		f.write('\n')
	f.close()
	return True



data = data_generation(10000)
text_file(data)
print data
