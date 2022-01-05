def brute(arr,k):
    Grab=[]
    Passenger=[]
    Ans=0
    for i in range(len(arr)):
        if arr[i]=="G":
            Grab.append(i)
        elif arr[i]=="P":
            Passenger.append(i)
        else :
            print("there are the stranger thing : ",arr[i]," pos ",i )
    for i in Grab:
        for j in Passenger:
            if abs(i-j) <= k:
                Ans+=1
                Passenger.remove(j)
                break
    return print(Ans)

def greedy(arr,k):
    Ans=0
    try:
        Grab=arr.index("G")
    except:
        return print("There is no Grab")
    try :
        Passenger=arr.index("P")
    except:
        return print("There is no Passenger")
    while len(arr)>0:
        if abs(Grab-Passenger) <= k:
            Ans+=1
            try:
                arr.remove("G")
                arr.remove("P")
                Grab=arr.index("G")
                Passenger=arr.index("P")
            except:
                break
        elif Passenger < Grab :
            try:
                arr.remove("P")
                Grab=arr.index("G")
                Passenger=arr.index("P")
            except:
                break
        else :
            try:
                arr.remove("G")
                Grab=arr.index("G")
                Passenger=arr.index("P")
            except:
                break
    return print(Ans)

def word(string):
    return [str(x) for x in string]
