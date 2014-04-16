import random
import unittest
import sys
sys.path.append("../src")
from depthfirstorder import DepthFirstOrder
from digraph import Digraph

class TestDepthFirstOrder(unittest.TestCase):
    def test_init(self):
        d = Digraph(13)
        d.add_edge(2,3)
        d.add_edge(0,6)
        d.add_edge(0,1)
        d.add_edge(2,0)
        d.add_edge(11,12)
        d.add_edge(9,12)
        d.add_edge(9,10)
        d.add_edge(9,11)
        d.add_edge(3,5)
        d.add_edge(8,7)
        d.add_edge(5,4)
        d.add_edge(0,5)
        d.add_edge(6,4)
        d.add_edge(6,9)
        d.add_edge(7,6)
        order = DepthFirstOrder(d)
        self.assertEquals([0,3,9,10,2,1,4,11,12,5,8,6,7], order.pre)
        self.assertEquals([0,5,4,1,6,9,11,12,10,2,3,7,8], order.preorder)
        self.assertEquals([8,2,10,9,0,1,7,11,12,6,5,4,3], order.post)
        self.assertEquals([4,5,1,12,11,10,9,6,0,3,2,7,8], order.postorder)


if __name__ == '__main__':
    unittest.main()