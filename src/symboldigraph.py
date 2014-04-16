"""Like digraph but operates with strings"""
from digraph import Digraph

class SymbolDigraph(object):
    """Like digraph but operates with strings, you can never remove edges"""
    def __init__(self):
        self.symboltable = {}
        self.names=[]
        self.digraph = Digraph()

    def add_vertice(self, edge_from):
        """Add named vertice"""
        index_from = self._check_index(edge_from)
        self._check_digraph_size(index_from)
        self.names[index_from] = edge_from

    def add_edge(self, edge_from, edge_to):
        """Add named edge link"""
        index_from = self._check_index(edge_from)
        index_to = self._check_index(edge_to)
        self._check_digraph_size(max(index_from, index_to))
        self.digraph.add_edge(index_from, index_to)

    def _check_index(self, key):
        """if exists, returns id, otherwise adds a new one and also returns"""
        keyname = str(key)
        #print "_check_index", key, "len(keyname)", len(keyname)
        if key == None or not(len(keyname)):
            raise Exception("Edge name cannot be none")
        if self.index(keyname) == -1:
            index = len(self.symboltable)
            self.symboltable[keyname] = index
            self._check_names_size(index)
            self.names[index] = key
        return self.symboltable[keyname]

    def index(self, key):
        """returns internal index by key"""
        if self.symboltable.has_key(key):
            return self.symboltable[key]
        return -1

    def _check_digraph_size(self, index):
        """resizes graph accordingly"""
        i = index - self.digraph.count_vertices()
        while i >= 0:
            self.digraph.add_vertice()
            i -= 1

    def _check_names_size(self, index):
        """resizes graph accordingly"""
        i = index - len(self.names)
        while i >= 0:
            self.names.append(None)
            i -= 1

    def count_vertices(self):
        """returns number of vertices (nodes)"""
        return self.digraph.count_vertices()

    def count_edges(self):
        """returns number of edges(links)"""
        return self.digraph.count_edges()

    def vertices(self):
        "Named vertices"
        return self.names

    def links(self, key):
        "Links from node"
        names = []
        for linkid in self.digraph.links(self.index(key)):
            names.append(self.name(linkid))
        return names

    def name(self, index):
        """Symbol by index"""
        return self.names[index]

