from operator import attrgetter
from graphics import *
import time



win = GraphWin('Graph', 1200, 600)
win.setBackground("white") 

coordinatesX = []
coordinatesY = []

def symmetry4foldXY(x,X,y,Y):
    #pt=Point(X+x,Y+y)
    coordinatesX.append(X+x)
    coordinatesY.append(Y+y)
    #pt.draw(win)
    #pt=Point(X-x,Y-y)
    coordinatesX.append(X-x)
    coordinatesY.append(Y-y)
    #pt.draw(win)
    #pt=Point(X-x,Y+y)
    coordinatesX.append(X-x)
    coordinatesY.append(Y+y)
    #pt.draw(win)
    #pt=Point(X+x,Y-y)
    coordinatesX.append(X+x)
    coordinatesY.append(Y-y)
    #pt.draw(win)

def ellipse(a,b,X,Y,gap):
    sa=a*a
    sb=b*b
    d=sb+sa*(0.25-b)
    x=0
    y=b
    
    k=0
    
    while sa*(y-0.5)>sb*(x+1):
        Q=sb*(2*x+3)
        if d<0:
            d+=Q
        else :
            d+=Q+2*sa*(1-y)
            y-=1
        x+=1
        
        if k is gap :
            symmetry4foldXY(x,X,y,Y)
            k=0
        else :
            k += 1
        
        
    k = 0
    sqXn=(x+0.5)**2
    sqYn=(y-1)**2
    d=(sb*sqXn)+(sa*sqYn)-(sa*sb)

    while y >= 0:
        Q=sa*(3-2*y)
        if d<0:
            d+=Q+2*sb*(x+1)
            x+=1
        else:
            d+=Q
        y-=1
        
        if k is gap :
            symmetry4foldXY(x,X,y,Y)
            k=0
        else :
            k += 1

        
ellipse(190,160,250,200,50)    

#defining the size of graph maxsize (11) for drawing purpose
size = 11





class Edge(object):
    def __init__(self,From,To,Weight):
        self.From = From
        self.To = To
        self.Weight = Weight
        
