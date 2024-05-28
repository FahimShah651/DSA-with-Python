class Vertex:
    def __init__(self,data) :
        self.data = data
        self.edges = []
    def add_edge(self,edge):
        self.edges.append(edge)
        
class Edge:
    def __init__(self,start,end):
        self.start = start
        self.end =end
        
class Graph:
    def __init__(self) :
        self.vertices =[]
        
    def add_vertex(self,data):
        vertex = Vertex(data)
        self.vertices.append(vertex)
        return vertex
    
    def add_edge(self,start,end):   
        edge = Edge(start,end)
        start.add_edge(edge)
        end.add_edge(edge)
    
    def remove_vertex(self,vertix):
        for i in self.vertices:
            if  vertix == i.data:
              self.vertices.remove(i)
              for j in i.edges:
                 print((j.start.data))

    def search_data(self,vertix):
        a = True
        for i in self.vertices:
            if  vertix == i.data:
                print(f" Vertix {vertix} found ")
                print("Its edges are :")
                for edge in i.edges:
                   print(f"{edge.start.data} --- {edge.end.data}")
                break
            else:
                a = False
        if a == False:
            print("Vertix Not found")
    
    
    def print_graph(self):
        for vertex in self.vertices:
            print("Vertex : ",vertex.data)
            print("Edge : ")
            for edge in vertex.edges:
                   print(f"{edge.start.data} --- {edge.end.data}")
            print()
            
     
garph =Graph()

Vertex_a = garph.add_vertex("A")
Vertex_b = garph.add_vertex("B")
Vertex_c = garph.add_vertex("C")
Vertex_d = garph.add_vertex("D")

garph.add_edge(Vertex_a,Vertex_b)
garph.add_edge(Vertex_b,Vertex_c)
garph.add_edge(Vertex_c,Vertex_d)
garph.add_edge(Vertex_d,Vertex_a)


garph.print_graph()
garph.search_data("A")
garph.search_data("F")

