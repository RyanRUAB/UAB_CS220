import time

#Setting the global variables so that they can be shared across the functions
timeg = 0
#The path of discovery
path = []
#The path of finishing
topopath = []
#Creates the vertex class so that I can keep track of the name, color, adjacent vertices,
#and the discovery / finish times
class Vertex:
	def __init__(self, name):
		self.name = name
		self.color = 'white'
		self.adjacent = []
		self.d = 0
		self.f = 0
	#This function allows for the adjacent vertices to be added 
	def addAdjacent(self, v):
		if v not in self.adjacent:
			self.adjacent.append(v)
#Creating a graph class with more extensive functions made keeping track of everything
#like individual vertices and edges much easier
class Graph:
	vertices = {}
	#This function builds a dictionary of vertices containing both the vertex name, its
	#number, and the actual Vertex class it is associated with
	def addV(self, vertex):
		if vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
	#This function is what allowed me to do the explore edge (u, v) part of the pseudocode
	def addE(self, u, v):
		if u in self.vertices and v in self.vertices:
			for i, j in self.vertices.items():
				print(i, j)
				
				if i == u:
					j.addAdjacent(v)
				if i == v:
					j.addAdjacent(u)
	#This was used for testing purposes	
	def verticesPrint(self):
		print(self.vertices)
	#This function shows the vertices as well as when they were discovered and finished
	#If there is no discovery or finish time then that vertex isn't a part of the graph
	def graphPrint(self):
		for i in self.vertices.keys():
			print("Vertex:", i, "Discovery:", self.vertices[i].d, "Finish:", self.vertices[i].f)
	#This is the primary DFS from the pseudocode, since the main DFS is built into the 
	#Vertex class this essentially just the DFS_Visit function
	def DFS_Visit(self, vertex):
		global timeg
		global path
		vertex.color = 'gray'
		timeg += 1
		#I set the discovery time after the increase so that it would index at 1 instead of 0
		vertex.d = timeg
		path.append(vertex.name)
		for v in vertex.adjacent:
			if self.vertices[v].color == 'white':
				self.DFS_Visit(self.vertices[v])
		vertex.color = 'black'
		timeg += 1
		vertex.f = timeg
		topopath.append(vertex.name)
	#Needed to make the second graph work, vertices was acting as a global variable not a class
	def verticesRemover(self):
		self.vertices = {}

#Modified file reader from previous labs, converts file into a dictionary
def fileReader(filename):
	file = open(filename, "r")
	graph = {}
	while True:
		line = file.readline()
		clean_line = line.strip()
		if not clean_line:
			break
		arraystring = clean_line.split(" ")
		try:
			vertex = int(arraystring[0])
			edge = int(arraystring[1])
		except IndexError:
			vertex = int(arraystring[0])
		try:
			graph.setdefault(vertex, []).append(edge)
		except UnboundLocalError:
			graph.setdefault(vertex)
		try:
			if edge not in graph.keys():
				graph.setdefault(edge, [])
		except UnboundLocalError:
			continue
	return graph
graphg = fileReader("mediumG.txt")

#Function that takes a given vertex and traces its path from the start vertex: set to 0 currently
def pathToVertex(endvertex):
	global path
	routeto = []
	if endvertex not in path:
		print("No path to end vertex")
		return
	else:
		print("The path from the start vertex to the end is:")
		for i in path:
			if i != endvertex:
				routeto.append(i)
			else:
				routeto.append(i)
				break
	return routeto

#Initializing the graph object
graph = Graph()

#Changing the start Vertex will change what vertex the pathing starts from. If a vertex
#is added that isn't in the graph then it will be created on its own and won't connect
#to anything else in the graph
start = Vertex(0)
graph.addV(start)

#Making the list of vertices first
for i in graphg.keys():
	graph.addV(Vertex(i))
#Applying the edges between the vertices second
for i in graphg.keys():
	for j in graphg[i]:
		if graphg[i] != []:
			graph.addE(i, j)
#The DFS function call to start the DFS process on the graph g
dfsstart = time.time_ns()
graph.DFS_Visit(start)
dfsend = time.time_ns()

#The call to print every vertex as well as its discovery and finish time
#uncomment if you would like to see the discovery and finish times yourself

#graph.graphPrint()

#Change the vertex here to change the final vertex in the path from 0
#print(pathToVertex(18))

#print("The DFS took", dfsend - dfsstart, "nanoseconds to run.")

#graph.verticesPrint()

#If you would like to see the full path uncomment the line below
#print(path)


#Everything for topological sort is below
#Resetting global variables for new graph
path = []
topopath = []
time = 0
graphdg = fileReader("tinyDG.txt")
dgraph = Graph()
dgraph.verticesRemover()
startdg = Vertex(0)
dgraph.addV(startdg)

for i in graphdg.keys():
	dgraph.addV(Vertex(i))
for i in graphdg.keys():
	for j in graphdg[i]:
		if graphdg[i] != []:
			dgraph.addE(i, j)

dgraph.DFS_Visit(startdg)
#print("Topological sort of tinyDG.txt", topopath)