def ArrayToString(array):
    string=""
    for i in array:
        string+=i
    return string

def KMP(pattern , text):
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(text)
    pi = [0]*lengthPattren
    j = 0 #index pattern

    computePi(pattern, lengthPattren, pi)

    i = 0 #index text
    while i < lengthText:
        if pattern[j] == text[i]:
            i+=1
            j+=1
        if j == lengthPattren:
            Ans.append(i-j+1)
            # print((i-j+1),"LR")
            j = pi[j-1]
        elif i<lengthText and pattern[j] != text[i]:
            if j!=0:
                j=pi[j-1]
            else:
                i+=1
    return Ans

def computePi(pattern, lengthPattren, pi):
    length = 0
    i=1
    while i<lengthPattren:
        if pattern[i] == pattern[length]:
            length+=1
            pi[i] = length
            i+=1
        else :
            if length != 0:
                length = pi[length-1]
            else:
                pi[i]=0
                i+=1
    return pi

def reverseKMP(pattern, text):
    reversetext=text[::-1]
    reverseAns=[]
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(reversetext)
    pi = [0]*lengthPattren
    j = 0 #index pattern

    computePi(pattern, lengthPattren, pi)

    i = 0 #index text
    while i < lengthText:
        if pattern[j] == reversetext[i]:
            i+=1
            j+=1
        if j == lengthPattren:
            reverseAns.append(i-j)
            # print((i-j+1),"LR")
            j = pi[j-1]
        elif i<lengthText and pattern[j] != reversetext[i]:
            if j!=0:
                j=pi[j-1]
            else:
                i+=1
    for i in reverseAns:
        Ans.append(lengthText-i)
    return Ans

def KMPprint(pattern, text):
    lengthPattren=len(pattern)
    piSet=[0]*lengthPattren
    pi=computePi(pattern, lengthPattren, piSet)
    for i in pi:
        print(i,end=" ")
    LR=KMP(pattern, text)
    RL=reverseKMP(pattern, text)
    print()
    print(len(RL)+len(LR))
    for j in LR:
        print(str(j)+" LR")
    while len(RL)!=0:
        print(str(RL.pop())+" RL")

def Naive(pattern, text):
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(text)
    for i in range(lengthText-lengthPattren+1):
        j=0
        while(j<lengthPattren):
            if(text[i+j] != pattern[j]):
                break
            j+=1
        if(j==lengthPattren):
            # print(i+1,"LR")
            Ans.append(i+1)
    return Ans

def reverseNaive(pattern, text):
    reversetext=text[::-1]
    reverseAns=[]
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(reversetext)
    for i in range(lengthText-lengthPattren+1):
        j=0
        while(j<lengthPattren):
            if(reversetext[i+j] != pattern[j]):
                break
            j+=1
        if(j==lengthPattren):
            # print(i+1,"LR")
            reverseAns.append(i)
    for i in reverseAns:
        Ans.append(lengthText-i)
    return Ans

def Naiveprint(pattern, text):
    lengthPattren=len(pattern)
    piSet=[0]*lengthPattren
    pi=computePi(pattern, lengthPattren, piSet)
    for i in pi:
        print(i,end=" ")
    LR=Naive(pattern, text)
    RL=reverseNaive(pattern, text)
    print()
    print(len(RL)+len(LR))
    for j in LR:
        print(str(j)+" LR")
    while len(RL)!=0:
        print(str(RL.pop())+" RL")


file = open("9.4.txt","r")
charSet = file.readline().strip().split(" ")
numSet = file.readline().strip().split(" ")
patternSet = file.readline().strip().split(" ")
textSet = file.readline().strip().split(" ")
file.close()
pattern = ArrayToString(patternSet)
text = ArrayToString(textSet)

# KMPprint(pattern, text)
# Naiveprint(pattern, text)


