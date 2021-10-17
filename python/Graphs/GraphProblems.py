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