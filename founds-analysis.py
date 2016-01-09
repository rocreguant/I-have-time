#!/usr/bin/env python
# coding: utf8
__author__ = 'roc'


import GPy 
from matplotlib import pyplot as pb
import numpy as np
import matplotlib


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

  #reversing the array    
  X = X[::-1]
  Y = Y[::-1]
  y = Y
  Y = Y[len(Y)-50:len(Y)-5] #

  kernel = GPy.kern.RBF(input_dim=1, lengthscale=5)
  m = GPy.models.GPRegression(np.array(range(len(Y-5)))[:, np.newaxis], Y[0:len(Y-5), np.newaxis], kernel)
  m.optimize()
  m.plot()
  matplotlib.pylab.show(block=True)
  
  aux = np.ndarray(4)
  aux[0] = len(Y-5)
  aux[1] = len(Y-5)+1
  aux[2] = len(Y-5)+2
  aux[3] = len(Y-5)+3
  prediction = m.predict(np.array(aux[:, np.newaxis])) 
  #print prediction
  
  totalvar = 0
  for va in prediction[1]:
    totalvar += va
  
  print 'prediction -- real'
  for i in range(len(prediction[0])):
    print prediction[0][i],'--', y[len(y)-5-1+i]
#  print Y[len(Y)-5:]#[len(Y-6):len(Y)-1]
    #varianceprint prediction[1][i]
  exit()