"""
wrapAround

def ArrayToString(array):
    string=""
    for i in array:
        string+=i
    return string

def KMP(pattern , text):
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(text)
    pi = [0]*lengthPattren
    j = 0 #index pattern

    computePi(pattern, lengthPattren, pi)

    i = 0 #index text
    while i < lengthText+lengthPattren-1:
        if pattern[j] == text[i%lengthText]:
            i+=1
            j+=1
        if j == lengthPattren:
            Ans.append(i-j+1)
            # print((i-j+1),"LR")
            j = pi[j-1]
        elif i<lengthText+lengthPattren-1 and pattern[j] != text[i%lengthText]:
            if j!=0:
                j=pi[j-1]
            else:
                i+=1
    return Ans

def computePi(pattern, lengthPattren, pi):
    length = 0
    i=1
    while i<lengthPattren:
        if pattern[i] == pattern[length]:
            length+=1
            pi[i] = length
            i+=1
        else :
            if length != 0:
                length = pi[length-1]
            else:
                pi[i]=0
                i+=1
    return pi

def reverseKMP(pattern, text):
    reversetext=text[::-1]
    reverseAns=[]
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(reversetext)
    pi = [0]*lengthPattren
    j = 0 #index pattern

    computePi(pattern, lengthPattren, pi)

    i = 0 #index text
    while i < lengthText:
        if pattern[j] == reversetext[i]:
            i+=1
            j+=1
        if j == lengthPattren:
            reverseAns.append(i-j)
            # print((i-j+1),"LR")
            j = pi[j-1]
        elif i<lengthText and pattern[j] != reversetext[i]:
            if j!=0:
                j=pi[j-1]
            else:
                i+=1
    for i in reverseAns:
        Ans.append(lengthText-i)
    return Ans

def KMPprint(pattern, text):
    lengthPattren=len(pattern)
    piSet=[0]*lengthPattren
    pi=computePi(pattern, lengthPattren, piSet)
    for i in pi:
        print(i,end=" ")
    LR=KMP(pattern, text)
    RL=reverseKMP(pattern, text)
    print()
    print(len(RL)+len(LR))
    for j in LR:
        print(str(j)+" LR")
    while len(RL)!=0:
        print(str(RL.pop())+" RL")

def Naive(pattern, text):
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(text)
    for i in range(lengthText-lengthPattren+1):
        j=0
        while(j<lengthPattren):
            if(text[i+j] != pattern[j]):
                break
            j+=1
        if(j==lengthPattren):
            # print(i+1,"LR")
            Ans.append(i+1)
    return Ans

def reverseNaive(pattern, text):
    reversetext=text[::-1]
    reverseAns=[]
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(reversetext)
    for i in range(lengthText-lengthPattren+1):
        j=0
        while(j<lengthPattren):
            if(reversetext[i+j] != pattern[j]):
                break
            j+=1
        if(j==lengthPattren):
            # print(i+1,"LR")
            reverseAns.append(i)
    for i in reverseAns:
        Ans.append(lengthText-i)
    return Ans

def Naiveprint(pattern, text):
    lengthPattren=len(pattern)
    piSet=[0]*lengthPattren
    pi=computePi(pattern, lengthPattren, piSet)
    for i in pi:
        print(i,end=" ")
    LR=Naive(pattern, text)
    RL=reverseNaive(pattern, text)
    print()
    print(len(RL)+len(LR))
    for j in LR:
        print(str(j)+" LR")
    while len(RL)!=0:
        print(str(RL.pop())+" RL")

def wraparound(pattern, text):
    Ans=[]
    lengthPattren = len(pattern)
    lengthText = len(text)
    start = lengthText-lengthPattren+1
    for i in range(start,lengthText+lengthPattren-1):
        j=0
        while(j<lengthPattren):
            if(text[(i+j)%lengthText] != pattern[j]):
                break
            j+=1
        if(j==lengthPattren):
            # print(i+1,"LR")
            Ans.append(i+1)
    return Ans


file = open("9.5.txt","r")
charSet = file.readline().strip().split(" ")
numSet = file.readline().strip().split(" ")
patternSet = file.readline().strip().split(" ")
textSet = file.readline().strip().split(" ")
file.close()
pattern = ArrayToString(patternSet)
text = ArrayToString(textSet)

KMPprint(pattern, text)
# Naiveprint(pattern, text)
# x=wraparound(pattern, text)
# print(x)
"""