'''
Finding paths in an NxN grid from start (0,0) to end (19,19) where only right and down movement is allowed.
Solved it using combinatorics. Number of paths will be 2N choose N where N is grid dimension. 
I tried this approach after some digging around, when when the naive recursion(code added as a comment towards the end) was exponential in time complexity O(4^N) with grid size N.... it was hilarious to see the results!'''
def factorial(N):
    if N==1:
        return 1
    elif N>1:
        return N*factorial(N-1)


def countpath(N):#N is grid dimension of a square grid
    #number of paths in a grid of NxN will be 2N choose N
    paths=factorial(2*N)/(factorial(N))**2#formula for 2N choose N
    return int(paths)

print countpath(20)

#below are the results of independent test runs
'''
refined:

for square grid of 10x10 dimesion number of paths from start (0,0) to(9,9) are 184756 found in 0.0 seconds
for square grid of 11x11 dimesion number of paths from start (0,0) to(10,10) are 705432 found in 0.0 seconds
for square grid of 12x12 dimesion number of paths from start (0,0) to(11,11) are 2704156 found in 0.0 seconds
for square grid of 13x13 dimesion number of paths from start (0,0) to(12,12) are 10400600 found in 0.0 seconds
for square grid of 14x14 dimesion number of paths from start (0,0) to(13,13) are 40116600 found in 0.0 seconds
for square grid of 15x15 dimesion number of paths from start (0,0) to(14,14) are 155117520 found in 0.0 seconds
for square grid of 16x16 dimesion number of paths from start (0,0) to(15,15) are 601080390 found in 0.0 seconds
for square grid of 17x17 dimesion number of paths from start (0,0) to(16,16) are 2333606220 found in 0.0 seconds
for square grid of 18x18 dimesion number of paths from start (0,0) to(17,17) are 9075135300 found in 0.0 seconds
for square grid of 19x19 dimesion number of paths from start (0,0) to(18,18) are 35345263800 found in 0.0 seconds
for square grid of 20x20 dimesion number of paths from start (0,0) to(19,19) are 137846528820 found in 0.0009996891021728516 
seconds
'''
'''
#Naive:(output given after code snippet)


def countpath(x=int(),y=int(),N=int()):
    if x<N and y <N:
        return countpath(x+1,y,N)+countpath(x,y+1,N)
    elif x==N or y==N or (x==N and y==N):
        return 1
from time import time
for i in range(10,21):
    start=time()
    print(f'for square grid of {i}x{i} dimesion number of paths from start (0,0) to({i-1},{i-1}) are {countpath(0,0,i)} found in {time()-start} seconds')



#Output:


for square grid of 10x10 dimesion number of paths from start (0,0) to(9,9) are 184756 found in 0.08 seconds
for square grid of 11x11 dimesion number of paths from start (0,0) to(10,10) are 705432 found in 0.29 seconds
for square grid of 12x12 dimesion number of paths from start (0,0) to(11,11) are 2704156 found in 1.12 seconds
for square grid of 13x13 dimesion number of paths from start (0,0) to(12,12) are 10400600 found in 4.09 seconds
for square grid of 14x14 dimesion number of paths from start (0,0) to(13,13) are 40116600 found in 15.70 seconds
for square grid of 15x15 dimesion number of paths from start (0,0) to(14,14) are 155117520 found in 60.16 seconds
for square grid of 16x16 dimesion number of paths from start (0,0) to(15,15) are 601080390 found in 246.97 seconds
for square grid of 17x17 dimesion number of paths from start (0,0) to(16,16) are 2333606220 found in 959.92 seconds
Traceback (most recent call last): keyboard interrupt'''
