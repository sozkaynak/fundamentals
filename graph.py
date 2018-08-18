# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:54:31 2018

@author: www.sumeyyeozkaynak.me
"""
#--------------------------------------Graph Method---------------------------#
class Vertex:
    def __init__(self, key):
        self.id=key
        self.connectedTo={}
        
    #Köşe noktasından diğerine bağlantı eklemek için kullanılıyor.
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
        
    def __str__(self):
        return str(self.id)+ ' connectedTo: ' + str([x.id for x in self.connectedTo])
    #ConnectedTo değişkeniyle temsil edilen düğümün tüm komşularını listeler
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    #DDüğümün bağlı olduğu düğümler arasındaki kenarların ağırlıklarını döndürür.
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
     #Düğümleri bir birine bağlayan bir sözlük içerir.
class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
        
    def addVertex(self,key):
        self.numVertices= self.numVertices+1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        
    # Tüm düğümlerin adlarını listeler
    def getVertices(self):
        return self.vertList.keys()
    #Self-loop yapmayı sağladık.
    def __iter__(self):
        return iter(self.vertList.values())
    
g=Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)   

for v in g:
    for w in v.getConnections():
        print("(%s,%s)"%(v.getId(),w.getId()))
   
# -----------------------------Building the Word Ladder Graph-----------------#      
#from pythonds.graphs import Graph
def buildGraph(WordFile):
    d={}
    g=Graph()
    wfile=open(WordFile,'r')
    
    #Bir harf ile farklılık gösteren kelimelerinin grubunu oluşturur.
    for line in wfile:
        word =line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+ word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
                
    #Aynı kovadaki kelimeler için düğüm ve kenar oluşturur.
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)


    return g

print(g)


