class Vertex(object):
    def __init__(self,Node_ID):
        self.Node_ID = Node_ID
        self.Parent_ID = -1
        self.AdjecencyList = []
        self.minDistance = 1000
        
		
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

    #strictly Ascending
    def addEdgeUndirList(self,start,end,Weight):
        if end < self.size :
            for i in range(start,end):
                self.addEdgeUndir(i,i+1,Weight)	
		
    def BFS(self,src):
        Queue = []
        visited = [0]*self.size
        Queue.append(self.VertexList[src])
        visited[src] = 1
        path = []

        step = 0 
              
        while (len(Queue) is not 0):
            u = Queue.pop(0)
            path.append(u.Node_ID)
         
            time.sleep(1)

            i=u.Node_ID
            pt = Point(coordinatesX[i],coordinatesY[i])
            cir = Circle(pt, 15)
            cir.setOutline('red')
            cir.setFill('green')
            cir.draw(win)
            
            label = Text(pt, i)
            label.setSize(18)
            label.setStyle("bold")
            
            label.draw(win)

            pt = Point(150+step,450)
            label = Text(pt, i)
            label.setSize(18)
            label.setStyle("bold")
            label.draw(win)

            step += 30
                                            
            for i in range (0,len(u.AdjecencyList)):
                x = u.AdjecencyList[i].To
                if visited[x] is 0:
                   visited[x] = 1
                   Queue.append(self.VertexList[x])

        return path           

	
    def DFS(self,src):
       Stack = []
       Stack.append(self.VertexList[src])
       visited = [0]*self.size
       visited[src] = 1

       path = []
       step = 0
                 
       while (len(Stack) is not 0):
           u = Stack.pop(len(Stack)-1)
           path.append(u.Node_ID)

           time.sleep(1)

           i=u.Node_ID
           pt = Point(coordinatesX[i],coordinatesY[i])
           cir = Circle(pt, 15)
           cir.setOutline('red')
           cir.setFill('green')
           cir.draw(win)
            
           label = Text(pt, i)
           label.setSize(18)
           label.setStyle("bold")
            
           label.draw(win)

           pt = Point(150+step,450)
           label = Text(pt, i)
           label.setSize(18)
           label.setStyle("bold")
           label.draw(win)

           step += 30
                                                   
           for i in range (0,len(u.AdjecencyList)):
               x = u.AdjecencyList[i].To
               if visited[x] is 0:
                   visited[x] = 1
                   Stack.append(self.VertexList[x])
       return path            	


    


    def DLS(self,src,limit):
       Stack = []
       visited = [0]*self.size   
       
       depth = -1
       
       Stack.append(self.VertexList[src])
       visited[src] = 1
       depth += 1

       path = []
       step = 0
       
                 
       while (len(Stack) is not 0):
           u = Stack.pop(len(Stack)-1)
           path.append(u.Node_ID)
           depth-=1

           time.sleep(1)

           i=u.Node_ID
           pt = Point(coordinatesX[i],coordinatesY[i])
           cir = Circle(pt, 15)
           cir.setOutline('red')
           cir.setFill('green')
           cir.draw(win)
            
           label = Text(pt, i)
           label.setSize(18)
           label.setStyle("bold")
            
           label.draw(win)

           pt = Point(150+step,450)
           label = Text(pt, i)
           label.setSize(18)
           label.setStyle("bold")
           label.draw(win)

           step += 30

           if depth < limit:
                                                   
               for i in range (0,len(u.AdjecencyList)):
                   x = u.AdjecencyList[i].To
                   if visited[x] is 0:
                       visited[x] = 1
                       Stack.append(self.VertexList[x])
                       depth+=1
       return path

    def DLSforItr(self,src,visited,limit,stepY):
        Stack = []
        depth = -1
        stepX = 0
       
        Stack.append(self.VertexList[src])
        visited[src] = 1
        depth += 1

        path = []

        while (len(Stack) is not 0):
           u = Stack.pop(len(Stack)-1)
           path.append(u.Node_ID)

           depth-=1

           time.sleep(1)

           i = u.Node_ID
           
           pt = Point(coordinatesX[i],coordinatesY[i])
           cir = Circle(pt, 15)
           cir.setOutline('red')
           cir.setFill('green')
           cir.draw(win)
            
           label = Text(pt, i)
           label.setSize(18)
           label.setStyle("bold")
           label.draw(win)

           pt = Point(230+stepX,450+stepY)
           label = Text(pt, i)
           label.setSize(11)
           label.setStyle("bold")
           label.draw(win)

           stepX += 30

           if depth < limit:
               for i in range (0,len(u.AdjecencyList)):
                   x = u.AdjecencyList[i].To
                   if visited[x] is 0:
                       visited[x] = 1
                       Stack.append(self.VertexList[x])
        return path   
        

        
    
    def DFSItr(self,src,limit):
        stepY = 0        
        visited = [0]*self.size
        
        for i in range(0,self.size):
            if visited[i] is 0:

                print self.DLSforItr(i,visited,limit,stepY)
                stepY += 18
                pt = Point(190,432+stepY)
                string ="Source "+str(i)+" :  "
                label = Text(pt, string)
                label.setSize(11)
                label.setStyle("bold")
                label.draw(win)


    def allpathDFS(self,src,dest):
        
        Stack = []
        Stack.append(self.VertexList[src])

        visited = [0] * self.size
       
        visited[src] = 1

        path = []

        stepY = 0

        countPath = 0
        
                 
        while (len(Stack) is not 0):
            u = Stack.pop(len(Stack)-1)
            path.append(u.Node_ID)

            if u.Node_ID is dest:
                print path

                #Drawing Paths
                stepX = 0

                for i in range(0,len(path)):

                    time.sleep(1)

                    pt = Point(coordinatesX[path[i]],coordinatesY[path[i]])

                    cir = Circle(pt, 15)
                    cir.setOutline('red')

                    if countPath is 0:
                        cir.setFill('green')

                    if countPath is 1:
                        cir.setFill('pink')

                    if countPath is 2:
                        cir.setFill('skyblue')
                        
                      

                    cir.draw(win)
                    
                    label = Text(pt, path[i])
                    label.setSize(18)
                    label.setStyle("bold")
                    label.draw(win)
                    
                    pt = Point(230+stepX,450+stepY)
                    label = Text(pt, path[i])
                    label.setSize(11)
                    label.setStyle("bold")
                    label.draw(win)

                    stepX += 30
                    
                                        
                
                #Set the current unvisited
                path.pop(len(path)-1)
                visited[u.Node_ID]=0

                stepY += 18
                countPath += 1
                time.sleep(4)

                # reset the color

                if countPath is 3:
                    countPath = 0

              
            else:
                
                for i in range (0,len(u.AdjecencyList)):
                    x = u.AdjecencyList[i].To
                    if visited[x] is 0:
                        visited[x] = 1
                        Stack.append(self.VertexList[x])


    def Dijkstra(self,src,dest):

        Queue = []

        pt = Point(500,10)
        label = Text(pt,"Node ID ")
        label.setSize(14)
        label.setStyle("bold")
        label.draw(win)
        
        pt = Point(600,10)
        label = Text(pt,"Parent ID ")
        label.setSize(14)
        label.setStyle("bold")
        label.draw(win)

        pt = Point(700,15)
        label = Text(pt,"Minimum\n Distance ")
        label.setSize(11)
        label.setStyle("bold")
        label.draw(win)
       
  
        Queue.append(self.VertexList[src])
        self.VertexList[src].minDistance = 0
        step = 0

        coordinateY = []

        for i in range(0,self.size):
            pt = Point(500,50+step)
            label = Text(pt, i)
            label.setSize(18)
            label.setStyle("bold")
            label.draw(win)
            step += 30
            coordinateY.append(20+step)
       
        step = 0      

        while (len(Queue) is not 0):
            
            Queue = sorted(Queue , key = attrgetter('minDistance'))
            u = Queue.pop(0)
            
            time.sleep(0.5)
            i = u.Node_ID
            
            pt = Point(600,coordinateY[i])
            label = Text(pt, u.Parent_ID)
            label.setSize(18)
            label.setStyle("bold")
            label.draw(win)

            pt = Point(700,coordinateY[i])
            
            label = Text(pt, u.minDistance)
            label.setSize(18)
            label.setStyle("bold")

            if i is dest:
                label.setTextColor("blue")

            label.draw(win)

            pt = Point(coordinatesX[i],coordinatesY[i])
            cir = Circle(pt, 15)
            cir.setOutline('red')
            cir.setFill('green')
            cir.draw(win)

            label = Text(pt, i)
            label.setSize(18)
            label.setStyle("bold")
            label.draw(win)

            step += 30
          
                                            
            for i in range(0,len(u.AdjecencyList)):

                v = u.AdjecencyList[i].To
                alt = u.minDistance + u.AdjecencyList[i].Weight
                                
                if(alt < self.VertexList[v].minDistance):
                    self.VertexList[v].minDistance = alt
                    self.VertexList[v].Parent_ID = u.Node_ID

                    Queue.append(self.VertexList[v])

        j = dest
        print "Destination ID: ",dest

        path = []
        
        while( j != -1 ):

            path.append(j)
                        
            j = self.VertexList[j].Parent_ID

        path.reverse()

        print path

        stepX = 0

        pt = Point(450+stepX,500)
        text=" Shortest Path Using Dijkstra"
        label = Text(pt,text)
        label.setSize(15)
        label.setStyle("bold")
        label.draw(win)

        for i in range(0,len(path)):

            time.sleep(2)
            pt = Point(coordinatesX[path[i]],coordinatesY[path[i]])
            if i < len(path)-1:
                
                pt2 = Point(coordinatesX[path[i+1]],coordinatesY[path[i+1]])
                line = Line(pt,pt2)
                line.setOutline('red')
                line.draw(win)

            
            cir = Circle(pt, 15)
            cir.setOutline('red')
            cir.setFill('skyblue')
            cir.draw(win)

            label = Text(pt, path[i])
            label.setSize(18)
            label.setStyle("bold")
            label.draw(win)

            pt = Point(350+stepX,540)
            text = str(path[i])+" -> "
            label = Text(pt,text)
            label.setSize(15)
            label.setStyle("bold")
            label.draw(win)

            stepX += 50
   

    #def primMST(self,src):
        
               
        


