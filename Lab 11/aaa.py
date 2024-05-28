class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, data):
        vertex = Vertex(data)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, start, end):
        edge = Edge(start, end)
        start.add_edge(edge)
        end.add_edge(edge)

    def remove_vertex(self, vertex):
        for v in self.vertices:
            if vertex == v.data:
                self.vertices.remove(v)
            for edge in v.edges:
                if edge.start.data == vertex:
                    self.remove_edge(edge.start.data, edge.end.data)
                if edge.end.data == vertex:
                    self.remove_edge(edge.start.data, edge.end.data)

    def remove_edge(self, start, end):
        for vertex in self.vertices:
            for edge in vertex.edges:
                if (edge.start.data == start) and (edge.end.data == end):
                    vertex.edges.remove(edge)

    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex:", vertex.data)
            print("Edges:")
            for edge in vertex.edges:
                print(f"{edge.start.data} --- {edge.end.data}")
            print()

    def BFS(self, data):
        queue = []
        visited = set()
        check = False
        for vertex in self.vertices:
            if vertex.data == data:
                check = True
                queue.append(vertex)
                visited.add(vertex)
                while queue:
                    current_vertex = queue.pop(0)
                    print(f"Visited vertex: {current_vertex.data}")
                    if current_vertex.data == "E":
                        break
                    for edge in current_vertex.edges:
                        if edge.end.data != "W" and edge.end not in visited:
                            visited.add(edge.end)
                            queue.append(edge.end)
                        if edge.start.data != "W" and edge.start not in visited:
                            visited.add(edge.start)
                            queue.append(edge.start)
                break
        if not check:
            print("Vertex not found in Graph")


graph = Graph()

vertex_a = graph.add_vertex("S")
vertex_b = graph.add_vertex("1")
vertex_c = graph.add_vertex("1")
vertex_d = graph.add_vertex("1")
vertex_e = graph.add_vertex("1")
vertex_f = graph.add_vertex("1")
vertex_g = graph.add_vertex("W")
vertex_h = graph.add_vertex("1")
vertex_i = graph.add_vertex("W")
vertex_j = graph.add_vertex("1")
vertex_k = graph.add_vertex("1")
vertex_l = graph.add_vertex("W")
vertex_m = graph.add_vertex("1")
vertex_n = graph.add_vertex("W")
vertex_o = graph.add_vertex("1")
vertex_p = graph.add_vertex("1")
vertex_q = graph.add_vertex("W")
vertex_r = graph.add_vertex("1")
vertex_s = graph.add_vertex("W")
vertex_t = graph.add_vertex("E")

graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_a, vertex_f)
graph.add_edge(vertex_b, vertex_c)
graph.add_edge(vertex_b, vertex_g)
graph.add_edge(vertex_c, vertex_h)
graph.add_edge(vertex_c, vertex_d)
graph.add_edge(vertex_d, vertex_e)
graph.add_edge(vertex_d, vertex_i)
graph.add_edge(vertex_e, vertex_j)
graph.add_edge(vertex_f, vertex_k)
graph.add_edge(vertex_f, vertex_g)
graph.add_edge(vertex_g, vertex_h)
graph.add_edge(vertex_g, vertex_l)
graph.add_edge(vertex_h, vertex_m)
graph.add_edge(vertex_i, vertex_n)
graph.add_edge(vertex_j, vertex_o)
graph.add_edge(vertex_k, vertex_p)
graph.add_edge(vertex_l, vertex_q)
graph.add_edge(vertex_l, vertex_m)
graph.add_edge(vertex_m, vertex_r)
graph.add_edge(vertex_m, vertex_n)
graph.add_edge(vertex_n, vertex_s)
graph.add_edge(vertex_n, vertex_o)
graph.add_edge(vertex_o, vertex_t)
graph.add_edge(vertex_p, vertex_q)
graph.add_edge(vertex_q, vertex_r)
graph.add_edge(vertex_r, vertex_s)
graph.add_edge(vertex_s, vertex_t)

graph.print_graph()

print("\n\n\n\n")
print("BFS Searched vertex, starting from S vertex")
graph.BFS("S")
