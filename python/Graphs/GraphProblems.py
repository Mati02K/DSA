from collections import deque

# All the basic Graph Based Problems is covered here

# Given a Acyclic Graph check if it is possible to reach the destination from source
def hasPath(graph,src,dest):
	if src == dest:
		return True

	neighbours = graph[src]
	for neighbour in neighbours:
		if hasPath(graph,neighbour,dest): # Check if a neighbour can travel to the same path
			return True

	return False


# Given a undirected graph find a way is there is a possible route from src to dest

def undirectedPath(graph,src,dest,visited=set()):
	if src == dest:
		return True

	if src in visited:
		return False

	visited.add(src)
	neighbours = graph[src]

	for neighbour in neighbours:
		if undirectedPath(graph,neighbour,dest,visited):
			return True

	return False



# Temp function to create a graph from unordered pairs
def buildGraph(edges):
	graph = {}

	for edge in edges:
		# Considering there is only two elements in the edges
		a = edge[0]
		b = edge[1]

		if a not in graph:
			graph[a] = []
		if b not in graph:
			graph[b] = []

		graph[a].append(b)
		graph[b].append(a)

	return graph

#Counted Components
# Counted Components refers to group of nodes
def countConnectedComponents(graph):
	count = 0
	visited = set()
	for node in graph:
		if explore(graph,node,visited):
			count += 1

	return count

#Tmp function for above code to check if a node is visited in a graph
def explore(graph,current,visited):
	if current in visited:
		return False

	visited.add(current)

	neighbours = graph[current]

	for neighbour in neighbours:
		explore(graph,neighbour,visited)

	return True

# Shortest path from one node to another (return -1 if not exists)
# we are going to use BFS instead of DFS as DFS have to check all possible nodes with max counter
def shortestPath(edges,src,dest):
	graph = buildGraph(edges)
	visited = set()
	queue = deque()
	queue.appendleft([src,0]) # ---> [node,distance]

	while len(queue) > 0:
		node,distance = queue.pop()
		if node == dest:
			return distance

		neighbours = graph[node]
		for neighbour in neighbours:
			if neighbour not in visited:
				visited.add(neighbour)
				queue.appendleft([neighbour, distance+1])

	return -1

# Given a grid with land(L) and water(W) find the number of island
def islandCount(grid):
	visited = set()
	count = 0
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			if exploreIsland(grid,row,col,visited):
				count+=1

	return count

def exploreIsland(grid,row,col,visited):
	rowInbound = 0 <= row and row < len(grid)
	colInbound = 0 <= col and col < len(grid[0])

	if not rowInbound or not colInbound:
		return False

	if grid[row][col] == 'W': # Since it is a water no need to explore
		return False

	key = str(row) + ',' + str(col) # key for storing in set

	if key in visited:
		return False

	visited.add(key)

	#Start Exploring in all 4 directions
	exploreIsland(grid,row - 1,col,visited) #up
	exploreIsland(grid,row + 1,col,visited) #Down
	exploreIsland(grid,row,col - 1,visited) # left
	exploreIsland(grid,row,col + 1,visited) #right

	return True

if __name__ == '__main__':
	graph = {
		'f' : ['g','i'],
		'g' : ['h'],
		'h' : [],
		'i' : ['g','k'],
		'j' : ['i'],
		'k' : []
	}

	print(hasPath(graph,'f','k'))
    # Undirected Graph
	edges = [
		['i','j'],
		['k','i'],
		['m','k'],
		['k','l'],
		['o','n']
	]

	print(buildGraph(edges))
	graph = buildGraph(edges)
	print(undirectedPath(graph,'i', 'm'))

	connectedcomponentgraph = {
		0 : [8, 1, 5],
		1 : [0],
		5 : [0, 8],
		8 : [0, 5],
		2 : [3, 4],
		3 : [2, 4],
		4 : [3, 2]
	}
	print(countConnectedComponents(connectedcomponentgraph))

	edges = [
		['w','x'],
		['x','y'],
		['z','y'],
		['z','v'],
		['w','v']
	]

	print(shortestPath(edges,'w','z'))

	grid = [
		['W', 'L', 'W', 'W', 'W'],
		['W', 'L', 'W', 'W', 'W'],
		['W', 'W', 'W', 'L', 'W'],
		['W', 'W', 'L', 'L', 'W'],
		['L', 'W', 'W', 'L', 'L'],
		['L', 'L', 'W', 'W', 'W'],
	]
	print(islandCount(grid))