#!/bin/env python
#test_digraph.py
import sys, unittest
sys.path.append("../src")
from symboldigraph import SymbolDigraph

class TestSymbolDigraph(unittest.TestCase):
    def testInitial(self):
        sd = SymbolDigraph()
        self.assertEquals(0, sd.count_vertices())

    def testAddNone(self):
        sd = SymbolDigraph()
        self.assertRaises(Exception, sd.add_edge, None, None)

    def testAddEmpty(self):
        sd = SymbolDigraph()
        self.assertRaises(Exception, sd.add_edge, "", "")

    def testAddVertice(self):
        sd = SymbolDigraph()
        sd.add_vertice("FU")
        sd.add_vertice("CK")
        self.assertEquals(2, sd.count_vertices())
        self.assertEquals(0, sd._index("FU"))
        self.assertEquals(1, sd._index("CK"))
        self.assertEquals(-1, sd._index("YO"))

    def testAddEdge(self):
        sd = SymbolDigraph()
        sd.add_edge("FU", "CK")
        sd.add_edge("FU", "RY")
        self.assertEquals(3, sd.count_vertices())
        self.assertEquals(2, sd.count_edges())
if __name__=="__main__":
    unittest.main()
