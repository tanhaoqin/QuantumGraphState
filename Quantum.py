# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 14:54:29 2014

@author: HanZikang & TanHaoQin
"""
import itertools
import random
import numpy as np

def EdgeListtoAdjacency(edgeList,dim):
    Matrix = np.zeros((dim,dim),dtype=int)
    #AdMatrix=[[0 for _ in range(dim)] for _ in range(dim)]
    #transforming edgelist to adjacencymatrix
    for edge in edgeList:
        for n in [0,1]:
            Matrix[edge[n]][edge[not n]]=1
    return Matrix
    # returns an array

def AdjacencytoEdgeList(Matrix):
    #matrix must be an array
    (n,n)=Matrix.shape
    edgeList=[[x,y] for x,y in itertools.combinations(range(n),2)
             if Matrix[x][y]]
    return edgeList

def read_file():
    
class Quantum:
    ##Initialization
    ##properties(non-capital initial): adMatrix, edgeList, dimension, qubitProperties
    ##functions: EdgeListtoAdjacency, AdjacencytoEdgeList
    ##methods: AdMatrix, EdgeList, ZMeasurement, YMeasurement
    ##Errors: diagonalErrors

        
    def add_correction(self,index,correction):
        self.qubitProperties[index][1].append(correction)
        
    def remove_correction(self,index):
        self.qubitProperties[index][1]=[]
        
    def local_complement():
        
    def complement
    
    def update_edgelist(self):
        self.edgeList=AdjacencytoEdgeList(self.adMatrix)
    
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
        
    def choose_neighbour(self,neighbours):
        '''
        generate a random neighbour for user
        return a num
        '''
        return random.sample(neighbours,1)[0]
        
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
        self.edgeList = AdjacencytoEdgeList(self.adMatrix)
        

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
        self.adMatrix = EdgeListtoAdjacency(edgeList,dim)
        self.edgeList = edgeList
        
    def __str__(self):
        #displaying the class instance:
        #adjacencyMatrix
        #edgelist
        return 'AdMatrix\n'+str(self.adMatrix)+'\nedgeList\n' \
            + str(self.edgeList) +'\ndimension  '+ str(self.dim)+'\n'
    
    def Measurement(self,Axis,VertexNumber):
        '''
        Axis: 'X','Y','Z'
        '''
        index = self.find_identifier(VertexNumber)
        final_measurement={'X':0,'Y':1,'Z':2}[Axis]
        
        correctionTable=[[0,2,1],[2,1,0],[1,0,2]]
        for x in self.qubitProperties[index][1]:
            # x: corrections
            final_measurement=correctionTable[x][final_measurement]
        outp=Quantum()
        outp.AdMatrix(self.adMatrix)
        outp.qubitProprties=self.qubitProperties
        outp.remove_correction(index)
        return [outp.XMeasurement,outp.YMeasurement,outp.ZMeasurement][final_measurement](VertexNumber)
              
    def ZMeasurement(self,VertexNumber):
        '''
        performing z-measurement on quantum state 
        returns a class instance of quantum
        '''
        index = self.find_identifier(VertexNumber)
        self.remove_vertex(index)
        self.update_edgelist()
        return self
    
    def YMeasurement(self,VertexNumber):
        '''
        performing y-measurement on quantum state 
        returns a class instance of quantum
        '''
        index = self.find_identifier(VertexNumber)
        neighbours=self.find_neighbours(index)
        #complementing VertexNumber with its neighbours
        for (s,t) in itertools.permutations(neighbours,2):
            if self.adMatrix[s][t]: self.adMatrix[s][t] = 0
            else: self.adMatrix[s][t] = 1
        #tagging the appropriate vertexes with the Z-adjustment
        for s in neighbours:
            self.add_correction(s,2)
            
        self.remove_vertex(index)
        self.update_edgelist()
        return self

    def XMeasurement(self,VertexANumber):
        '''
        performing z-measurement on quantum state 
        returns a class instance of quantum
        '''
        indexA =self.find_identifier(VertexANumber)
        neighboursA=self.find_neighbours(indexA)
        indexB=self.choose_neighbour(neighboursA)
        print indexB
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
        #Complement the mutual neighbors of vertices a and b
        a=neighboursA+neighboursB
        a.sort()
        mutual=[a[i] for i in range(len(a)-1) if a[i]==a[i+1]]
        for i,j in itertools.permutations(mutual,2):
            if self.adMatrix[i][j]: self.adMatrix[i][j]=0
            else: self.adMatrix[i][j]=1
        #Complement vertex b with the neighbors (except b) of a
        neighboursA.remove(indexB)
        for i in neighboursA:
            if self.adMatrix[i][indexB]:
                self.adMatrix[i][indexB],self.adMatrix[indexB][i]=0,0
            else:
                self.adMatrix[i][indexB],self.adMatrix[indexB][i]=1,1
        self.remove_vertex(indexA)
        self.update_edgelist()
        return self
def test():

    #initialization
    e=[[0,4],[1,2],[1,4],[1,3],[1,0]]
    c = Quantum()                
    c.EdgeList(e,5)
    print c
    #Z measurement
    d=c.Measurement("Z",1)
    print d
    #Y measurement
    e=c.Measurement("Y",1)
    print e

    g=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
    h=Quantum()
    h.AdMatrix(g)
    print h
    i=h.Measurement("X",0)
    print i
    f=e.Measurement("Y",2)
    print f
    g=e.Measurement("X",2)
    print g
    print 'test pass'

#if __name__ == '__main__':
 #   test()
  #  print "hello world"

print test()
