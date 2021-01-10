from unittest import TestCase
from GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from src.Node import Node


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        graph = DiGraph()
        self.graphTest = GraphAlgo(graph)
        for n in range(6):
            self.graphTest.graphAlgo.add_node(n)
        self.graphTest.graphAlgo.add_edge(0, 1, 1)
        self.graphTest.graphAlgo.add_edge(1, 0, 1.1)
        self.graphTest.graphAlgo.add_edge(1, 2, 1.3)
        self.graphTest.graphAlgo.add_edge(2, 3, 1.1)
        self.graphTest.graphAlgo.add_edge(1, 3, 1.9)
        self.graphTest.graphAlgo.add_edge(3, 4, 8)
        self.graphTest.graphAlgo.add_edge(4, 5, 1.9)
        self.graphTest.graphAlgo.add_edge(5, 2, 1.9)

    def test_connected_components(self):
        testComps = self.graphTest.connected_components()
        answerComps = [[0, 1], [2, 3, 4, 5]]
        self.assertTrue(answerComps == testComps)

    def test_connected_component(self):
        list1 = [2, 3, 4, 5]
        list2 = self.graphTest.connected_component(3)
        self.assertEqual(list1, list2)

    def test_dfs(self):
        dfsTest = self.graphTest.DFS(3)
        x = [self.graphTest.graphAlgo.get_vertex(3), self.graphTest.graphAlgo.get_vertex(4), self.graphTest.graphAlgo.get_vertex(5), self.graphTest.graphAlgo.get_vertex(2)]
        self.assertEqual(x, dfsTest)

    def test_shortest_path_dist(self):
        x = self.graphTest.shortestPath_Dist(1, 5)
        self.assertEqual(x, 11.8)

    def test_shortest_path(self):
        val, path = 2.9, [0, 1, 3]
        valtest, pathtes = self.graphTest.shortest_path(0, 3)
        self.assertEqual(val, valtest)
        self.assertEqual(path, pathtes)
