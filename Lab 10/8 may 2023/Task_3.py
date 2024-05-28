class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, data):
        vertex = {"data": data, "edges": []}
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, start, end):
        edge = {"start": start, "end": end}
        start["edges"].append(edge)
        end["edges"].append(edge)

    def print_graph(self):
        num_vertices = len(self.vertices)
        adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

        # Create a mapping from vertex to its index in the adjacency matrix
        vertex_to_index = {vertex["data"]: index for index, vertex in enumerate(self.vertices)}

        for vertex in self.vertices:
            for edge in vertex["edges"]:
                start_index = vertex_to_index[edge['start']['data']]
                end_index = vertex_to_index[edge['end']['data']]
                adjacency_matrix[start_index][end_index] = 1
                adjacency_matrix[end_index][start_index] = 1

        # Print the adjacency matrix
        print("Adjacency Matrix:")
        for row in adjacency_matrix:
            print(row)

        print()



graph = Graph()

vertex_a = graph.add_vertex("A")
vertex_b = graph.add_vertex("B")
vertex_c = graph.add_vertex("C")
vertex_d = graph.add_vertex("D")
vertex_e = graph.add_vertex("E")
vertex_f = graph.add_vertex("F")
vertex_g = graph.add_vertex("G")
vertex_h = graph.add_vertex("H")
vertex_i = graph.add_vertex("I")
vertex_j = graph.add_vertex("J")
vertex_k = graph.add_vertex("K")
vertex_l = graph.add_vertex("L")
vertex_m = graph.add_vertex("M")
vertex_n = graph.add_vertex("N")
vertex_o = graph.add_vertex("O")
vertex_p = graph.add_vertex("P")

graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_a, vertex_e)
graph.add_edge(vertex_a, vertex_f)
graph.add_edge(vertex_b, vertex_c)
graph.add_edge(vertex_b, vertex_f)
graph.add_edge(vertex_c, vertex_d)
graph.add_edge(vertex_c, vertex_g)
graph.add_edge(vertex_d, vertex_g)
graph.add_edge(vertex_d, vertex_h)
graph.add_edge(vertex_e, vertex_f)
graph.add_edge(vertex_e, vertex_i)
graph.add_edge(vertex_f, vertex_i)
graph.add_edge(vertex_g, vertex_j)
graph.add_edge(vertex_g, vertex_k)
graph.add_edge(vertex_g, vertex_l)
graph.add_edge(vertex_h, vertex_l)
graph.add_edge(vertex_i, vertex_m)
graph.add_edge(vertex_i, vertex_n)
graph.add_edge(vertex_i, vertex_j)
graph.add_edge(vertex_j, vertex_k)
graph.add_edge(vertex_l, vertex_p)
graph.add_edge(vertex_k, vertex_n)
graph.add_edge(vertex_k, vertex_o)
graph.add_edge(vertex_m, vertex_n)

graph.print_graph()
