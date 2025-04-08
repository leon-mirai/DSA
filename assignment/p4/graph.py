class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = dict()
        
    def add_vertex(self, node):
        self.number_of_nodes += 1
        self.adjacent_list[node] = []
        
    
    def add_edge(self, node1, node2):
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)



    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = " ".join(node_connections)
            print(f"{node} --> {connections}")
        
myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('0', '1')
myGraph.add_edge('0', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '3')
myGraph.add_edge('2', '0')
myGraph.add_edge('2', '1')
myGraph.add_edge('2', '4')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '3')
myGraph.add_edge('4', '5')
myGraph.add_edge('5', '4')
myGraph.add_edge('5', '6')
myGraph.add_edge('6', '5')
myGraph.show_connections()
print(myGraph.adjacent_list)
