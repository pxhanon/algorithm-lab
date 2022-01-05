def Max_diff(a):
    if(len(a)>=2):
        minright = min(a)
        minrightlocation = a.index(minright)
        maxleft = max(a)
        maxleftlocation = a.index(maxleft)
        if (minrightlocation<maxleftlocation):
            max_diff = maxleft-minright
            return max_diff
        else :
            maxright = max(a[minrightlocation:len(a)])
            maxrightlocation = a[minrightlocation:len(a)].index(maxright)
            minleft = min(a[0:maxleftlocation+1])
            minleftlocation = a[0:maxleftlocation+1].index(minleft)
            if(maxright-minright < maxleft-minleft):
                max_diff = maxleft-minleft
            else :
                max_diff = maxright-minright
            mid = Max_diff(a[maxleftlocation+1:minrightlocation])
            if (max_diff < mid):
                return mid
            else :
                return max_diff
    else :
        return 0

def bruteforce(arr):
    ans = 0
    for i in range (len(arr)):
        for j in range (len(arr)):
            if (i<j) and (arr[j]-arr[i]>ans):
                ans = arr[j]-arr[i]
                bday = i
                sday = j
    print("The location of minimum number", bday+1)
    print("The minimum number in a given array is : ", arr[bday])
    print("The location of maximum number", sday+1)
    print("The maximum number in a given array is : ", arr[sday])
    print("The difference of max and min", ans)
    print("The date of hold USD", sday-bday)
    return



# file=open("8.6.txt","r")
# date = file.readline()
# cost = file.readline().strip().split(" ")
# a=[float(i) for i in cost]
# a = [43.12,44.49,43.01,41.54,40.32,50.12,38.91,49.40,35.99,48.33,31.72,30.72,31.07,30.48,32.48,34.25,35.29,33.93,32.32,31.18]
# x=Max_diff(a)
# print("%.2f"%x)
# x=bruteforce(a)
# -------------------------------------------------------------------------------------------------------------------------------
file=open("8.6.txt","r")
date = file.readline()
cost = file.readline().strip().split(" ")
file.close()
x=[float(i) for i in cost]
a=[float(i) for i in cost]

# x = [43.12,44.49,43.01,41.54,40.32,30.48,38.91,49.40,35.99,48.33,31.72,30.72,31.07,50.12,32.48,34.25,35.29,33.93,32.32,31.18]
# a = [43.12,44.49,43.01,41.54,40.32,30.48,38.91,49.40,35.99,48.33,31.72,30.72,31.07,50.12,32.48,34.25,35.29,33.93,32.32,31.18]
# x = [35.10,35.01,35.11,35.02,35.08,35.03,35.09,35.12,35.04,35.17,35.14,35.19,35.13,35.07,35.16,35.20,35.06,35.05,35.18,35.16]
# a = [35.10,35.01,35.11,35.02,35.08,35.03,35.09,35.12,35.04,35.17,35.14,35.19,35.13,35.07,35.16,35.20,35.06,35.05,35.18,35.16]
# x = [43.12,44.49,43.01,41.54,40.32,50.12,38.91,49.40,35.99,48.33,31.72,30.72,31.07,30.48,32.48,34.25,35.29,33.93,32.32,31.18]
# a = [43.12,44.49,43.01,41.54,40.32,50.12,38.91,49.40,35.99,48.33,31.72,30.72,31.07,30.48,32.48,34.25,35.29,33.93,32.32,31.18]

temp=[]
Ans=[]
left=0
right=len(a)

while(True):
    if max(a)==0:
        break
    maxleft = max(a[left:right])
    maxleftlocation = a.index(maxleft)
    minright = min(a[left:right])
    minrightlocation = a.index(minright)
    if minrightlocation < maxleftlocation :
        Ans.append([minrightlocation,maxleftlocation])
        break
    else :
        temp.append([maxleftlocation,minrightlocation])
        left=maxleftlocation+1
        right=minrightlocation
        for i in range(maxleftlocation+1):
            a[i]=0
        for i in range(minrightlocation,len(a)):
            a[i]=0

left=0
right=len(a)-1
for t in temp:
    Ans.append([left,t[0]])
    left=t[0]+1
    Ans.append([t[1],right])
    right=t[1]-1

listDiff=[]
for i in Ans:
    Max = max(x[i[0]:i[1]+1])
    Min = min(x[i[0]:i[1]+1])
    Diff = Max-Min
    listDiff.append(Diff)

Max_diff = max(listDiff)
location = listDiff.index(Max_diff)
for i in range(Ans[location][0]):
    x[i]=0
for i in range(Ans[location][1]+1,len(a)):
    x[i]=0
buycost=min(x[Ans[location][0]:Ans[location][1]+1])
sellcost=max(x[Ans[location][0]:Ans[location][1]+1])
buydate=x.index(buycost)
selldate=x.index(sellcost)

print("Buy Date  :",buydate+1)
print("Buy       : %.2f"%buycost)
print("Sell Date :",selldate+1)
print("Sell      : %.2f"%sellcost)
print("Profit    : %.2f"%Max_diff)
print("Hold      :",selldate-buydate)