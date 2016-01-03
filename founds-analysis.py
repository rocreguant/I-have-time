#!/usr/bin/env python
# coding: utf8
__author__ = 'roc'


import GPy 
from matplotlib import pyplot as pb
import numpy as np


__DATASET_FOLDER__ 		= '/home/roc/workspace/I-have-time/founds-dataset/'
__DATASET_FILES__ 		= [ '*CXBorsaDividends','*CXFonsTresorLlargTermini',
                          '*CXMultiactiu30','*CXMultiactiu100', '*CXRendaFixaInternacional']
__DATASET_EXTENSION__ = '.csv'
__SAMPLE_LENGTH__		= 50

for _file in __DATASET_FILES__:
  f = open(__DATASET_FOLDER__+_file+__DATASET_EXTENSION__, 'r')
  X = np.ndarray(0)
  Y = np.ndarray(0)
  
  #first row is the header
  for row in f:
    break
  for row in f:
    aux = row.split(';')
    X = np.append(X,aux[0][0:10])
    Y = np.append(Y,float(aux[1].replace(',','.')))
    
  X = X[::-1]
  Y = Y[::-1]
  exit()
