from heapq import heappush, heappop

FILE = 'dijkstraData.txt'

def create_graph(file):
	adjacency_list = {}
	with open(file, 'r') as f:
		for line in f.readlines():
			line = line.strip().split('\t')
			vertex = int(line[0]) - 1
			adjacency_list[vertex] = []
			for edge in line[1:]:
				head, weight = [int(x) for x in edge.split(',')]
				adjacency_list[vertex].append((head - 1, weight))

	return adjacency_list


def recalculate_greedy_score(w, vertex, weight, greedy_scores, heap, vertex_heap_map, A, dead_scores):
	current_greedy_score = greedy_scores[vertex]
	if A[w] + weight < current_greedy_score:
		dead_scores[current_greedy_score] = True
		greedy_scores[vertex] = A[w] + weight
		heappush(heap, A[w] + weight)
		vertex_heap_map[A[w] + weight] = vertex


def insert_connections_into_heap(w, vertex, heap, weight, vertex_heap_map, greedy_scores, A, vertices_in_heap):
	heappush(heap, A[w] + weight)
	vertex_heap_map[A[w] + weight] = vertex
	vertices_in_heap[vertex] = True
	greedy_scores[vertex] = A[w] + weight


# what if greedy scores for two vertices are the same?
def insert_and_recalculate(w, heap, vertex_heap_map, vertices_in_heap, graph, A, greedy_scores, dead_scores):
	for edge in graph[w]:
		vertex, weight = edge
		if vertex in vertices_in_heap:
			recalculate_greedy_score(w, vertex, weight, greedy_scores, heap, vertex_heap_map, A, dead_scores)
		else:
			insert_connections_into_heap(w, vertex, heap, weight, vertex_heap_map, greedy_scores, A, vertices_in_heap)


def dijkstra(s, graph):
	dead_scores = {}
	A = [-1]*len(graph) # list of shortest paths from s
	heap = []
	vertex_heap_map = {}
	vertices_in_heap = {}
	greedy_scores = {}
	A[s] = 0

	# Put all vertices with tail s in heap with key being 
	# the score of the Dijkstra greedy criteria (0 + s-v length, 
	# in this case). Then map the score to the vertex in vertex_heap_map
	for edge in graph[s]:
		vertex, weight = edge
		insert_connections_into_heap(s, vertex, heap, weight, vertex_heap_map, greedy_scores, A, vertices_in_heap)
		
	while heap:
		score = heappop(heap)
		if score not in dead_scores:
			w = vertex_heap_map[score]
			A[w] = score
			vertices_in_heap[w] = False
			insert_and_recalculate(w, heap, vertex_heap_map, vertices_in_heap, graph, A, greedy_scores, dead_scores)

	return A


if __name__ == '__main__':
	graph = create_graph(FILE)
	shortest_paths = dijkstra(0, graph) # shortest paths starting from vertex 0
	# Answer is 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
	print('%d,%d,%d,%d,%d,%d,%d,%d,%d,%d' % (shortest_paths[6], 
		shortest_paths[36], shortest_paths[58], shortest_paths[81],
		shortest_paths[98], shortest_paths[114], shortest_paths[132],
		shortest_paths[164], shortest_paths[187], shortest_paths[196]))
