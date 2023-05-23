soltuple=[]
def findpythatrip(N):
    for c in range(0,1001):
        bal=1000-c
        for b in range(0,bal+1):
            a=bal-b
            if a**2 + b**2 == c**2:
                return ((a,b,c), a*b*c)
    return "No such triplet found in specified range for N"
print(findpythatrip(1000))