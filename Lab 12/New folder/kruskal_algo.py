class Vertex:
    def __init__(self, name):
        self.name = name
        self.parent = None

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, start_vertex, weight, end_vertex):
        self.edges.append((start_vertex, weight, end_vertex))

    def find(self, vertex):
        if vertex.parent is None:
            return vertex
        return self.find(vertex.parent)

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        root2.parent = root1

    def kruskal(self):
        minimum_spanning_tree = []
        sorted_edges = sorted(self.edges, key=lambda x: x[1])  
        for edge in sorted_edges:
            start_vertex, weight, end_vertex = edge
            if self.find(start_vertex) != self.find(end_vertex):
                minimum_spanning_tree.append(edge)
                self.union(start_vertex, end_vertex)

        return minimum_spanning_tree

    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex:", vertex.name)
        for edge in self.edges:
            start_vertex, weight, end_vertex = edge
            print("Edge:", start_vertex.name, "--", weight, "--", end_vertex.name)

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

# Print the graph
graph.print_graph()

# Find the minimum spanning tree
minimum_spanning_tree = graph.kruskal()

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    start_vertex, weight, end_vertex = edge
    print(start_vertex.name, "--", weight, "--", end_vertex.name)
