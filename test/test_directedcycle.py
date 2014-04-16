#!/bin/env python
#test_digraph.py
import sys, unittest
sys.path.append("../src")
from digraph import Digraph
from directedcycle import DirectedCycle

class TestDirectedCycle(unittest.TestCase):
    def testInitial(self):
        pass
    def testCycle(self):
        d = Digraph(13)
        d.add_edge(4,2)
        d.add_edge(2,3)
        d.add_edge(3,2)
        d.add_edge(6,0)
        d.add_edge(0,1)
        d.add_edge(2,0)
        d.add_edge(11,12)
        d.add_edge(12,9)
        d.add_edge(9,10)
        d.add_edge(9,11)
        d.add_edge(7,9)
        d.add_edge(10,12)
        d.add_edge(11,4)
        d.add_edge(4,3)
        d.add_edge(3,5)
        d.add_edge(6,8)
        d.add_edge(8,6)
        d.add_edge(5,4)
        d.add_edge(0,5)
        d.add_edge(6,4)
        d.add_edge(6,9)
        d.add_edge(7,6)
        self.assertEquals(13, d.count_vertices())
        finder = DirectedCycle(d)
        self.assertEquals([3,4,5,3], finder.cycle)

    def has_no_cycle(self):
        d = Digraph()
        d.add_edge(2, 3)
        dc = DirectedCycle(d)
        self.assertEquals(False, dc.has_cycle())

    def has_cycle_b(self):
        d = Digraph()
        d.add_edge(1, 2)
        d.add_edge(2, 3)
        d.add_edge(3, 1)
        dc = DirectedCycle(d)
        self.assertEquals(True, dc.has_cycle())

if __name__=="__main__":
    unittest.main()
