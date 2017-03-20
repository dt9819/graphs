# Graph - Data Structure

'''

    class "Edge" contains information about
        Source Node ID
        Destination Node ID
        Weight between Source and Destination


'''
class Edge(object):
    def __init__(self,From,To,Weight):
        self.From = From
        self.To = To
        self.Weight = Weight

'''

    class "Vertex" contains information about
        Node ID 
        List of Adjecent Nodes 

        Also the information about the
        single source shortest path attributes
        like :
        
        Parent ID -  Parent of the Node if a source Node is given
        minDistance  -  Distance from the Source Node  
        

'''
        
        
class Vertex(object):
    def __init__(self,Node_ID):

        # Vertex Info
        self.Node_ID = Node_ID
        self.AdjecencyList = []

        # Shortest Path algo attributes
        
        self.Parent_ID = -1
        self.minDistance = 1000

'''

    class "Graph" contains information about
        size of graph
        List of Vertex

    class "Graph" performs :
        Initializtion of Vertex List
        Addition of Directed Egde
        Addition of Un Directed Edge

'''        
		
class Graph(object):
    def __init__(self,size):
        self.size = size
        self.VertexList = []
                
        for i in range (0,self.size):
            self.VertexList.append(Vertex(i))

 
    def addEdgedir(self,From,To,Weight):
        self.VertexList[From].AdjecencyList.append(Edge(From,To,Weight))

    def addEdgeUndir(self,From,To,Weight):
        self.addEdgedir(From,To,Weight)
        self.addEdgedir(To,From,Weight)



# Defining the Graph
size = 5
g = Graph(size)

g.addEdgeUndir(1,2,5)
g.addEdgedir(3,4,6)

        
# Printing Adjecency Matrix

for i in range(0,size):
    x = []
    for j in range(0,len(g.VertexList[i].AdjecencyList)):
        x.append(g.VertexList[i].AdjecencyList[j].To)
    print "ID -> {",i,"}",x