from random import randint



g = Graph(size)
# Drawing the Graph
for i in range(0,size): 

    pt = Point(coordinatesX[i],coordinatesY[i])
    cir = Circle(pt, 13)
    cir.setOutline('red')
    cir.setFill('yellow')
    cir.draw(win)
 
    label = Text(pt, i)
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)


temp = []

text = "\t\tUndirected Edge \t      Weight" 
label = Text(Point(840,10),text)
label.setSize(11)
label.setStyle("bold")
label.draw(win)
# random distribution of edges of Graph
step=0
for i in range(0,size*2):
    i = randint(0,size-1)
    j = randint(0,size-1)
    W = randint(0,size-1)
    
    x = str(i)
    y = str(j)
    comma=","
    current = x+comma+y
    
    
    if( (i != j) and ((current in temp) is False)):
        g.addEdgeUndir(i,j,W)

        line = Line(Point(coordinatesX[i],coordinatesY[i]), Point(coordinatesX[j],coordinatesY[j]))
        line.setOutline('blue')
        line.draw(win)

        text = "\t ("+str(i)+","+str(j)+ ") \t\t" +str(W)
        pt = Point(900,40+step)
        label = Text(pt,text)
        label.setSize(9)
        label.setStyle("bold")
        label.draw(win)

        step+=20

        current += " " 
        temp.append(current)

