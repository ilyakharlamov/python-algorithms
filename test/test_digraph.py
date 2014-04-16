#!/bin/sh
#test_digraph.py
import sys, unittest
sys.path.append("../src")
from digraph import Digraph

class TestDigraph(unittest.TestCase):
    def testInitial(self):
        pass
    def testOverflow(self):
        d = Digraph(5)
        d.add_edge(0, 1)
        self.assertRaises(Exception, d.add_edge, 10, 1)

    def test_add_vertice(self):
        d = Digraph()
        self.assertEquals(0, d.count_vertices())
        d.add_vertice()
        self.assertEquals(1, d.count_vertices())
        d.add_vertice()
        d.add_vertice()
        self.assertEquals(3, d.count_vertices())
    def test_add_edge_to_empty(self):
        d = Digraph()
        self.assertEquals(0, d.count_vertices())
        d.add_vertice()
        d.add_vertice()
        d.add_vertice()
        d.add_edge(0, 1)
        d.add_edge(2, 0)
        self.assertEquals(2, d.count_edges())

    def test_add_edge_to_non_empty(self):
        d = Digraph(3)
        d.add_edge(1,2)
        self.assertEquals(1, len(d.links(1)))
        self.assertEquals(0, len(d.links(2)))


if __name__=="__main__":
    unittest.main()
