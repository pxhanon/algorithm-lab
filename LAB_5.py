from math import sqrt
MAX = 1000000.0
def dist(p1, p2):
    return sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))
def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)
def mTCDP(points, n):
    if (n < 3):
        return 0
    table=[[0 for x in range(n)] for x in range(n)]
    g=0
    while(g<n):
        i=0
        j=g
        while(j<n):
            if j<i+2:
                table[i][j]=0
            else:
                table[i][j]=MAX
                k=i+1
                while k<j:
                    val = table[i][k] + table[k][j] + cost(points,i,j,k)
                    if table[i][j] > val:
                        table[i][j] = val
                    k+=1
            i+=1
            j+=1
        g+=1
    return table[0][n-1]


with open('6 Extra.txt', 'r') as f:
    points = [[float(num) for num in line.split(' ')] for line in f]
points.remove(points[0])


#points = [[-5.5,-2], [4,0], [15,7], [2,10], [-3,6]]
n = len(points)
print(mTCDP(points,n))
