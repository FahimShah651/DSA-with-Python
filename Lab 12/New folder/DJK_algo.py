import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))

    def __lt__(self, other):
        return self.distance < other.distance

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices[name] = vertex
        return vertex

    def get_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        else:
            return None

    def add_edge(self, start, weight, end):
        self.vertices[start.name].add_neighbor(end.name, weight)

    def print_graph(self):
        for vertex_name, vertex in self.vertices.items():
            neighbors = ", ".join([f"{neighbor} ({weight})" for neighbor, weight in vertex.neighbors])
            print(f"{vertex_name}: {neighbors}")

    def dijkstra(self, start):
        start.distance = 0
        unvisited_vertices = list(self.vertices.values())

        while unvisited_vertices:
            current_vertex = min(unvisited_vertices)
            unvisited_vertices.remove(current_vertex)

            for neighbor_name, weight in current_vertex.neighbors:
                neighbor = self.get_vertex(neighbor_name)
                if neighbor.visited:
                    continue

                new_distance = current_vertex.distance + weight
                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.previous = current_vertex

            current_vertex.visited = True

    def get_shortest_path(self, end):
        path = []
        current_vertex = self.get_vertex(end)
        while current_vertex:
            path.insert(0, current_vertex.name)
            current_vertex = current_vertex.previous
        return path


# Create a graph
graph = Graph()

# Add vertices
vertex_a = graph.add_vertex("A")
vertex_b = graph.add_vertex("B")
vertex_c = graph.add_vertex("C")
vertex_d = graph.add_vertex("D")
vertex_e = graph.add_vertex("E")
vertex_f = graph.add_vertex("F")
vertex_g = graph.add_vertex("G")

# Add edges with weights
graph.add_edge(vertex_a, 2, vertex_b)
graph.add_edge(vertex_a, 3, vertex_d)
graph.add_edge(vertex_a, 3, vertex_c)
graph.add_edge(vertex_b, 4, vertex_c)
graph.add_edge(vertex_b, 3, vertex_e)
graph.add_edge(vertex_d, 7, vertex_f)
graph.add_edge(vertex_d, 5, vertex_c)
graph.add_edge(vertex_c, 6, vertex_f)
graph.add_edge(vertex_c, 1, vertex_e)
graph.add_edge(vertex_f, 8, vertex_e)
graph.add_edge(vertex_f, 9, vertex_g)

# Run Dijkstra's algorithm
graph.dijkstra(vertex_a)

# Get the shortest path to vertex G
shortest_path = graph.get_shortest_path(vertex_g.name)
print("Shortest Path: A to G :: ", shortest_path)
print()
shortest_path = graph.get_shortest_path(vertex_e.name)
print("Shortest Path: A to E :: ", shortest_path)

