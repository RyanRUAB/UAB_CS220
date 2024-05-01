from queue import PriorityQueue
import time

#Creates the vertex class so that I can keep track of the name, adjacent vertices, key,
#and parent vertices
class Vertex:
	def __init__(self, name):
		self.name = name
		self.adjacent = {}
		#Setting key to a million so I can still use < and > as python doesn't have infinity
		self.key = 1000000
		self.pi = None
		self.d = None
	#This function allows for the adjacent vertices to be added, now capable of adding weight
	def addAdjacent(self, v, w):
		if v not in self.adjacent.keys():
			self.adjacent[v] = w
#Creating a graph class with more extensive functions made keeping track of everything
#like individual vertices and edges much easier, also able to implement weights now
class Graph:
	vertices = {}
	#This function builds a dictionary of vertices containing both the vertex name, its
	#number, and the actual Vertex class it is associated with
	def addV(self, vertex):
		if vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
	#The same add edge function from lab 9 but with a weight requirement   
	def addE(self, u, v, w):
		if u in self.vertices and v in self.vertices:
			for i, j in self.vertices.items():
				if i == u:
					j.addAdjacent(v, w)
				if i == v:
					j.addAdjacent(u, w)
					
	def mstPrim(self, r):
		r = self.vertices[r]
		r.key = 0
		Q = PriorityQueue()
		for i, j in self.vertices.items():
			Q.put((j.key, i))		
		while Q.queue:
			u = Q.get()
			vertex = u[1]
			vertex = self.vertices[vertex]
			for v in vertex.adjacent.items():
				#the million is there cause it has to check the tuple
				if (1000000, v[0]) in Q.queue and v[1] < self.vertices[v[0]].key:
					self.vertices[v[0]].pi = u
					self.vertices[v[0]].key = v[1]
	def iss(self, s):
		for v in self.vertices.values():
			v.d = 1000000
			v.pi = None
		s.d = 0
	def relax(self, u, v, w):
		if v.d > u.d + w:
			v.d = u.d + w
			v.pi = u
	def dijkstra(self, w, s):
		self.iss(s)
		S = None
		Q = self.vertices


	#Using this so I could reuse the graph				
	def verticesRemover(self):
		self.vertices = {}							
	#This was used for testing purposes	
	def verticesPrint(self):
		print(self.vertices)
	#This is the adjancency list function used to print the mediumdg txt file
	def printAdjList(self):
		for i, j in self.vertices.items():
			print(i, list(j.adjacent.items()))

#Repurposed file reader from other labs, makes tuples instead of dictionaries this time
def fileReader(filename):
	file = open(filename, "r")
	graph = []
	while True:
		line = file.readline()
		clean_line = line.strip()
		if not clean_line:
			break
		clean_line = " ".join(clean_line.split())
		arraystring = clean_line.split(" ")
		try:
			vertex = int(arraystring[0])
			edge = int(arraystring[1])
			weight = float(arraystring[2])
		except IndexError:
			vertex = int(arraystring[0])
		try:
			graph.append((vertex, edge, weight))
		except UnboundLocalError:
			graph.append((vertex))
	return graph

xtralargedg = fileReader("XtraLargeDG.txt")
largedg = fileReader("largeDG.txt")
mediumdg = fileReader("mediumDG.txt")
tinydg = fileReader("tinyDG-1.txt")
prelabmst = fileReader("prelab-MST.txt")

graph = Graph()

#Intializing vertices in graph class
for i in mediumdg:
	try:
		graph.addV(Vertex(i[0]))
		if i[1] not in graph.vertices.keys():
			graph.addV(Vertex(i[1]))
	except TypeError:
		continue
for i in mediumdg:
	try:
		graph.addE(i[0], i[1], i[2])
	except TypeError:
		continue

graph.printAdjList()

startmed = time.time_ns()
graph.mstPrim(0)
endmed = time.time_ns()
print("It took", endmed-startmed, "nanoseconds for the med MST-Prim to run.")

graph.verticesRemover()

for i in largedg:
	try:
		graph.addV(Vertex(i[0]))
		if i[1] not in graph.vertices.keys():
			graph.addV(Vertex(i[1]))
	except TypeError:
		continue
for i in largedg:
	try:
		graph.addE(i[0], i[1], i[2])
	except TypeError:
		continue

startlarge = time.time_ns()
graph.mstPrim(0)
endlarge = time.time_ns()
print("It took", endlarge-startlarge, "nanoseconds for the large MST-Prim to run.")

graph.verticesRemover()

for i in xtralargedg:
	try:
		graph.addV(Vertex(i[0]))
		if i[1] not in graph.vertices.keys():
			graph.addV(Vertex(i[1]))
	except TypeError:
		continue
for i in xtralargedg:
	try:
		graph.addE(i[0], i[1], i[2])
	except TypeError:
		continue

startxtralarge = time.time_ns()
graph.mstPrim(0)
endxtralarge = time.time_ns()
print("It took", endxtralarge-startxtralarge, "nanoseconds for the extra large MST-Prim to run.")

