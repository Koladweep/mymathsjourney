
def countchain(n):
    count=0
    while n>1:
        if n%2==0:
            count+=1
            n=n/2#skip ahead 1 step
        else:
            count+=2
            n=((3*n)+1)/2#skip ahead 2 steps(count odd and count next even(3n+1 is even if n is odd))
    return count
#print(countchain(837799))



longestchain=0
longestn=0
from time import time
start=time()
ctime=0
for i in range(500000,1000000):
    ichain=countchain(i)
    if ichain>longestchain:
        longestchain=ichain
        longestn=i
        ctime=time()-start#time to compute longest chain
    print(f'\r longest visible chain ={ichain:3.3f}, for {i} in {ctime:.2f} seconds, timelapse: {time()-start:.2f}',end='', flush=True)
print(f'longest collatz chain computed {longestchain} for {longestn} in {ctime:.2f} seconds')
#below is my bruteforce solution and above is the optimum Project Euler solution
'''
n=1000000
countmax=0
count=0
reccollatz=0#to record the longest tailed collatz number
from time import time
start=time()
tmax=0#time taken to compute longest chain
while n>=1:
    collatz=n

    while collatz!=1:
        collatz=collatz/2 if collatz%2==0 else 3*collatz+1
        count+=1
    
    if countmax<count:
        countmax=count
        reccollatz=n
        tmax=time()-start
    
    print(f'\r countmax={countmax} for {reccollatz} in {tmax:.3f} seconds. Time elapsed {time()-start:.3f}. Checking {n}',end='',flush=False)

    count=0
    n=n-1
print(f' collatz longest chain is {countmax} elements long for starting point {reccollatz} computed in {tmax} seconds')
'''
