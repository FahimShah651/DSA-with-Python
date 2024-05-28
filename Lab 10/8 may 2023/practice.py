class Graph:
    def __init__(self) -> None:
        self.vertices = []
        self.edges = []
        
    def add_vertex(self,data):
        self.vertices.append(data)
    
    def add_edge(self,start,end):
        edg = []
        edg.append(start)
        edg.append(end)
        self.edges.append(edg)
        
    def dispaly_vertices(self):
        for vertix in self.vertices:
            print("Vertix : ",vertix)
            print("Edge :")
            for edge in self.edges:
                print(edge)
                
                
     
garph =Graph()
Vertex_a = garph.add_vertex("A")
Vertex_b = garph.add_vertex("B")
Vertex_c = garph.add_vertex("C")
Vertex_d = garph.add_vertex("D")

garph.add_edge(Vertex_a,Vertex_b)
garph.add_edge(Vertex_b,Vertex_c)
garph.add_edge(Vertex_c,Vertex_d)
garph.add_edge(Vertex_d,Vertex_a)


garph.dispaly_vertices()
        