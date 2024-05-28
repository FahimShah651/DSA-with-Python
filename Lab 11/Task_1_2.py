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
            
    def DFS(self,data,visited = set()):  #lifo
        check = False
        for vertex in self.vertices:
            if vertex.data ==data :
                check = True
                print(f"Vertix : {vertex.data} " )
                visited.add(vertex.data)
                for edge in vertex.edges:
                    if edge.end.data not in visited:
                        self.DFS(edge.end.data,visited) 
                    if edge.start.data not in visited:
                        self.DFS(edge.start.data,visited)
        if check == False:
            print("Vertex not found in Graph")
            
         
    def BFS(self,data):  #fifo
        queue = []
        visited = set()
        check = False
        for vertex in self.vertices:
            if vertex.data ==data :
                check = True
                queue.append(vertex)
                visited.add(vertex)
                while queue:
                   current_vertex =  queue.pop(0)
                   print(f"Visited vertex: {current_vertex.data}")
                   for edge in current_vertex.edges:
                     end_next_vertex = edge.end
                     start_next_vertex = edge.start
                     if end_next_vertex not in visited:
                        visited.add(end_next_vertex)
                        queue.append(end_next_vertex)
                     if start_next_vertex not in visited:
                        visited.add(start_next_vertex)
                        queue.append(start_next_vertex)
                break
        if check == False:
            print("Vertex not found in Graph")
            
                        
        
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

print("\n\n\n\n")
print("DFS Searched vertex , starting from G vertex")
graph.DFS("A")

# print("\n\n\n\n")
# print("BFS Searched vertex , starting from G vertex")
# graph.BFS("G")


