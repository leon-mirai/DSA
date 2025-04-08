class Graph:
    def __init__(self):
        self.nodes = {}
        
    def add_node(self, node, toll = 0):
        if node in self.nodes:
            print(f"Node {node} already exists")
        self.nodes[node] = {
            "toll": toll,
            "roads": {}
        }
    
    def add_road(self, from_node, to_node, distance):
        if from_node not in self.nodes:
            raise ValueError(f"Node {from_node} does not exist")
        if to_node not in self.nodes:
            raise ValueError(f"Node {to_node} does not exist")
        
        self.nodes[from_node]["roads"][to_node] = distance
        
    def get_toll(self, node):
        return self.nodes[node]["toll"]
    
    def get_neighbours(self, node):
        return self.nodes[node]["roads"]
    
    def find_shortest_path(self, start, target):
        dists = {node: float("inf") for node in self.nodes}
        dists[start] = 0
        prev = {node: None for node in self.nodes}
        unvisited = set(self.nodes.keys())
        
        while unvisited:
            curr = min(unvisited, key=lambda node: dists[node])
            unvisited.remove(curr)
            
            if dists[curr] == float("inf"):
                break
            
            for n, dist in self.get_neighbours(curr).items():
                new_dist = dists[curr] + dist
                if new_dist < dists[n]:
                    dists[n] = new_dist
                    prev[n] = curr
        
        
        return self.reconstruct_path(prev, target), dists[target]
    
    def reconstruct_path(self, prev, target):
        if prev[target] is not None and target not in self.nodes:
            return None
        
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        return path[::-1]
    
    
g = Graph()
g.add_node("A", toll=0)
g.add_node("B", toll=2)
g.add_node("C", toll=3)
g.add_node("D", toll=2)

g.add_road("A", "B", 4)
g.add_road("A", "C", 8)
g.add_road("B", "C", 5)
g.add_road("B", "D", 2)

path, distance = g.find_shortest_path("A", "D")
print(f"\nShortest path from A to D: {path} (Distance: {distance})")

