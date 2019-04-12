import unittest
import time

#A unit testing example with directed graphs

class Node(object):

    def __init__(self):
	#Creating a node
        self.connections = set()

    def connect_to(self, node):
	#Adding a connection
        self.connections.add(node)
    
    def is_connected_to(self, node):
	#Testing if there is a connection between two nodes
        connects = self.connections
        visited = set() #A set of visited nodes, efficient approaches need only visit each node once
        while  len(connects)>0:
            if node in connects:
                return True
            else:
                visited.update(connects)
                for n in connects:
                    connects = connects.union(n.connections)
                connects = connects - visited
                

        return False



class NodeTest(unittest.TestCase):

    def test_is_connected_to_self(self):
	#Testing self connections
        foo = Node()
        foo.connect_to(foo)
        self.assertTrue(foo.is_connected_to(foo))

    def test_is_not_connected_to_self(self):
	#Testing lack of self connection
        foo = Node()
        self.assertFalse(foo.is_connected_to(foo))

    def test_unidirectional_connection_to_neighbour(self):
		#Testing unidirectional connections to neighbours
        foo = Node()
        bar = Node()
        bar.connect_to(foo)
        self.assertTrue(bar.is_connected_to(foo))
        self.assertFalse(foo.is_connected_to(bar))

    def test_nodes_with_connection_to_themselves(self):
        foo = Node()
        bar = Node()
        baz = Node()

        # Connect the nodes to themselves.
        foo.connect_to(foo)
        bar.connect_to(bar)
        baz.connect_to(baz)

        # Connect baz => bar => foo.
        baz.connect_to(bar)
        bar.connect_to(foo)

        self.assertTrue(baz.is_connected_to(foo))
        self.assertTrue(baz.is_connected_to(bar))
        self.assertTrue(bar.is_connected_to(foo))

    def test_cyclic_graph(self):
	#Testing cyclic graphs
        foo = Node()
        bar = Node()
        baz = Node()

        # Connect the nodes baz => bar => foo => baz.
        baz.connect_to(bar)
        bar.connect_to(foo)
        foo.connect_to(baz)

        self.assertTrue(baz.is_connected_to(foo))
        self.assertTrue(baz.is_connected_to(bar))
        self.assertTrue(baz.is_connected_to(baz))

    def test_cyclic_neighbours(self):
	#Testing cyclic neighbours graphs
        foo = Node()
        bar = Node()
        baz = Node()

        # Connect the nodes baz => bar <=> foo.
        baz.connect_to(bar)
        bar.connect_to(foo)
        foo.connect_to(bar)

        self.assertTrue(baz.is_connected_to(foo))
        self.assertTrue(baz.is_connected_to(bar))
        self.assertFalse(baz.is_connected_to(baz))
    
    def test_orphaned_node(self):
	#Testing graphs with orphaned nodes
        foo = Node()
        bar = Node()
        baz = Node()
        foo.connect_to(bar)
        bar.connect_to(foo)

        self.assertTrue(bar.is_connected_to(bar))
        self.assertTrue(foo.is_connected_to(foo))
        self.assertFalse(foo.is_connected_to(baz))
        self.assertFalse(bar.is_connected_to(baz))

    def test_multiple_connections(self):
	#Testing a complex graph with multiple connections per node
        foo = Node()
        bar = Node()
        baz = Node()
        kar = Node()
        tar = Node()
        raz = Node()

        foo.connect_to(baz)
        baz.connect_to(tar)
        baz.connect_to(kar)
        kar.connect_to(tar)
        tar.connect_to(bar)
        bar.connect_to(baz)
        bar.connect_to(raz)

        self.assertTrue(foo.is_connected_to(raz))
        self.assertTrue(kar.is_connected_to(baz))
        self.assertTrue(baz.is_connected_to(bar))
        self.assertTrue(baz.is_connected_to(bar))
        self.assertTrue(baz.is_connected_to(raz))
        self.assertFalse(raz.is_connected_to(foo))


if __name__ == '__main__':
    unittest.main()