from collections import defaultdict 

class Graph:

    def __init__(self):
        self.graph = defaultdict(list) 
    
    def createEdge(self,i,j): 
        self.graph[i].append(j) 
    
    def BFS(self, source):
        queue = []
        visited = [False]*(len(self.graph)+1)
        queue.append(source)
        visited[source] = True
        while(queue):
            a = queue.pop()
            print(a)
            for i in self.graph[a]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

g = Graph() 
g.createEdge(0, 1) 
g.createEdge(1, 2) 
g.createEdge(2, 3) 
print("BFS is:")
g.BFS(0) 