import unittest
import sys
import StringIO
sys.path.append("../src")
from symboldigraph import SymbolDigraph
from topological import Topological

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_init(self):
        sd = SymbolDigraph()
        dag = StringIO.StringIO("""2/3 
        0/6 
        0/1 
        2/0 
        11/12  
        9/12  
        9/10  
        9/11 
        3/5 
        8/7 
        5/4 
        0/5 
        6/4 
        6/9 
        7/6""")
        for line in dag:
            dependencies = line.strip().split("/")
            for i in range(len(dependencies)):
                if i == 0:
                    continue
                sd.add_edge(dependencies[0], dependencies[i])
        topological = Topological(sd.digraph)
        etalon = ['8','7','2','3','0','6','9','10','11','12','1','5','4']
        self.assertEquals(etalon, map(lambda x: sd.name(x), topological.independent_last()))


if __name__ == '__main__':
    unittest.main()
