#Finds smallest trianle number with atleast n factors
class nfactortriangleceil:
    def __init__(self, divisors_target, primes):
        self.divisors_target = divisors_target
        self.primes = primes

    def get_divisors_count(self, n):
        count = 1
        i = 0
        while n > 1 and i < len(self.primes):
            exponent = 1
            while n % self.primes[i] == 0:
                exponent += 1
                n //= self.primes[i]
            count *= exponent
            i += 1
        return count

    def find_triangular_number(self):
        n = 1
        while True:
            triangular_number = (n * (n + 1)) // 2
            divisors_count = self.get_divisors_count(triangular_number)
            if divisors_count >= self.divisors_target:
                return triangular_number
            n += 1


# Example usage: Find the first triangular number with at least 500 divisors
primelist=[]
with open('primesunder70000.txt','r') as f:
    l=f.readline().rstrip('\n')
    while l!='':
        primelist.append(int(l))
        l=f.readline()
finder = TriangularNumberFinder(500, primelist)
triangular_number = finder.find_triangular_number()
print("The first triangular number with at least 500 divisors is:", triangular_number)
