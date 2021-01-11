# DirectedWeightedGraph-PY ![python (1)](https://user-images.githubusercontent.com/73976733/104119424-d19d8480-5337-11eb-8a0d-fb8e26dab285.png)

![Webp net-compress-image (3)](https://user-images.githubusercontent.com/73976733/101813689-b9163080-3b25-11eb-9e93-5471b17b0e15.jpg)


# Welcome to EX3-Final Assigment in OOP in ariel university :tada::mortar_board:



# General Info ::books:

**In this task we were required to implement a deliberate and weighted graph with all the algorithms similar to the previous task only in the Python programming language and in addition we were required to compare execution times between our results and the network x and java library and also implemented a graphical representation of the graph using maplotlib library in Python Have fun!**.

<img width="450" alt="Screen Shot 2021-01-10 at 22 26 44 (1)" src="https://user-images.githubusercontent.com/73976733/104136369-4905ff00-539e-11eb-87bf-a4af2e0b5976.png"><img width="450" alt="Screen Shot 2021-01-10 at 23 44 45 (2) (1)" src="https://user-images.githubusercontent.com/73976733/104136411-92eee500-539e-11eb-9b7c-260ff63beb37.png">



# Getting Started ::zap:
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites: :bulb:

* PyCharm ![22](https://user-images.githubusercontent.com/73976733/104122372-55ae3700-534d-11eb-8de4-492973fca972.jpeg)

* or some other IDE 

**library:**

<img width="496" alt="Screen Shot 2021-01-12 at 1 08 27" src="https://user-images.githubusercontent.com/73976733/104248904-0e21cb00-5473-11eb-903e-0e0685c53dca.png">




# Installing ::wrench:
Clone that project to your workspace directory

        git clone https://github.com/KobiSaada/DirectedWeightedGraph-PY
        
  Open your IDE and make sure you see the project 'DirectedWeightedGraph-PY'
  
 # Example of run test in check(0) ::pencil:

 after you clone this project there is a class call Ex3 main run it in check(0):
 
        g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)

    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()
 
  
  
  # Data Stracture:
  # Node class:
 *  **get_id()**->return the id of thr Node
 *  **get_weight(self, neighbor)**->return the weight between this Node and this neighbor out from this node 
 *  **get_weightIn(self, neighbor)**->return the weight between this Node and neighbor in grom this node
 *  **deleteNi_in(self, id1)**-> by given int id1 delete him from neigbors in to this node
 *  **deleteNi_out(self, id1)**-> by given int id1 delete him from neigbors out to this node
 *  **add_out_Ni(self, node_out: int, weight: float)**->  by given int id1 and float weight add to neighbor out of this node a ni and weight between them
 *  **add_in_Ni(self, node_out: int, weight: float)**->  by given int id1 and float weight add to neighbor in of this node a ni and weight between them
 *  **getPosition(self)**->return the position of node
  
   # DiGraph Class :
   * **__init__(self)**->Init this graph.
   * **get_vertex(self,n)**->get a Node if the node exist in the graph else return NONE.
   * **add_edge(self, id1: int, id2: int, weight: float)**->Adds an edge to the graph return: True if the edge was added successfully, False o.w.
   * **get_all_v(self)**->return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data).
   * **e_size(self)**-> Returns the number of edges in this graph.
   * **add_node(self, node_id: int, pos: tuple = None)**->Adds a node to the graph return: True if the node was added successfully, False o.w.
   * **remove_edge(self, node_id1: int, node_id2: int)**->Removes an edge from the graph return: True if the edge was removed successfully, False o.w.
   * **get_mc(self)**->Returns the current version of this graph,on every change in the graph state - the MC should be increased return: The current version of this graph.
   * **all_in_edges_of_node(self, id1: int)**->return a dictionary of all the nodes connected to (into) node_id,each node is represented using a pair (key, weight)
   * **all_out_edges_of_node(self, id1: int)**->return a dictionary of all the nodes connected from node_id,each node is represented using a pair (key,
   weight).
   * **v_size(self)**->Returns the number of vertices in this graph.
   * **remove_node(self, node_id: int)**->Removes a node from the graph return: True if the node was removed successfully, False o.w.
   * **get_vertices(self)**->Returns a dict of nodes representing the vertices in the graph, in dict order.
        
          
   
   # GraphAlgo Class :
 *  **get_graph(self)**->return this graph
 *  **load_from_json(self,file:str)**-> Loads a graph from a json file.
 *  **sava_to_json**-> save a graph to a json file.
 *  **plot_graph(self)**->  Plots the graph If the nodes have a position, the nodes will be placed there Otherwise, they will be placed in a random but elegant manner using matplot lib libarary.
 * https://matplotlib.org/users/pyplot_tutorial.html
 *   **connected_components(self)**->  Finds all the Strongly Connected Component(SCC) in the graph.
   # Example for connected_components:
   ![Scc](https://user-images.githubusercontent.com/73976733/104119114-27712d00-5336-11eb-90c4-a4b71b392f6d.png)
    
      OUTPUT->THE COMPONENTS IN THIS PIQTURE IS ARE :[[a,b,e],[f,g],[c,d,h]];

 *   **connected_component(self, id1: int)** -> list: Finds the Strongly Connected Component(SCC) that node id1 is a part of.
 *   **shortest_path(self, id1: int, id2: int)** -> (float, list): Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
   # Example for shortest path ::pushpin:
   ![multi-stage-graph](https://user-images.githubusercontent.com/73976733/102022330-c124d900-3d8e-11eb-84ae-4ad241999919.jpg)
   
   # Diagram PLTUML ::chart_with_downwards_trend:
<img width="342" alt="Screen Shot 2021-01-10 at 9 20 43" src="https://user-images.githubusercontent.com/73976733/104139391-d30c9280-53b3-11eb-825f-3d7625f04daa.png">
<img width="322" alt="Screen Shot 2021-01-10 at 9 21 32" src="https://user-images.githubusercontent.com/73976733/104139394-d6078300-53b3-11eb-943f-5351da340b12.png">
<img width="106" alt="Screen Shot 2021-01-10 at 9 21 59" src="https://user-images.githubusercontent.com/73976733/104139395-d6a01980-53b3-11eb-928b-cb7e505c6784.png">



# Results Compare Times ::bar_chart::hourglass:
<img width="550" alt="Screen Shot 2021-01-11 at 0 49 08 (1)" src="https://user-images.githubusercontent.com/73976733/104139455-50d09e00-53b4-11eb-98c8-7aa7ab6e227d.png">


# External Info ::mag_right:
* https://matplotlib.org/3.1.1/gallery/style_sheets/dark_background.html
* https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
* https://en.wikipedia.org/wiki/Strongly_connected_component
* https://wiki.c2.com/?WeightedDirectedGraph


# Enjoy!:smile:
# Authors :
***KOBI SAADA & TAMIR KAlIAUH*** :v:



   
  






