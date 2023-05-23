#naive code to factorize
def isprime(N):
    copy=N
    i=2 if N%2==0 else 3
    if type(N) !=int: #N is outside domain of isprime function
        return False 
    elif N<2: #N is outside domain of isprime function
        return False
    while i<int(copy**.5)+ 1:
        if copy%i==0:
            return False
        i+=2
    return True


def factorize(num):
    PF=dict()
    i=2 if num%2==0 else 3#for odd numbers, we start from 3 else from 2
    root=int(num**.5)+1
    switch=True if i==2 else False
    while(num>root):
        if num%i==0:
            count=0
            if isprime(i):
                while(num%i==0):
                    num=int(num/i)
                    count+=1
                PF[i]=count
        if switch:
            i=3;switch=False;continue
        i+=2
    return PF

#below method finds LCM of a list of numbers provided to it by finding the maximum power of all prime factors of all numbers in the list and multiplying together all such prime factors raised to that power
'''Logic:
1)accept a list to find LCM for
2)create a list of dictionaries of thier prime factors and their respective powers
3) create a set of their prime factors
4)create a dictionary of prime factors and thier largest powers in the entire list of PFdictionaries
'''
def LCM(L):
    PFs=dict()
    for i in L:
        PFi=factorize(i)
        for PF in PFi:
            if PF in PFs :
                if PFs[PF]<PFi[PF]:#if a greater power of a known prime factor is encountered, we update the entry by replacing previous onne with the higher power
                    PFs[PF]=PFi[PF]
                else:#a lower power than a known power of of a known Prime factor is encountered, we do nothing.
                    pass
            else:#if PF is a newly encountered prime factor, we create a new entry.
                PFs[PF]=PFi[PF] #recording the PF and it's respective power
    lcm=1
    for PF in PFs:
        lcm*=PF**PFs[PF]#cumulative multiplication of all common prime factors of all numbers in List L raised to max power in which they exist in any of the numbers in L
    return lcm