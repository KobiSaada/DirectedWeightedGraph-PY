# DirectedWeightedGraph-PY ![python (1)](https://user-images.githubusercontent.com/73976733/104119424-d19d8480-5337-11eb-8a0d-fb8e26dab285.png)


# welcome to EX3-Final Assigment in OOP in ariel university :tada::mortar_board:

![Webp net-compress-image (3)](https://user-images.githubusercontent.com/73976733/101813689-b9163080-3b25-11eb-9e93-5471b17b0e15.jpg)



# Geneal Info ::books:
In this task we were required to implement a deliberate and weighted graph with all the algorithms similar to the previous task only in the Python programming language and in addition we were required to compare execution times between our results and the network x and java library and also implemented a graphical representation of the graph using maplotlib library in Python Have fun.
<img width="639" alt="Screen Shot 2021-01-10 at 11 04 27" src="https://user-images.githubusercontent.com/73976733/104119179-7b7c1180-5336-11eb-8910-b16a2105519a.png">



# Getting Started ::zap:
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites:![images1](https://user-images.githubusercontent.com/73976733/104119486-440e6480-5338-11eb-9b19-efb559b320f3.jpeg) ![eclipse](https://user-images.githubusercontent.com/73976733/104119509-6ef8b880-5338-11eb-9f7e-ebb74c2821f3.png)


* JDK-15.0.1

* Eclipse

* IntelliJ

* or some other IDE (recommended)

# Installing ::wrench:
Clone that project to your workspace directory

        git clone https://github.com/KobiSaada/DirectedWeightedGraph-PY
        
  Open your IDE and make sure you see the project 'DirectedWeightedGraph-PY'
  
  
  # Data Stracture:
  # Node class:
  * get_id()->return the id of thr Node
  * get_weight(self, neighbor)->return the weight between this Node and this neighbor out from this node 
  * get_weightIn(self, neighbor)->return the weight between this Node and neighbor in grom this node
  * deleteNi_in(self, id1)-> by given int id1 delete him from neigbors in to this node
   * deleteNi_out(self, id1)-> by given int id1 delete him from neigbors out to this node
   * add_out_Ni(self, node_out: int, weight: float)->  by given int id1 and float weight add to neighbor out of this node a ni and weight between them
   * add_in_Ni(self, node_out: int, weight: float)->  by given int id1 and float weight add to neighbor in of this node a ni and weight between them
   * getPosition(self)->return the position of node
   # DiGraph :
   
   # GraphAlgo :
   * get_graph(self)->return this graph
   * load_from_json-> Loads a graph from a json file.
   * sava_to_json-> save a graph to a json file.
   * plot_graph(self)->  Plots the graph If the nodes have a position, the nodes will be placed there Otherwise, they will be placed in a random but elegant manner.
   * connected_components(self)->  Finds all the Strongly Connected Component(SCC) in the graph.
   # Example to connected_components:
   ![Scc](https://user-images.githubusercontent.com/73976733/104119114-27712d00-5336-11eb-90c4-a4b71b392f6d.png)

   * connected_component(self, id1: int) -> list: Finds the Strongly Connected Component(SCC) that node id1 is a part of.
   * shortest_path(self, id1: int, id2: int) -> (float, list): Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
   # Example to shortest path :
   ![multi-stage-graph](https://user-images.githubusercontent.com/73976733/102022330-c124d900-3d8e-11eb-84ae-4ad241999919.jpg)
   
   # Diagram PlTUML :
   
   <img width="684" alt="Screen Shot 2021-01-10 at 9 20 43" src="https://user-images.githubusercontent.com/73976733/104119230-b8e09f00-5336-11eb-880d-bed1c8eb1f2f.png">
<img width="643" alt="Screen Shot 2021-01-10 at 9 21 32" src="https://user-images.githubusercontent.com/73976733/104119233-bd0cbc80-5336-11eb-9342-df865528d261.png">
<img width="212" alt="Screen Shot 2021-01-10 at 9 21 59" src="https://user-images.githubusercontent.com/73976733/104119236-be3de980-5336-11eb-9044-5b745a197dcb.png">

# Results Compare Times ::bar_chart::alarm_clock:
<img width="1127" alt="Screen Shot 2021-01-10 at 9 13 43" src="https://user-images.githubusercontent.com/73976733/104119269-efb6b500-5336-11eb-8cfb-2ed1c49a4deb.png">





   
  






