'''10001st prime
Toggle Pin=7

 Show HTML problem content 
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''
#import prime finder 
from sys import path
path.append(r'C:\Users\Das\Documents\python playground\project euler')
from q5 import isprime
count=0#to count the serial index of prime number series
i=0
Plist=[]
flag=False
num=0
while len(Plist)!=10001:
    if isprime(num):
        Plist.append(num)
    num+=1

def isprimeverify(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(Plist[10000])