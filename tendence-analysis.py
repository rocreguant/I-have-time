#!/usr/bin/env python
# coding: utf8
__author__ = 'roc'


import GPy 
from matplotlib import pyplot as pb
import numpy as np
import collections

__DATASET_FOLDER__ 		= '/home/roc/workspace/I-have-time/founds-dataset/'
__DATASET_FILES__ 		= [ '*CXBorsaDividends','*CXFonsTresorLlargTermini',
                          '*CXMultiactiu30','*CXMultiactiu100', '*CXRendaFixaInternacional']
__DATASET_EXTENSION__ = '.csv'
__SAMPLE_LENGTH__		= 10

me = 0
market = 0 
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
  
  print 'STARTING'
  #reversing the array    
  X = X[::-1]
  Y = Y[::-1]
  Y = Y[len(Y)-101:len(Y)-1]
  
  l = []
  count = 0
  money = 1000
  value = 0
  for i in range(len(Y)):
    try:
      b = Y[i] <= Y[i+1] #if grow
      if b:
        if count == 0:
          value = Y[i+2]
        count +=1
      else: #get lower
        l.append(count)
        if count >0 : #Making sure that I actualy have 'bought' stuff
          money = money * Y[i+2]/value
        print money
        count = 0
    except:
      print '\n'# out of range \n Money: '
      
  m = 1000*Y[len(Y)-1]/Y[0]
  print 'standard market: ',  m
  print 'Algorithm outperformance: ', money/m-1
  counter=collections.Counter(l)
  print counter
  print len(l)-counter[0]-counter[1]

