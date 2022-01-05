from collections import defaultdict
INF=999999
class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
        self.adjMtx = [[INF for colum in range(vertex)] for row in range(vertex)]
        for v in range(self.V):
            self.adjMtx[v][v]=0

    def add_edge(self, s, d):   # Add edge into the graph
        self.graph[s].append(d)
        self.adjMtx[s][d] = 1

    def add_new(self, s, d):
        component = self.scc()
        self.add_edge(component[s][0],component[d][0])

    def compress(self):
        graphscc = defaultdict(list)
        component = self.scc()
        for i in range(len(component)):
            for x in component[i]:
                for k in self.graph[x]:
                    for j in range(len(component)):
                        if k in component[j] and i!=j:
                            if not(j in graphscc[i]):
                                graphscc[i].append(j)
        return(self.degree(len(component),graphscc))

    def degree(self, v, g):
        inDeg = [0 for i in range(v)]
        outDeg = [0 for i in range(v)]
        for i in range(v):
            for j in g[i]:
                outDeg[i] += 1
                inDeg[j] += 1
        for x in range(v):
            for y in range(v):
                if x!=y and outDeg[x] == 0 and inDeg[y] == 0:
                    return [x,y]

    def dfs(self, d, visited_vertex,temp):   # dfs
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex,temp)
        temp = temp.append(d)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    def transpose(self):    # transpose the matrix
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def scc(self):    # stongly connected components
        stack = []
        scc_list=[]
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            temp=[]
            i = stack.pop()
            if not visited_vertex[i]:
               gr.dfs(i, visited_vertex,temp)
               scc_list.append(temp)
        return scc_list

    def floydWarshall(self, graph):
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        for k in range(len(graph[0])):
            for i in range(len(graph[0])):
                for j in range(len(graph[0])):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        return(dist)

    def print_floyd(self):
        Ans=0
        floyd=self.floydWarshall(self.adjMtx)
        for i in floyd :
            for j in i :
                if j==INF:
                    Ans+=1
        if Ans == 0 :
            print(1)
        else :
            print(0)
            

with open("6.6.txt","r") as s:
    graph = [[int(num) for num in line.split(' ')] for line in s]

many=-1
for g in graph:
    if (len(g)==2):
        many+=1

mtx=[]
i=0
while graph[i] != [0,0]:
    e=graph[i][1]
    temp=[]
    temp.append(graph[i])
    i+=1
    for j in range(e):
        temp.append(graph[i])
        i+=1
    mtx.append(temp)

for x in mtx:
    e=[]
    g = Graph(x[0][0])
    for i in range(1,len(x)):
        if x[i][2] == 1 :
            e.append(x[i][0:2])
        else :
            e.append(x[i][0:2])
            rev=x[i][0:2]
            rev.reverse()
            e.append(rev)
    for j in e:
        g.add_edge(j[0]-1,j[1]-1)
    print(g.scc())
    g.print_floyd()
    n=0
    while(len(g.scc())!=1):
        n+=1
        g.add_new(g.compress()[0],g.compress()[1])
        print("step : ",n," ", g.scc())
    print("")
    print(g.scc())
    g.print_floyd()
    print("---------------------------")