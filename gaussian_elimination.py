# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 14:52:12 2014

@author: Tan Hao Qin
"""
#this class is written to perform gaussian elimination on matrices

import clifford_algorithm
import numpy as np

def swap_rows(array,row1,row2):
    #swap two rows in a matrix
    temp = array[row1].copy()
    array[row1] = array[row2]
    array[row2] = temp

def multiply_row(array,row1,constant):
    #multiplies a row in a matrix by a constant
    array[row1] = array[row1]*constant
    

def row_addition(array,row1,row2,constant):
    #adds the second row multiplied by a constant into the first row
    array[row1] = array[row1]+constant*array[row2]

def find_non_zero_entry_in_column(array,column_index,startIndex = 0):
    #finds the first row in an array that has a non-zero entry at column j starting from row startIndex
    #returns row number
    m,n = array.shape
    for i in range(startIndex,m):
        if array[i][column_index] != 0:
            return i
    else:
        return -1
        
def ensure_all_other_row_entries_zero(array,row_index,column_index):
    x = np.transpose(array)[column_index].copy()
    for i in range(array.shape[0]):
        if i != row_index:  
            row_addition(array,i,row_index,-1*(float(x[i])/x[row_index]))            

def row_echelon_form(array):
    m,n = array.shape
    current_row = 0
    for current_column in range(n):
        entry = find_non_zero_entry_in_column(array,current_column,current_row)
        print "current_column : "+str(current_column)
        print "current_row : "+str(current_row)
        print "first_non_zero_entry : " + str(find_non_zero_entry_in_column(array,current_column,current_row)) 
        if  entry != -1:
            if entry != current_row:
                swap_rows(array,find_non_zero_entry_in_column(array,current_column,current_row),current_row)
                entry = current_row                
                print "swap"                
                print array
            if array[current_row][current_column] != 1:
                multiply_row(array,current_row,float(1)/array[current_row][current_column])
                print "divide"
                print array
            ensure_all_other_row_entries_zero(array,current_row,current_column)
            print "minus"            
            print array            
            current_row+=1
            

def parse_ref(array):
    var = {0:"a",1:"b",2:"c",3:"d"}
    m,n = array.shape    
    k = n/4
    print k
    count = [np.count_nonzero(array[i]) for i in range(m)]
    for i in range(m):
        if count[i] == 1:
            print var[int(np.nonzero(array[i])[0]/k)]+str(int(np.nonzero(array[i])[0]%k))
            #print "Variable"+var_name+" = 0"
        elif count[i] != 0:
            output_string = ""
            for j in range(count[i]):
                identifier = np.nonzero(array[i])[0][j]
                output_string+=var[int(identifier)/k]+str(int(identifier)%k)
                if j != count[i]-1:
                    output_string+=" + "
                else:
                    output_string+=" = 0"
            print output_string

def gaussian_elimination(array):
    rref = row_echelon_form(matA)     





        
matA = np.array([[1,2],[3,4]]).astype(float)
swap_rows(matA,0,1)
assert (matA == np.array([[3,4],[1,2]])).all()
multiply_row(matA,0,2)
assert (matA == np.array([[6,8],[1,2]])).all()
row_addition(matA,0,1,-6)
assert (matA == np.array([[0,-4],[1,2]])).all()
assert find_non_zero_entry_in_column(matA,0)==1
swap_rows(matA,0,1)
assert find_non_zero_entry_in_column(matA,0,1)==-1
matA = np.array([[6,8],[1,2]]).astype(float)
ensure_all_other_row_entries_zero(matA,1,0)
assert (matA == np.array([[0,-4],[1,2]])).all()
print "Test Success"

matA = np.array([[0,1,0],[1,0,1],[0,1,0]])
matB = np.array([[0,1,1],[1,0,1],[1,1,0]])
matC = clifford_algorithm.generate_linear_systems(matA,matB)
print matC
row_echelon_form(matC)

matD = np.array([[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]])
parse_ref(matC)