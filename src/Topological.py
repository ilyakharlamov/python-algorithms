"Topological sort"
from directedcycle import DirectedCycle
from depthfirstorder import DepthFirstOrder

class Topological(object):
    """Does topological sort"""
    def __init__(self, digraph):
        self.finder = DirectedCycle(digraph)
        self.dfs = DepthFirstOrder(digraph)

    def independent_last(self):
        "Sort independent last"
        if not self.finder.has_cycle():
            return self.dfs.reverse_postorder()
        return None

    def independent_first(self):
        "Sort independent first"
        if not self.finder.has_cycle():
            return self.dfs.postorder
        return None
