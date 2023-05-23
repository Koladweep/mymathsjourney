import math

def pollard_rho(n):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def pollard_rho_factor(n):
        x = 2
        y = 2
        d = 1
        f = lambda x: (x**2 + 1) % n

        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)

        return d

    if n % 2 == 0:
        return 2

    while True:
        factor = pollard_rho_factor(n)
        if factor == n:
            return factor
        n //= factor

def largest_prime_factor(num):
    factor = pollard_rho(num)
    while factor != num:
        num //= factor
        factor = pollard_rho(num)
    return num

target_num = 600851475143
largest_factor = largest_prime_factor(target_num)
print(largest_factor)
