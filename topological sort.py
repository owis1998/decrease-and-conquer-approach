def algorithm(graph):
	visited_vertices = []
	def fn():
		for lst in graph.get_all_vertices():
			if lst.peekFirst() in visited_vertices:
				continue

			for ver in lst.getAll():
				if ver == lst.peekFirst() or graph.connected(ver, lst, dircted = True):
					continue
			else:
				visited_vertices.append(lst.peekFirst())
				return fn()

	fn()
	return visited_vertices
