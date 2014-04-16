"""DFS for Digraph"""
class DepthFirstOrder:
    "Compute preorder and postorder for a digraph or edge-weighted digraph"
    def __init__(self, digraph):
        vertices_count = digraph.count_vertices()
        self.pre = [None] * vertices_count
        self.post = [None] * vertices_count
        self.preorder = []
        self.postorder = []
        self.precounter = 0
        self.postcounter = 0
        self.marked = [False] * vertices_count
        for vertice in range(vertices_count):
            if not self.marked[vertice]:
                self.dfs(digraph, vertice)

    def dfs(self, digraph, vertice):
        "DepthFirstSearch"
        self.marked[vertice] = True
        self.pre[vertice] = self.precounter
        self.precounter += 1
        self.preorder.append(vertice)
        for vertice_to in digraph.links(vertice):
            if not self.marked[vertice_to]:
                self.dfs(digraph, vertice_to)
        self.postorder.append(vertice)
        self.post[vertice] = self.postcounter
        self.postcounter += 1

    def reverse_postorder (self):
        reverse = []
        for i in self.postorder:
            reverse.insert(0, i)
        return reverse
