import unittest
from GraphAlgo import *
import time
import unittest

import networkx as nx
import random
import threading


class MyTestCase(unittest.TestCase):

    def init(self, Json_Dfile: str):

        self.graphAlgo = GraphAlgo()
        self.graphAlgo.load_from_json(Json_Dfile)
        self.load_nx_json(Json_Dfile)
        print('File of Graph:', Json_Dfile)

    def testSave_graph_Creator(self):
        myGraph_creator = self.graph_creator(1000, 1500, 2)
        kobi = GraphAlgo(myGraph_creator)
        start_time = time.time()
        kobi.save_to_json("../data/g_saveTestTime_1000N.json")
        end_time = time.time()
        print('MyGraph->' + "save_test_time:", 'Time:' + str(end_time - start_time))

    def test_save(self):
        self.init("../data/T0.json")
        start_time = time.time()
        dict_jx = nx.node_link_data(self.graph_x, dict(source='src', target='dest', name='id', key='key', link='links'))
        with open('../data/gX_save.json', 'w') as f:
            json.dump(dict_jx, f)
        end_time = time.time()
        print('NX:', "save_test_2time", ':', end_time - start_time)
        myGraph_creator = self.graph_creator(1000, 1500, 2)
        kobi = GraphAlgo(myGraph_creator)

        start_time = time.time()
        kobi.save_to_json("../data/g_saveTestTimekobi.json")

        self.graphAlgo.save_to_json("../data/g_saveTestTime.json")
        end_time = time.time()
        print('Our:', "save_test_time", ':', end_time - start_time)

    def time_net_x(self, NxVsMy, name_func=()):
        start_time = time.time()
        network_x_res = NxVsMy(self.graph_x, *name_func)
        end_time = time.time()
        Time_Nx = end_time - start_time
        print('NetworkX:', NxVsMy.__name__ + ' ' + 'arg:' + str(name_func), ':', 'Time:' + str(Time_Nx))

        return network_x_res, Time_Nx

    def time_Our_Graph(self, MyGraphF, iterArgu=()):
        start_time = time.time()
        My_graph_res = MyGraphF(*iterArgu)
        end_time = time.time()
        Time_OurG = end_time - start_time
        print('MyGraph:', MyGraphF.__name__ + ' ' + 'arg' + str(iterArgu), ':', 'Time:' + str(Time_OurG))

        return My_graph_res, Time_OurG

    def compare_times(self, NX, MYgraph):

        NxG1 = self.time_net_x(nx.dijkstra_path, (2, 5))

        if NX[1] <= MYgraph[1]:
            print('NetworkX Win in This Test Time')
            return 'The Path With the min dist is : ' + str(NX[0]) + ', ' + str(NxG1[0]) + ' ' + ' Time:' + str(NX[1])
        else:
            print('OurGraph Win  in This Test Time')
            return 'The Path With the min dist :' + str(MYgraph) + ' ' + ' Time:' + str(MYgraph[1])
            return

    def test_Compare_shortest_path(self):

        self.init('../data/G_10_80_0.json')
        MyGG = self.time_Our_Graph(self.graphAlgo.shortest_path, (2, 5))
        NxGX = self.time_net_x(nx.dijkstra_path_length, (2, 5))
        NxGx = self.time_net_x(nx.dijkstra_path, (2, 5))
        ko = NxGX[0], NxGx[0]
        self.assertEqual(MyGG[0], ko)  # Checking the correctness of the algorithm
        print(self.compare_times(NxGX, MyGG))

        self.init('../data/G_100_800_0.json')
        MyG = self.time_Our_Graph(self.graphAlgo.shortest_path, (2, 5))
        NxG = self.time_net_x(nx.dijkstra_path_length, (2, 5))
        NxG1 = self.time_net_x(nx.dijkstra_path, (2, 5))
        k = NxG[0], NxG1[0]
        self.assertEqual(MyG[0], k)
        print(self.compare_times(NxG, MyG))

        self.init('../data/G_1000_8000_0.json')
        MyG1 = self.time_Our_Graph(self.graphAlgo.shortest_path, (2, 5))
        NxG2 = self.time_net_x(nx.dijkstra_path_length, (2, 5))
        NxG3 = self.time_net_x(nx.dijkstra_path, (2, 5))
        k1 = NxG2[0], NxG3[0]
        self.assertEqual(MyG1[0], k1)  # Checking the correctness of the algorithm
        print(self.compare_times(NxG2, MyG1))

        self.init('../data/G_10000_80000_0.json')
        MyG2 = self.time_Our_Graph(self.graphAlgo.shortest_path, (2, 5))
        NxG3 = self.time_net_x(nx.dijkstra_path_length, (2, 5))
        NxG4 = self.time_net_x(nx.dijkstra_path, (2, 5))
        k2 = NxG3[0], NxG4[0]
        self.assertEqual(MyG2[0], k2)  # Checking the correctness of the algorithm
        print(self.compare_times(NxG3, MyG2))

        self.init('../data/G_20000_160000_0.json')
        MyG3 = self.time_Our_Graph(self.graphAlgo.shortest_path, (2, 5))
        NxG4 = self.time_net_x(nx.dijkstra_path_length, (2, 5))
        NxG5 = self.time_net_x(nx.dijkstra_path, (2, 5))
        k3 = NxG4[0], NxG5[0]
        self.assertEqual(MyG3[0], k3)  # Checking the correctness of the algorithm
        print(self.compare_times(NxG4, MyG3))

        self.init('../data/G_30000_240000_0.json')
        MyG4 = self.time_Our_Graph(self.graphAlgo.shortest_path, (2, 5))
        NxG5 = self.time_net_x(nx.dijkstra_path_length, (2, 5))
        NxG6 = self.time_net_x(nx.dijkstra_path, (2, 5))

        k4 = NxG5[0], NxG6[0]
        self.assertEqual(MyG4[0], k4)  # Checking the correctness of the algorithm
        print(self.compare_times(NxG5, MyG4))

        return

    def test_load(self):
        start_time = time.time()
        graph = GraphAlgo()
        graph.load_from_json("../data/T0.json")
        end_time = time.time()
        print('MyLoad:', "test_load", ':', end_time - start_time)

        start_time = time.time()
        self.load_nx_json("../data/T0.json")
        end_time = time.time()
        print('NXload:', "test_load", ':', end_time - start_time)

    def load_nx_json(self, data_file_js):
        dictG = {}

        with open(data_file_js, 'r') as file:
            data = json.load(file)
            self.graph_x = nx.DiGraph()

            for i in data['Nodes']:
                if 'pos' in i.keys():
                    listS = i['pos'].split(',')
                    pos = (float(listS[0]), float(listS[1]))
                    dictG[i['id']] = pos
                self.graph_x.add_node(i['id'])
            for i in data['Edges']:
                self.graph_x.add_edge(i['src'], i['dest'], weight=i['w'])
        return dictG

    def test_Compare_connected_component(self):
        self.init('../data/G_10_80_0.json')
        networkX_res = self.time_net_x(self.get_strongly_scc, (1,))
        myGraph_res = self.time_Our_Graph(self.graphAlgo.connected_component, (1,))
        print(self.compare_times(networkX_res, myGraph_res))
        return

    def test_Compare_connected_components(self):
        self.init('../data/G_10_80_0.json')
        networkX_res = self.time_net_x(nx.strongly_connected_components, ())
        myGraph_res = self.time_Our_Graph(self.graphAlgo.connected_components, ())
        print(self.compare_times(networkX_res, myGraph_res))

        self.init('../data/G_100_800_0.json')
        networkX_res = self.time_net_x(nx.strongly_connected_components, ())
        myGraph_res = self.time_Our_Graph(self.graphAlgo.connected_components, ())
        print(self.compare_times(networkX_res, myGraph_res))

    @staticmethod
    def get_strongly_scc(graphx, node):

        for scc in nx.strongly_connected_components(graphx):
            if node in scc:
                return scc
        else:
            return []

    def open_graph(self, file_name):
        graph_json = DiGraph()
        with open(file_name, 'r') as json_file:
            json_data = json.load(json_file)
            for i in json_data['Nodes']:
                if 'pos' in i.keys():
                    s = i['pos'].split(',')
                    position = (s[0], s[1])
                    graph_json.add_node(i['id'], position)
                    for j in json_data['Edges']:
                        graph_json.add_edge(j['src'], j['dest'], j['w'])
                        self.graphAlgo = graph_json
                else:
                    graph_json.add_node(i['id'])
                    for j in json_data['Edges']:
                        graph_json.add_edge(j['src'], j['dest'], j['w'])
                        self.graphAlgo = graph_json

    """
   create a graph with v_size and e_size 
    """

    def graph_creator(self, v_size, e_size, seed):
        g = DiGraph()
        k = v_size

        while k != 0:
            g.add_node(k)
            k = k - 1

        while g.e_size() < e_size:
            a = self.nextRnd(0, v_size)
            b = self.nextRnd(0, v_size)

            g.add_edge(a, b, random.random() * seed)

        return g

    def nextRnd1(self, min1, max1):
        d = random.random()
        dx = max1 - min1
        ans = d * dx + min1

        return ans

    def nextRnd(self, min2, max1):
        v = self.nextRnd1(0.0 + min2, max1)
        ans = int(v)

        return ans

    def test_graph_creator(self):
        s = self.graph_creator(1000000, 20000, 2)
        g = self.time_Our_Graph(self.graph_creator, (100000, 200000, 2))
        print(g)


if __name__ == '__main__':
    unittest.main()
