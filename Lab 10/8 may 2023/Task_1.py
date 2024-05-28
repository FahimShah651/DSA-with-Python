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
                    self.remove_edge(edge.start.data,edge.end.data)
                if edge.end.data == vertex:
                    self.remove_edge(edge.start.data,edge.end.data)
      
          
    def remove_edge(self, start, end):
        for vertex in self.vertices:
            for edge in vertex.edges:
                if (edge.start.data == start) and (edge.end.data == end):
                    #print(f" edges of vertix : {vertex.data} : {edge.start.data} -- {edge.end.data}")
                    vertex.edges.remove(edge)

    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex:", vertex.data)
            print("Edges:")
            for edge in vertex.edges:
                print(f"{edge.start.data} --- {edge.end.data}")
            print()


graph = Graph()

vertex_a = graph.add_vertex(10)
vertex_b = graph.add_vertex(20)
vertex_c = graph.add_vertex(30)
vertex_d = graph.add_vertex(40)
vertex_e = graph.add_vertex(50)
vertex_f = graph.add_vertex(60)

graph.add_edge(vertex_a, vertex_e)
graph.add_edge(vertex_a, vertex_d)
graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_b, vertex_c)
graph.add_edge(vertex_c, vertex_d)
graph.add_edge(vertex_e, vertex_f)
graph.add_edge(vertex_f, vertex_d)

graph.print_graph()

graph.remove_vertex(60)
print("\nAfter removing vertex 60:")
graph.print_graph()

graph.remove_edge(20, 30)
print("\nAfter removing edge between 20 and 30 :")
graph.print_graph()
