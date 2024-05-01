import time

class node:
     def __init__(self, vertex):
        self.vertex = vertex
        self.color = None
        self.d = None
        self.pi = None

class graph:
    def __init__(self, vertex, edge):
        self.V = vertex
        self.edge = edge
          
def BFS(G, s):    
    G.V.remove(s)
    for u in G.V:
        u = node(u)
        u.color = "white"
        u.d = float('inf')
        u.pi = None
    s = node(s)
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = []
    Q.append(s)
    while Q:
        u = Q[0]
        Q.pop(0)
        dict = G.edge
        try:
            for v in dict.get(u):
                print(v)
                if v.color == "white":
                    v.color = "gray"
                    v.d = u.d + 1
                    v.pi = u
                    Q.append(v)
        except TypeError:
            continue
        u.color = "black"

def printPath(G, s, v):
    if v == s:
        print(s)
    elif v.pi == None:
        print("No path from s to v exists")
    else:
        printPath(G, s, v.pi)
        print(v)


#Modified file reader from previous labs
def fileReader(filename):
    file = open(filename, "r")
    vertex = []
    edge = []
    while True:
        line = file.readline()
        if not line:
            break
        arraystring = line.split(" ")
        try:
            vertex.append(int(arraystring[0]))
            vertex.append(int(arraystring[1]))
        except IndexError:
            vertex.append(int(arraystring[0]))
        try:
            #accounts for single vertices with no edges
            if arraystring[1] is not None:
                edge.append(tuple([int(arraystring[0]), int(arraystring[1])]))
        except IndexError:
            continue
    #Python method of removing duplicates from vertices list by converting to a dictionary then back to a list
    vertexremove = list(dict.fromkeys(vertex))
    dictedge = dict()
    #Method of turning the edges into key value pairs where a single vertex can lead to various different ones
    for key, value in edge:
        dictedge.setdefault(key, []).append(value)
    #Two return values for both vertices of the graph and edges in the graph
    return vertexremove, dictedge

filelargegvertex, filelargegedge = fileReader("largeG.txt")
filemediumgvertex, filemediumgedge = fileReader("mediumG-1.txt")

#initializing the files as the graph class
mediumg = graph(filemediumgvertex, filemediumgedge)
largeg = graph(filelargegvertex, filelargegedge)

#print(mediumg.edge)
#Creating a BFS by starting from the first given vertex
startmed = time.time_ns()
BFS(mediumg, mediumg.V[0])
endmed = time.time_ns()

startlarge = time.time_ns()
BFS(largeg, largeg.V[0])
endlarge = time.time_ns()

print("The time for the BFS of the medium file is", endmed-startmed, "nanoseconds")
print("The time for the BFS of the large file is", endlarge-startlarge, "nanoseconds")


#printPath(mediumg, 246, mediumg.V[2])

