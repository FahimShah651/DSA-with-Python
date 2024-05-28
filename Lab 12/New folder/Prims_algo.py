import heapq

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = []

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((weight, neighbor))

    def get_neighbors(self):
        return self.neighbors

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return False

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex1, weight, vertex2):
        vertex1.add_neighbor(vertex2, weight)
        vertex2.add_neighbor(vertex1, weight)

    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex", vertex.key)
            for weight, neighbor in vertex.get_neighbors():
                print(" -> Neighbor:", neighbor.key, "Weight:", weight)

    def minimum_spanning_tree(self, start_vertex):
        mst = []
        heap = []
        visited = set()

      
        visited.add(start_vertex)

        for weight, neighbor in start_vertex.get_neighbors():
            heapq.heappush(heap, (weight, start_vertex, neighbor))

        while heap:
    
            weight, source, destination = heapq.heappop(heap)

            if destination not in visited:

                mst.append((source.key, destination.key, weight))

   
                visited.add(destination)

                for weight, neighbor in destination.get_neighbors():
                    heapq.heappush(heap, (weight, destination, neighbor))

        return mst

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

# Print the graph
graph.print_graph()


# Find the minimum spanning tree starting from vertex A
minimum_spanning_tree = graph.minimum_spanning_tree(vertex_a)
print("\nMinimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
