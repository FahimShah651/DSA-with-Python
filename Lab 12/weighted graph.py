class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)
        return edge


class Edge:
    def __init__(self, start, weight, end):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, data):
        vertex = Vertex(data)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, start, weight, end):
        edge = Edge(start, weight, end)
        start.add_edge(edge)
        end.add_edge(edge)
        return edge

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            # Remove the vertex from all connected edges
            for edge in vertex.edges:
                if edge.start == vertex:
                    edge.end.edges.remove(edge)
                else:
                    edge.start.edges.remove(edge)
            # Remove the vertex from the graph
            self.vertices.remove(vertex)

    def remove_edge(self, edge):
        start = edge.start
        end = edge.end
        start.edges.remove(edge)
        end.edges.remove(edge)

    def incident_edges(self, v):
        incident_edges = []
        for edge in v.edges:
            if edge.start == v:
                incident_edges.append(edge)
            else:
                # For an undirected graph, consider both directions of the edge
                incident_edges.append(Edge(edge.end, edge.weight, edge.start))
        return incident_edges

    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex:", vertex.data)
            print("Edges:")
            for edge in vertex.edges:
                print(f"{edge.start.data} -[{edge.weight}]-> {edge.end.data}")
            print()

    def djk(self):
        dictionary_list = []
        for i in self.vertices:
            dictionary = {
                "Vertix ": i.data,
                "Cost ": float('inf')
            }
            dictionary_list.append(dictionary)
        dictionary_list[0].update({"Cost ": 0})
        self.assign(dictionary_list)
        for i in dictionary_list:
            print(i)

    def assign(self, dictionary_list, visited=set()):
        n = 0
        for i in self.vertices:
            visited.add(i.data)
            for edge in i.edges:

                #  print(dictionary_list[n].get("Cost "), " edge  : ",edge.start.data," -- ", edge.weight, " -- ",edge.end.data)
                if edge.end.data not in visited:
                    if dictionary_list[n].get("Cost ") < edge.weight:
                        #  print("return index : ", a)
                        dictionary_list[self.find_vertix(edge.end.data)].update(
                            {"Cost ": (dictionary_list[n].get("Cost ") + edge.weight)})
                    
                if edge.start.data not in visited:

                    if dictionary_list[n].get("Cost ") < edge.weight:
                        #  print("return index : ", a)
                        dictionary_list[self.find_vertix(edge.start.data)].update(
                            {"Cost ": (dictionary_list[n].get("Cost ") + edge.weight)})

            n = n+1

    def find_vertix(self, vertex):
        n = 0
        for i in self.vertices:
            if vertex == i.data:
                return n
            n = n+1


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
graph.djk()