# end
        
# Printing Adjecency Matrix

for i in range(0,size):
    x = []
    for j in range(0,len(g.VertexList[i].AdjecencyList)):
        x.append(g.VertexList[i].AdjecencyList[j].To)
    print "ID -> {",i,"}",x

i = randint(0,size-1)
print "\nSource_ID ->",i

# Choose Your Algo
Choice = 5

SelectBFS = 0
SelectDFS = 1
SelectDLS = 2
SelectItrDFS = 3
SelectDFSPathGen = 4
SelectDijkstra = 5
SelectPrim = 6



if Choice is not 3:
    pt = Point(60,400)
    label = Text(pt," Source = ")
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)
    src = str(i)+":"
    pt = Point(130,400)
    label = Text(pt,src)
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)

    

if Choice is SelectBFS:
    
    pt = Point(60,450)
    label = Text(pt," BFS = ")
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)
    print "\nBreadth First Search ",g.BFS(i)

if Choice is SelectDFS:
    
    pt = Point(60,450)
    label = Text(pt," DFS = ")
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)
    print "\nDepth First Search ",g.DFS(i)

if Choice is SelectDLS:
    MaxDepth = 1
    pt = Point(70,450)
    
    dp = " DLS\n (MaxDepth = "
    dp += str(MaxDepth)+") "
    label = Text(pt,dp)
    label.setSize(13)
    label.setStyle("bold")
    label.draw(win)
    print "\nDepth Limited Search ",g.DLS(i,MaxDepth)

if Choice is SelectItrDFS:
    MaxDepth = 0
    pt = Point(70,450)
    
    dp = " Iterative DFS\n (MaxDepth = "
    dp += str(MaxDepth)+") "
    label = Text(pt,dp)
    label.setSize(13)
    label.setStyle("bold")
    label.draw(win)
    print "\nIterative DFS "
    g.DFSItr(i,MaxDepth-1)

j = randint(0,size-1)

if Choice is SelectDFSPathGen:
    pt = Point(90,450)

    label = Text(pt,"All Path using DFS = ")
    label.setSize(11)
    label.setStyle("bold")
    label.draw(win)
    
   

    pt = Point(85,420)
    label = Text(pt," Destination = ")
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)
    src = str(j)+":"

    pt = Point(180,420)
    label = Text(pt,src)
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)

    print "\nGenerating All Path using DFS "
    g.allpathDFS(i,j)

if Choice is SelectDijkstra:
    
    pt = Point(95,440)
    Dest = "Destination = "+str(j)
    label = Text(pt,Dest)
    label.setSize(18)
    label.setStyle("bold")
    label.draw(win)

    g.Dijkstra(i,j)

if Choice is SelectPrim:
    g.primMST(i)
    



win.getMouse()
win.close() 	
		
	






	
