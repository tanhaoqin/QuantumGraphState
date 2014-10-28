# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 14:52:12 2014

@author: Tan Hao Qin
"""
#this class is written to perform gaussian elimination on matrices

import numpy as np

def find_max_entry_in_column(matrix,column):
    #returns row number
    return matrix.argmax(0)(0,column)

def gaussian_elimination(matA):
    print np.argmax(matA)[0]     


matA = np.matrix('1 1 2;0 1 -1')
print matA


print find_max_entry_in_column(matA,0)