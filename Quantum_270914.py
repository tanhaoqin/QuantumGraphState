# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 14:54:29 2014

@author: HanZikang & TanHaoQin
"""
import convert.py as cv
import itertools
import random
import numpy as np
class Quantum:
    """
    Initialization
    properties(non-capital initial): adMatrix, edgeList, dimension, qubitProperties, adjacencyMatrixUpdated, edgeListUpdated
    functions: EdgeListtoAdjacency, AdjacencytoEdgeList
    methods: AdMatrix, EdgeList, ZMeasurement, YMeasurement, update_edgelist, update_adjacencymatrix
    Errors: diagonalErrors
    """    
    def add_correction(self,index,correction):
        self.qubitProperties[index][1].append(correction)
        
    def remove_correction(self,index):
        self.qubitProperties[index][1]=[]
        
    def local_complement(self,index):
        neighbours=self.find_neighbours(index)
        for (s,t) in itertools.permutations(neighbours,2):
            if self.adMatrix[s][t]: self.adMatrix[s][t] = 0
            else: self.adMatrix[s][t] = 1
        self.adjacencyMatrixUpdated=True
        self.edgeListUpdated=False
        return self
        
    def update(self):
        if self.adjacencyMatrixUpdated and not self.edgeListUpdated:
            self.update_edgelist()
        elif self.edgeListUpdated and not self.adjacencyMatrixUpdated:
            self.update_adjacencymatrix()
            
    
    def update_edgelist(self):
        self.edgeList=cv.AdjacencytoEdgeList(self.adMatrix)
        self.edgeListUpdated=True
    
    def update_adjacencymatrix(self):
        self.adMatrix=cv.EdgeListtoAdjacency(self.edgeList,self.dim)
        self.adjacencyMatrixUpdated=True
    
    def remove_vertex(self,index):
        '''
        removing the index-corresponded vertex
        returns a class instance of quantum
        '''
        #removing from adjacency matrix and qubitProperties
        self.adMatrix=np.delete(np.delete(self.adMatrix,index,0),index,1)
        #creating another class instance as the measured state
        self.qubitProperties=self.qubitProperties[:index]+\
                            self.qubitProperties[index+1:]  #qubitProperties gets updated
        self.dim-=1
        
    def find_identifier(self, VertexNumber):
        '''
        locating the index number for the identifier chosen
        returns index
        '''
        for n in range(self.dim): 
        #finding the index with the identifier
            if self.qubitProperties[n][0]==VertexNumber:
                return n
        
    def find_neighbours(self,index):
        '''
        finding neighbours to the specified index
        returns a list
        '''
        neighbours=list(itertools.compress(range(self.dim),self.adMatrix[index]))
        return neighbours
        
    def find_mutual_neighbours(self,indexA,indexB):
        neighboursA=self.find_neighbours(indexA)
        neighboursB=self.find_neighbours(indexB)
        a=neighboursA+neighboursB
        a.sort()
        mutual=[a[i] for i in range(len(a)-1) if a[i]==a[i+1]]
        return mutual
        
    def choose_neighbour(self,neighbours):
        '''
        generate a random neighbour for user
        return a num
        '''
        return random.sample(neighbours,1)[0]
        
    def complement_neighbours(self,indexA,indexB):
        neighboursA=self.find_neighbours(indexA)
        neighboursB=self.find_neighbours(indexB)
        #Complement the neighbors of b with the neighbors of a
        set1=sorted([sorted(list(i)) for i in list(itertools.product(neighboursA,neighboursB))])
        set1=[s for s,t in itertools.groupby(set1)]
        #eliminating repeated pairs
        for s,t in set1:
            if s!=t:
                if self.adMatrix[s][t]:
                    self.adMatrix[s][t],self.adMatrix[t][s] = 0,0
                else:
                    self.adMatrix[s][t],self.adMatrix[t][s] = 1,1
        
    def __init__(self):
        pass

    def AdMatrix(self,adMatrix):
        # assuming input to be a list (matrix)
        adMatrix = np.array(adMatrix)
        #converting a list to an array
        assert adMatrix.shape[0] == adMatrix.shape[1],"Please insert a square matrix."         
        self.dim = adMatrix.shape[0]
        #defining the dimension property
        for r in range(self.dim):
            ##There is no entanglement between one vertex and itself(diagonals are not 1s)
            assert adMatrix[r][r]==0,"There should be no edges between a vertex and itself."
            
        #creating rest of the properties
        self.adMatrix = adMatrix
        self.qubitProperties = [[x,[]] for x in range(self.dim)]
        self.adjacencyMatrixUpdated = True
        self.edgeListUpdated = False

    def EdgeList(self,edgeList,dim):
            #checking for formatting errors
        for edge in edgeList:
            #An element in edgelist must be of length 2
            assert len(edge)==2, "Please insert a valid edgelist"
            #There is no entanglement between one vertex and itself
            assert edge[0]!=edge[1], "Please insert a valid edgelist"
        #dimension must be bigger than the largest mentioned index in the edgelist
        assert dim>=max([max(edge) for edge in edgeList])+1,"Please insert a valid dimension"

        #eliminating repeated entries in edgeLists
        [edge.sort() for edge in edgeList].sort()
        #arrange the edges themselves and altogether
        edgeList=[i for i,j in itertools.groupby(edgeList)]
        #eliminating repeated edges
        
        self.dim = dim
        self.qubitProperties = [[x,[]] for x in range(self.dim)]
        self.edgeList = edgeList
        self.adjacencyMatrixUpdated = False
        self.edgeListUpdated = True
        
    def __str__(self):
        #displaying the class instance:
        #adjacencyMatrix
        #edgelist
        self.update()
        return 'AdMatrix\n'+str(self.adMatrix)+'\nedgeList\n' \
            + str(self.edgeList) +'\ndimension  '+ str(self.dim)+'\n'
  
