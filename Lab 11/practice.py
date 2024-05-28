def dfs(graph,node,visited = set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)
        
def bfs(graph,visited):
    queue = []
    queue.append(1)
    visited[1]= True
    while queue:
        temp = queue.pop(0)
        print(temp)
        for child in graph[temp]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True
                
                
inp = [[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,5],[4,6],[5,6]]

graph = {}

n = 6
for i in range(1,n+1):
    graph[i] = []
for (u,v) in inp:
    graph[u].append(v)
    graph[v].append(u)
  
visited = {}  
for i in range(1,n+1):
   graph[i] = []
   visited[i] = False 

print(graph)

dfs(graph,5)
bfs(graph,visited)

