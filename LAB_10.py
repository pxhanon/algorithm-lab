from itertools import combinations
from collections import defaultdict
import copy

def BruteForceVertexCover(Problem):
    file = open(Problem,"r")
    K = int(file.readline().strip())
    Matrix = [[int(y) for y in x.strip().split(" ")] for x in file.readlines()]
    file.close()
    numVortex = len(Matrix)
    vortex = [i for i in range(numVortex)]
    combiVortex=[[y for y in x] for x in combinations(vortex,K)]
    Ans=[]
    for i in combiVortex:
        clone=copy.deepcopy(Matrix)
        for j in i:
            clone[j]=[0]*numVortex
            for k in range(numVortex):
                if Matrix[j][k] == 1:
                    clone[k][j] = 0
        if sum([sum(x) for x in clone]) == 0:
            Ans.append(i)

    if len(Ans) == 0:
        print("No")
    else :
        print("Yes")
        for i in Ans:
            i=[i+1 for i in i]
            print(*i)

# BruteForceVertexCover("10.2.0.txt")

def ApproximateMaxEdge(Problem):
    file = open(Problem,"r")
    Matrix = [[int(y) for y in x.strip().split(" ")] for x in file.readlines()]
    file.close()
    Vertex=len(Matrix)
    Ans=[]
    clone=copy.deepcopy(Matrix)
    NoEdge=[[0]*Vertex]*Vertex
    while clone != NoEdge:
        maxEdge = 0
        for i in range(Vertex):
            Edge = 0
            for j in range(Vertex):
                if clone[i][j] == 1:
                    Edge+=1
            if Edge >= maxEdge:
                maxEdge = Edge
                Point = i
        for k in range(Vertex):
            clone[Point][k] = 0
            clone[k][Point] = 0
        Ans.append(Point+1)
    print(*Ans)
    print(len(Ans))

# ApproximateMaxEdge("2.3.txt")

def ApproximateVisitPoint(Problem):
    file = open(Problem,"r")
    Matrix = [[int(y) for y in x.strip().split(" ")] for x in file.readlines()]
    file.close()
    Vertex=len(Matrix)
    Graph=defaultdict(list)
    for i in range(Vertex):
        for j in range(Vertex):
            if Matrix[i][j]==1:
                Graph[i].append(j)
    Ans=[]
    visited = [False]*Vertex
    for u in range(Vertex):
        if not visited[u]:
            for v in Graph[u]:
                if not visited[v]:
                    visited[u]=True
                    visited[v]=True
                    break
    for k in range(Vertex):
        if visited[k]:
            Ans.append(k+1)
    print(*Ans)
    print(len(Ans))

# ApproximateVisitPoint("10.3.0.txt")

def Reduce(Problem):
    file = open(Problem,"r")
    num = int(file.readline().strip())
    literal = [[int(y) for y in x.strip().split(" ")] for x in file.readlines()]
    file.close()
    AllLiteral=[]
    for i in literal:
        for j in i:
            if not(abs(j) in AllLiteral):
                AllLiteral.append(abs(j))
    numLiteral=len(AllLiteral)
    Vortex=2*numLiteral+3*num
    VortexCover=numLiteral+2*num

    p=2*numLiteral

    Matrix=[[0 for y in range(Vortex)] for x in range(Vortex)]
    for i in range(0,2*numLiteral,2):
        Matrix[i][i+1]=1
        Matrix[i+1][i]=1

    for i in range(num):
        Matrix[p][p+1]=Matrix[p+1][p]=1
        Matrix[p][p+2]=Matrix[p+2][p]=1
        Matrix[p+1][p+2]=Matrix[p+2][p+1]=1
        for j in range(3):
            v=((abs(literal[i][j])-1)*2)
            if literal[i][j]>0 :                             
                Matrix[p+j][v]=Matrix[v][p+j]=1
            else:
                Matrix[p+j][v+1]=Matrix[v+1][p+j]=1  
        p+=3

    print(Vortex)
    print(VortexCover)
    for x in Matrix:
        print(*x)

# Reduce("3.3.txt")