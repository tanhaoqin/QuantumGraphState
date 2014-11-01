#!usr/bin/python

import itertools
import numpy as np

def EdgeListtoAdjacency(edgeList,dim):
    #generating adjacency matrix from ground up
    Matrix = np.zeros((dim,dim),dtype=int)
    for edge in edgeList:
        Matrix[edge[0]][edge[1]]=1
        Matrix[edge[1]][edge[0]]=1
    return Matrix

def AdjacencytoEdgeList(Matrix):
    #matrix must be an array
    (n,n)=Matrix.shape
    edgeList=[[x,y] for x,y in itertools.combinations(range(n),2)
             if Matrix[x][y]]
    return edgeList

