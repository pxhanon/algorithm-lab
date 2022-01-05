import math
import numpy
import sys
def FINDGCD1(x,y):
    x=abs(x)
    y=abs(y)
    t=min(x,y)
    if (t==0):
        return max(x,y)
    while(x%t!=0 or y%t!=0):
            t-=1
    return t

def FINDGCD2(x,y):
    x=abs(x)
    y=abs(y)
    t=min(x,y)
    if (t==0):
        return max(x,y)
    def PrimeFactor(n):
        t = []
        i=2
        while(i<=n):
            if n%i==0:
                t.append(i)
                n=n/i
            else:
                i+=1 
        return t
    s=[]
    i=0
    j=0
    while(i<len(PrimeFactor(x)) and j<len(PrimeFactor(y))):
        if(PrimeFactor(x)[i]==PrimeFactor(y)[j]):
            s.append(PrimeFactor(x)[i])
            i+=1
            j+=1
        else:
            if((PrimeFactor(x)[i])<(PrimeFactor(y)[j])):
                i+=1
            else:
                j+=1
    if(len(s)==0):
        return 1
    else:
        return numpy.prod(s)

def FINDGCD3(x,y):
    x=abs(x)
    y=abs(y)
    t=min(x,y)
    if (t==0):
        return max(x,y)
    while (x/y > 100):
        x=x-(100*y)
    while (y/x > 100):
        y=y-(100*x)
    if x > y:
        return FINDGCD3(x-y,y)
    elif x == y:
        return x
    else:
        return FINDGCD3(x,y-x)

#print(FINDGCD1(FINDGCD1(-15,0),FINDGCD1(20,-25)))
#print(FINDGCD2(FINDGCD2(-15,0),FINDGCD2(20,-25)))
#print(FINDGCD3(FINDGCD3(-15,0),FINDGCD3(20,-25)))

#print(FINDGCD1(-2,-4))
#print(FINDGCD2(-2,-4))
#print(FINDGCD3(-2,-4))

#print(FINDGCD1(FINDGCD1(189,252),FINDGCD1(1197,292005)))
#print(FINDGCD2(FINDGCD2(189,252),FINDGCD2(1197,292005)))
#print(FINDGCD3(FINDGCD3(189,252),FINDGCD3(1197,292005)))

#print(FINDGCD1(FINDGCD1(36,84),120))
#print(FINDGCD2(FINDGCD2(36,84),120))
#print(FINDGCD3(FINDGCD3(36,84),120))