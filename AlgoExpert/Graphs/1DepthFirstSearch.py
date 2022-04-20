import unittest 

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# Visualize this graph in paper to understanding this .. 
class SimpleTest(unittest.TestCase):
    # Return True or False:
    def test(self,):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")

        output = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
        self.assertEqual(graph.depthFirstSearch([]), output)

if __name__ == '__main__':
    unittest.main()