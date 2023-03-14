# Sieve of Eratosthenes - base verison - O( n log log n)

def countPrimes(n):
    prime = [True] * (n+1)
    p = 2
    while p*p <=n: # p <= sqrt(n) bt this way is faster
        if prime[p] == True:
            for i in range (p*p, n+1, p):
                prime[i] = False
            p += 1

    
    primes = []
    for p in range (2, n):
        if prime[p]:
            primes.append(p)
    return len(primes)

"""
The time complexity of this algorithm comes from the fact 
that it needs to iterate over all numbers from 2 to n, 
and for each prime number p, it needs to remove all multiples of p from the list. 
The number of multiples of p that are less than or equal to n is n/p, 
so the total time complexity of the algorithm is the sum of n/p for all prime numbers p less than or equal to n.
This sum can be approximated as n * (1/2 + 1/3 + 1/5 + 1/7 + ...), which is equivalent to n * log log n. 
Therefore, the time complexity of the Sieve of Eratosthene is O(n log log n)
"""
""""""


