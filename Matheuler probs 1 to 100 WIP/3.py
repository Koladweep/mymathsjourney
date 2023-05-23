#naive code to factorize



def isprime(N):
    copy=N
    i=2 if N%2==0 else 3
    while i<int(copy**.5)+ 1:
        if copy%i==0:
            return False
        i+=2
    return True





def factorize(num):
    PF=dict()
    i=2 if num%2==0 else 3
    num2=num
    root=int(num2**.5)+1
    while num2>1 and i<=root:
        if num%i==0 and isprime(i):
            count=0
            while num2%i==0:
                num2=num2/i
                #add power counter here
                count+=1
            PF[i]=count
        i+=2
    if num2>1:
        PF[(int(num2))]=int(num2)
    return PF
print(factorize(11111111111119*181)) 