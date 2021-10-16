from collections import deque

# This File shows how we can traverse a graph using BFS and DFS algos
# Stack for Dfs and Queue for BFS

#Source is the staring point
def depthFirstSearch(graph,source):
	stack = [source]

	while stack:
		current = stack.pop()
		print(current)
		neighbours = graph[current] # Getting all the neighbours of the current node
		for neighbour in neighbours:
			stack.append(neighbour)

def depthFirstSearchRecursive(graph,source):
	print(source)
	neighbours = graph[source]
	for neighbour in neighbours:
		depthFirstSearchRecursive(graph,neighbour)

# For BFS Recursive is mostly not possible

def breadthFirstSearch(graph,source):
	queue = deque()
	queue.appendleft(source)

	while queue:
		current = queue.pop()
		print(current)
		neighbours = graph[current] # Getting all the neighbours of the current node
		for neighbour in neighbours:
			queue.appendleft(neighbour)



if __name__ == '__main__':
	# The below is a example of directed graph structure and key is the node and values(list) is the possible neighbors
	graphs = {
		'a' : ['b','c'],
		'b' : ['d'],
		'c' : ['e'],
		'd' : ['f'],
		'e' : [],
		'f' : []
	}
	depthFirstSearch(graphs,'a')
	depthFirstSearchRecursive(graphs, 'a')
	breadthFirstSearch(graphs,'a')