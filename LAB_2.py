class Graph():
    def permutations(self,lst):
        if len(lst)==0:
            return []
        if len(lst)==1:
            return [lst]
        per=[]
        for i in range(len(lst)):
            m=lst[i]
            remlst = lst[:i] + lst[i+1:]
            for p in self.permutations(remlst):
                per.append([m] + p)
        return per

    def __init__(self,size):
        self.graph=[[0 for colum in range(size)] for row in range(size)]
        self.V=size

    def hamcycle(self):
        Allcycle=[]
        Ans=[]
        for i in list(self.permutations([i for i in range(self.V)])):
            if(i[0]>=1):
                break
            Allcycle.append(i)
        for i in range(len(Allcycle)):
                if self.checkcycle(Allcycle[i],0) == True:
                        Ans.append(Allcycle[i])
        #print(Ans)
        return Ans

    def checkcycle(self,path,pos):
        if pos == self.V:
            if self.graph[ path[pos-1] ][ path[0] ] >= 1:
                return True
            else:
                return False
        for v in range(self.V):
                if self.checkline(v, pos, path) == True:
                    if self.checkcycle(path, pos+1) == True:
                        return True
        return False

    def checkline(self,v,pos,path):
        if self.graph[path[pos]][path[(pos+1)%self.V]] >= 1:
            return True
        return False

    def hampath(self):
        Ans=[]
        AllPath=[]
        possiblePath=self.permutations([i for i in range(self.V)])
        for i in list(possiblePath):
            AllPath.append(i)
        for i in range(len(AllPath)):
                if self.checkpath(AllPath[i],0) == True:
                        Ans.append(AllPath[i])
        #print(Ans)
        return Ans

    def checkpath(self,path,pos):
        if pos == self.V:
            return True
        for v in range(self.V):
                if self.checkline(v, pos, path) == True:
                    if self.checkpath(path, pos+1) == True:
                        return True
        return False

    def path(self,u,v):
        next=[]
        for i in range(len(u)):
            if self.graph[i] == 1:
                next.append(i)
        for x in next:
            if x==v:
                return True

    def path2(self,u,v):
        start=[]
        end=[]
        if u==v:
            return "It's a dot"
        if u<-1 or v<-1 or u>self.V or v>self.V:
            return "The dot does not in this graph"
        origin=self.hampath()
        for i in range(len(origin)):
            if origin[i][0] == u:
                start.append(origin[i])
        for path in start:
            mid=[]
            for j in range(len(path)):
                if path[j]==v:
                    mid.append(path[:(j+1)])
                else:
                    continue
            end.append(mid)
        #print(end)
        return end

    def newPath(self,u,v):
        if u==v:
            return "It's a dot"
        if u<-1 or v<-1 or u>self.V or v>self.V:
            return "The dot does not in this graph"
        if self.graph[u][v]==0:
            self.graph[u][v] = 1
            self.graph[v][u] = 1
            return "the new path has been added"
        else :
            return "the path is already have"

    def removePath(self,u,v):
        if u==v:
            return "It's a dot"
        if u<-1 or v<-1 or u>self.V or v>self.V:
            return "The dot does not in this graph"
        if self.graph[u][v]==1:
            self.graph[u][v] = 0
            self.graph[v][u] = 0
            return "the new path has been removeed"
        else :
            return "the path is already have no"

"""
g1 = Graph(6)
g1.graph = [[0,1,0,0,0,1],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,1,0,1,0],[0,0,0,1,0,1],[1,0,0,0,1,0]]
g1.hamcycle()
"""
"""
g2 = Graph(15)
g2.graph = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
            ,[1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1]
            ,[1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1]
            ,[1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1]
            ,[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]]
g2.hamcycle()
"""
"""
g3 = Graph(4)
g3.graph=[[1,2,0,2],[2,1,2,1],[0,2,0,2],[2,1,2,1]]
g3.hamcycle()
"""

"""
g4 = Graph(8)
g4.graph=[[0,0,1,1,0,0,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,1],[0,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,0]]
check=0
for i in range(len(g4.graph)):
    if check==0:
        for j in range(len(g4.graph)):
            if g4.hamcycle() == []:
                if g4.newPath(i,j)=="the new path has been added":
                    g4.newPath(i,j)
            else :
                check=1
                break
    else :
        break
print(g4.hamcycle())
"""

"""
g4 = Graph(8)
g4.graph=[[0,0,1,1,0,0,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,1],[0,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,0]]
if g4.hamcycle() == []:
    check=0
    error=0
    string=""
    for i in range(len(g4.graph)):
        if check == 0:
            for j in range(len(g4.graph)):
                if g4.newPath(i,j)=="the new path has been added":
                    g4.newPath(i,j)
                    if g4.hamcycle() == []:
                        g4.removePath(i,j)
                    else :
                        check=1
                        break
        else :
            error=1
            break
if error==1:
    print(g4.hamcycle())
else :
    print("can't be add one path for create the hamcycle")
"""
