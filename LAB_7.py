def floydWarshall(graph,n):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],max(dist[i][k],dist[k][j]))
    return(dist)

def pie(graph,n):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    newgraph = [[None for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(dist[i][j]!=0 and dist[i][j]!=999999):
                newgraph[i][j]= i     
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(dist[i][j]<=max(dist[i][k],dist[k][j])):
                    newgraph[i][j] = newgraph[i][j]
                    dist[i][j]=dist[i][j]
                else:
                    newgraph[i][j] = newgraph[k][j]
                    dist[i][j]=max(dist[i][k],dist[k][j])
    for i in range(n):
        for j in range(n):
            if(newgraph[i][j]!= None):
                newgraph[i][j]= newgraph[i][j]
    # print(graph)
    # print("____________________")
    # print(dist)
    # print("____________________")
    # print(newgraph)
    return(newgraph)

def traceback(graphD,graphP,start,end):
    if(graphD[start][end] == 999999):
        return "no path"
    path = [start,end]
    while(path[0]!=path[1]):
        path.insert(1,graphP[path[0]][path[1]])
    path.pop(0)
    return path

def CQ(graph):
    check = graph
    eage = graph[0][1]
    del check[0:eage+1]
    return(check)

with open("7_extra1.txt","r") as s:
    graph = [[int(num) for num in line.split(' ')] for line in s]
N=graph[0][0]
INIT = 999999
adjMtx = [[INIT for colum in range(N)] for row in range(N)]
for x in range(N):
    adjMtx[x][x]=0
for i in range(1,graph[0][1]+1):
    adjMtx[graph[i][0]-1][graph[i][1]-1]=graph[i][2]
    # adjMtx[graph[i][1]-1][graph[i][0]-1]=graph[i][2]

floyd=floydWarshall(adjMtx,N)
for i in range(graph[0][1]+1,graph[0][1]+graph[0][2]+1):
    print(floyd[graph[i][0]-1][graph[i][1]-1])

Pie=pie(adjMtx,N)
# Check = CQ(graph)
# print(Check)
# print(graph)
for i in range(graph[0][1]+1,graph[0][1]+graph[0][2]+1):
    trace = traceback(floyd,Pie,graph[i][0]-1,graph[i][1]-1)
    print(trace)
# print(floyd)
# print(Pie)




