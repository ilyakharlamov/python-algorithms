""" Finds a directed cycle in a digraph. Runs in O(E + V) time."""
class DirectedCycle(object):
    """ Finds a directed cycle in a digraph. Runs in O(E + V) time."""
    def __init__(self, digraph ):
        vertices_count = digraph.count_vertices()
        # marked[v] = has vertex v been marked?
        self.marked = [False] * vertices_count
        # is vertex on the stack?
        self.on_stack = [False] * vertices_count
        # edgeTo[v] = previous vertex on path to v
        self.edge_to = [0] * vertices_count 
        self.cycle = [] #
        for vertice in range(vertices_count):
            if not self.marked[vertice]:
                self.dfs(digraph, vertice)

    def dfs (self,  digraph, vertice ):
        """check that algorithm computes 
        either the topological order or finds a directed cycle"""
        self.on_stack[vertice] = True
        self.marked[vertice] = True
        for vertice_to in digraph.adj[vertice]:
            #short circuit if directed cycle found
            if len(self.cycle):
                return
            elif not self.marked[vertice_to]:
                self.edge_to[vertice_to] = vertice
                self.dfs(digraph, vertice_to)
            elif self.on_stack[vertice_to]: #trace back directed cycle
                self.cycle = []
                temp = vertice
                while temp != vertice_to:
                    self.cycle.append(temp)
                    temp = self.edge_to[temp]
                self.cycle.append(vertice_to)
                self.cycle.append(vertice)
        self.on_stack[vertice] = False

    def has_cycle(self):
        "has cycle"
        return len(self.cycle) > 0
