"Find the sum of all the primes below two million."
from q5 import isprime
sumprime(N):
sum=0
for i in range(2,2000000):
    if isprime(i):
        sum+=i
print(f'sum: ')