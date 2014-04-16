""" A graph, implemented using an array of lists.
Parallel edges and self-loops are permitted.
The <tt>Digraph</tt> class represents an directed graph of vertices
named 0 through V-1.
It supports the following operations: add an edge to the graph,
iterate over all of the neighbors incident to a vertex.
Parallel edges and self-loops are permitted.
<p>
For additional documentation,
see <a href="http://algs4.cs.princeton.edu/42directed">Section 4.2</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""
import os
class Digraph(object):
    """A graph, implemented using an array of lists"""
    def __init__(self, vertices_count=0):
        #self.vertices_size = None
        #self.N = None
        if vertices_count < 0:
            raise Exception("Number of vertices in a Digraph must be nonnegative")
        self.edges_count = 0
        self.adj = map(lambda x:[], range(vertices_count))

    def count_vertices(self):
        """return number of vertices (nodes)"""
        return len(self.adj)

    def count_edges(self):
        """Return number of edges (links between nodes)"""
        return  self.edges_count

    def add_vertice(self):
        """Adds a new node to the digraph"""
        self.adj.append([])

    def add_edge(self, index_from, index_to):
        """Add the directed edge v->w to the digraph."""
        vertices_count = self.count_vertices()
        for tmp in [index_from, index_to]:
            if tmp < 0 or tmp >= vertices_count:
                raise Exception("vertex %s is not between 0 and %s" %  (index_from, vertices_count-1))
        self.adj[index_from].insert(0, index_to)
        self.edges_count += 1

    def reverse(self) :
        """Return the reverse of the digraph."""
        vertices_count = self.count_vertices()
        reversed_digraph = Digraph(vertices_count)
        for index_from in range(vertices_count):
            for index_to in self.adj[index_from]:
                reversed_digraph.add_edge(index_to, index_from)
        return reversed_digraph

    def links(self, index_from):
        return self.adj[index_from]

    def __str__(self):
        s = ""
        NEWLINE = os.linesep
        vertices_count = self.count_vertices()
        s+=str(vertices_count) + " vertices, " + str(self.edges_count) + " edges " + NEWLINE
        for v in range(vertices_count):
            print "v", v
            s+="%d: " % v
            for w in self.adj[v]:
                s+="%d " % w
            s+=NEWLINE
        return s
    

