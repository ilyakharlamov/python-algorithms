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
        self.assertEquals("FU", sd.name(sd.index("FU")))
        sd.add_vertice("CK")
        self.assertEquals(2, sd.count_vertices())
        self.assertEquals(0, sd.index("FU"))
        self.assertEquals("FU", sd.name(sd.index("FU")))
        self.assertEquals(1, sd.index("CK"))
        self.assertEquals(-1, sd.index("YO"))

    def testAddEdge(self):
        sd = SymbolDigraph()
        sd.add_edge("FU", "CK")
        sd.add_edge("FU", "RY")
        self.assertEquals(3, sd.count_vertices())
        self.assertEquals(2, sd.count_edges())


    def testRoutes(self):
        sd = SymbolDigraph()
        sd.add_edge("JFK","MCO")
        sd.add_edge("ORD","DEN")
        sd.add_edge("ORD","HOU")
        sd.add_edge("DFW","PHX")
        sd.add_edge("JFK","ATL")
        sd.add_edge("ORD","DFW")
        sd.add_edge("ORD","PHX")
        sd.add_edge("ATL","HOU")
        sd.add_edge("DEN","PHX")
        sd.add_edge("PHX","LAX")
        sd.add_edge("JFK","ORD")
        sd.add_edge("DEN","LAS")
        sd.add_edge("DFW","HOU")
        sd.add_edge("ORD","ATL")
        sd.add_edge("LAS","LAX")
        sd.add_edge("ATL","MCO")
        sd.add_edge("HOU","MCO")
        sd.add_edge("LAS","PHX")
        self.assertEquals(10, len(sd.vertices()))
        self.assertEquals(2, len(sd.links("ATL")))
        self.assertEquals(3, len(sd.links("JFK")))


if __name__=="__main__":
    unittest.main()
