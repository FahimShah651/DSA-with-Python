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

    def remove_vertex(self, vertex_data):
        for vertex in self.vertices:
            if vertex["data"] == vertex_data:
                for edge in vertex["edges"]:
                    edge["start"]["edges"].remove(edge)
                    edge["end"]["edges"].remove(edge)
                self.vertices.remove(vertex)
                break

    def remove_edge(self, start_data, end_data):
        for vertex in self.vertices:
            for edge in vertex["edges"]:
                if (edge["start"]["data"] == start_data) and (edge["end"]["data"] == end_data):
                    vertex["edges"].remove(edge)
                    break

    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex:", vertex["data"])
            print("Edges:")
            for edge in vertex["edges"]:
                print(f"{edge['start']['data']} --- {edge['end']['data']}")
            print()

    def search_data(self, vertex_data):
        found = False
        for vertex in self.vertices:
            if vertex["data"] == vertex_data:
                found = True
                print(f"Vertex {vertex_data} found")
                print("Its edges are:")
                for edge in vertex["edges"]:
                    print(f"{edge['start']['data']} --- {edge['end']['data']}")
                break
        if not found:
            print("Vertex not found")


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
print("\n")
print("\n")
# Search for specific vertex
graph.search_data(30)
print("\n")
graph.search_data(40)
