import sys, resource, time

sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

SCCFILE = 'SCC.txt'

t = 0
s = None

class Graph:
	def __init__(self, n):
		self.n = n
		self.connections = {}
		self.reverse_connections = {}

		for i in range(n):
			self.connections[i] = []
			self.reverse_connections[i] = []

	def connect(self, from_node, to_node):
		self.connections[from_node].append(to_node)
		self.reverse_connections[to_node].append(from_node)
	
	def DFS_scc(self, i, explored, finishing_times, leaders, is_reversed):
		global t
		global s
		explored[i] = True
		
		if not is_reversed: # second loop
			connections = self.connections
			leaders[i] = s
		else:
			connections = self.reverse_connections
				
		for connection in connections[i]:
			if not explored[connection]:
				self.DFS_scc(connection, explored, finishing_times, leaders, is_reversed)
		
		if is_reversed:
			finishing_times[t] = i
			t += 1
				

	def calculate_SCCs(self, leaders):
		SCCs = {}
		for node in leaders:
			if node in SCCs:
				SCCs[node] += 1
			else:
				SCCs[node] = 1

		return SCCs

	def get_largest_SCCs_sizes(self):
		global t
		global s
		explored = [False]*self.n # position i is a boolean telling whether that node has been explored
		finishing_times = [-1]*self.n
		leaders = [-1]*self.n

		for i in range(self.n - 1, -1, -1):
			if not explored[i]:
				self.DFS_scc(i, explored, finishing_times, leaders, True)

		explored = [False]*self.n
		leader = True
		for time in range(len(finishing_times) - 1, -1, -1):
			if not explored[finishing_times[time]]:
				s = finishing_times[time]
				self.DFS_scc(finishing_times[time], explored, finishing_times, leaders, False)

		largest_SCCs = []
		SCCs = list(self.calculate_SCCs(leaders).values())
		for i in range(5):
			SCC = max(SCCs)
			largest_SCCs.append(SCC)
			SCCs.remove(SCC)

		return largest_SCCs

def load_graph(file, graph):
	with open(file, 'r') as connections:
		for line in connections.readlines():
			from_node, to_node = list(map(int, line.split()))
			graph.connect(from_node - 1, to_node - 1)

if __name__ == '__main__':
	graph = Graph(875714)
	load_graph(SCCFILE, graph)
	print(graph.get_largest_SCCs_sizes())
