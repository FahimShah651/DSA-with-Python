import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices[name] = vertex
        return vertex

    def add_edge(self, start_vertex, weight, end_vertex):
        self.vertices[start_vertex.name].add_neighbor(end_vertex, weight)

    def get_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        else:
            return None

    def get_shortest_path(self, start_vertex, end_vertex):
        start = self.get_vertex(start_vertex)
        end = self.get_vertex(end_vertex)

        start.distance = 0
        queue = [start]

        while len(queue) > 0:
            current_vertex = queue[0]
            queue = queue[1:]
            current_vertex.visited = True

            for neighbor, weight in current_vertex.adjacent.items():
                if not neighbor.visited:
                    new_distance = current_vertex.distance + weight
                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.previous = current_vertex
                        queue.append(neighbor)

        path = []
        current_vertex = end

        while current_vertex is not None:
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
e1 = graph.add_edge(vertex_a, 2, vertex_b)
e2 = graph.add_edge(vertex_a, 3, vertex_d)
e3 = graph.add_edge(vertex_a, 3, vertex_c)
e4 = graph.add_edge(vertex_b, 4, vertex_c)
e5 = graph.add_edge(vertex_b, 3, vertex_e)
e6 = graph.add_edge(vertex_d, 7, vertex_f)
e7 = graph.add_edge(vertex_d, 5, vertex_c)
e8 = graph.add_edge(vertex_c, 6, vertex_f)
e9 = graph.add_edge(vertex_c, 1, vertex_e)
e10 = graph.add_edge(vertex_f, 8, vertex_e)
e11 = graph.add_edge(vertex_f, 9, vertex_g)

# Find the shortest path from vertex A to vertex G
shortest_path = graph.get_shortest_path("A", "G")
print("Shortest path:", shortest_path)
