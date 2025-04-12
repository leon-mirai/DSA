TOL = 1.5 # tolerance multiplier

class NavGraph:
    
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, toll=0):
        self.nodes.setdefault(node, {"toll": toll, "roads": {}})

    def add_road(self, node1, node2, distance):
        self.nodes[node1]["roads"][node2] = distance
        
    def find_path(self, start, target, metric="distance", alpha=0.5) -> tuple:
        """Finds optimal path based on specified metric.
        
        Args:
            start: Starting node
            target: Target node
            metric: Optimization criteria ("distance", "toll", or "balanced")
            alpha: Weight for distance in balanced metric (0-1)
                   x -> 1 (distance), x -> 0 (toll)
        
        Returns:
            tuple: (path, total_cost)
        """
        # Cache max values for normalization
        max_dist = max((d for node in self.nodes.values() 
                    for d in node["roads"].values()), default=1)
        max_toll = max((node["toll"] for node in self.nodes.values()), default=1)
        
        # Initialize data structures
        costs = {node: float('inf') for node in self.nodes}
        previous = {node: None for node in self.nodes}
        unvisited = set(self.nodes.keys())
        
        # Set initial cost based on metric
        if metric == "distance":
            costs[start] = 0
        elif metric == "toll":
            costs[start] = self.nodes[start]["toll"] / max_toll
        else:  # balanced
            initial_toll = self.nodes[start]["toll"] / max_toll
            costs[start] = (1 - alpha) * initial_toll
        
        # Main Dijkstra's algorithm loop
        while unvisited:
            current = min(unvisited, key=lambda node: costs[node])
            unvisited.remove(current)
            
            if current == target:
                break
                
            for neighbor, distance in self.nodes[current]["roads"].items():
                if metric == "distance":
                    new_cost = costs[current] + distance
                elif metric == "toll":
                    new_cost = costs[current] + (self.nodes[neighbor]["toll"] / max_toll)
                else:  # balanced
                    norm_dist = distance / max_dist
                    norm_toll = self.nodes[neighbor]["toll"] / max_toll
                    # Improved balanced cost calculation
                    new_cost = costs[current] + (alpha * norm_dist) ** 2 + ((1 - alpha) * norm_toll) ** 2
                    
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    previous[neighbor] = current
        
        path = self._reconstruct_path(previous, target)
        total_cost = costs.get(target, float('inf'))
        
        # For balanced metric, return normalized cost
        if metric == "balanced" and path:
            actual_dist = sum(self.nodes[path[i]]["roads"][path[i+1]] for i in range(len(path)-1)) / max_dist
            actual_toll = sum(self.nodes[node]["toll"] for node in path) / max_toll
            total_cost = (alpha * actual_dist) + ((1 - alpha) * actual_toll)
        
        return path, total_cost 

    def _reconstruct_path(self, previous, target) -> list:
        path = []
        current = target
        while current is not None:
            path.insert(0, current)
            current = previous.get(current)
        return path if path and path[0] in previous else []

    def compare_routes(self, start, target, alpha=0.5) -> tuple[list, list]:
        """Returns tuple of (kept_routes, discarded_routes) with full metrics"""
        metrics = [
            ("shortest", "distance"),
            ("cheapest", "toll"),
            ("balanced", "balanced")
        ]
        
        results = {}
        for name, metric in metrics:
            path, cost = self.find_path(start, target, metric, alpha)
            if path:
                total_distance = sum(self.nodes[path[i]]["roads"][path[i+1]] 
                                 for i in range(len(path)-1))
                total_toll = sum(self.nodes[node]["toll"] for node in path)
                results[name] = {
                    "path": path,
                    "distance": total_distance,
                    "toll": total_toll,
                    "cost": cost if name == "balanced" else None
                }
        
        if not results:
            return [], []
            
        min_dist = min(route["distance"] for route in results.values())
        min_toll = min(route["toll"] for route in results.values())
        
        kept = []
        discarded = []
        
        for name, data in results.items():
            route_data = {"type": name, **data}
            if (data["distance"] <= TOL * min_dist or 
                data["toll"] <= TOL * min_toll):
                kept.append(route_data)
            else:
                discarded.append(route_data)
        
        return kept, discarded

def test_alphas(graph, start, target, alphas=[0.1, 0.5, 0.9]):
    """Simplified route tester showing toll and distance separately"""
    for alpha in alphas:
        print(f"\nTesting alpha={alpha:.1f}")
        kept, discarded = graph.compare_routes(start, target, alpha)
        
        # Accepted routes
        if kept:
            print("\n[Accepted Routes]")
            for route in kept:
                print(f"\n{route['type'].upper()}: {' → '.join(route['path'])}")
                print(f"  Distance: {route['distance']:.1f} km")
                print(f"  Toll: ${route['toll']:.2f}")
                if route['cost'] is not None:
                    print(f"  Balanced score: {route['cost']:.2f}")
        else:
            print("\nNo valid routes found")
        
        # Discarded routes
        if discarded:
            print("\n[Discarded Routes]")
            min_dist = min(r["distance"] for r in kept) if kept else float('inf')
            min_toll = min(r["toll"] for r in kept) if kept else float('inf')
            
            for route in discarded:
                print(f"\n{route['type'].upper()}: {' → '.join(route['path'])}")
                print(f"  Distance: {route['distance']:.1f} km ({route['distance']/min_dist:.1f}x min)")
                print(f"  Toll: ${route['toll']:.2f} ({route['toll']/min_toll:.1f}x min)")
                
                reasons = []
                if route['distance'] > TOL * min_dist:
                    reasons.append(f"Distance > {TOL}x min")
                if route['toll'] > TOL * min_toll:
                    reasons.append(f"Toll > {TOL}x min")
                
                print(f"  Reason: {' & '.join(reasons)}")

def create_graph():
    """Graph with three clear options"""
    g = NavGraph()
    g.add_node("Start", toll=0)
    g.add_node("Fast", toll=6)   # Shortest
    g.add_node("Cheap", toll=1)  # Cheapest
    g.add_node("Mid", toll=3)    # Balanced
    g.add_node("End", toll=0)
    
    g.add_road("Start", "Fast", 2)
    g.add_road("Fast", "End", 2)   # 4km, $6
    g.add_road("Start", "Cheap", 6)
    g.add_road("Cheap", "End", 6)  # 12km, $1
    g.add_road("Start", "Mid", 4)
    g.add_road("Mid", "End", 4)    # 8km, $3
    return g

g = create_graph()
test_alphas(g, "Start", "End", alphas=[0.5])