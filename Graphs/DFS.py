from collections import defaultdict 

class Graph:

    def __init__(self):
        self.graph = defaultdict(list) 
    
    def createEdge(self,i,j): 
        self.graph[i].append(j) 
    
    def DFS(self, source, numberOfNodes):
        stack = []
        visited = [False]*(numberOfNodes)
        stack.append(source)
        while(stack):
            a = stack.pop(-1)
            if(visited[a]== False):
                print(a)
            visited[a] = True
            for i in self.graph[a]: 
                if visited[i] == False: 
                    stack.append(i) 
g = Graph() 
g.createEdge(0, 1) 
g.createEdge(0, 2) 
g.createEdge(0, 3) 
g.createEdge(1, 5) 
g.createEdge(1, 6) 
g.createEdge(2, 4)
g.createEdge(3, 4) 
g.createEdge(4, 1)
print("DFS is:")
g.DFS(0,7) 