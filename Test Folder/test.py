class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	time = 0
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in self.vertices.keys():
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
		vertex.color = 'blue'
		vertex.finish = time
		time += 1
		
	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)
			
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('0')
g.add_vertex(a)
g.add_vertex(Vertex('1'))
g.add_vertex(Vertex('2'))
g.add_vertex(Vertex('3'))
g.add_vertex(Vertex('4'))
g.add_vertex(Vertex('5'))
g.add_vertex(Vertex('6'))
g.add_vertex(Vertex('7'))
g.add_vertex(Vertex('8'))
g.add_vertex(Vertex('9'))

edges = ['01', '04', '15', '26', '34', '37', '47', '56', '58', '59', '69', '79']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.dfs(a)
g.print_graph()