#!/usr/bin/env python3

from datetime import datetime

def sieve_of_eratosthenes(count):
    if count < 2:
        return [False] * (count + 1)
    else:
        values = [True] * (count + 1)
        values[0] = values[1] = False
        upper = int(count ** 0.5) + 1 
        for i in range(2, upper):
            if values[i]:
                s = slice(i*i, count + 1, i)
                x = (count - i*i + i) // i
                values[s] = [False] * x
                #for j in range(i * i, count + 1, i):
                #    values[j] = False
        return values

def prime_count(count):
    primes = [i for (i, v) in enumerate(sieve_of_eratosthenes(count)) if v]
    # print(primes)
    return len(primes)

if __name__ == '__main__':
    for i in (10, 100, 1000, 10000, 100000, 1000*1000, 10*1000*1000, 100*1000*1000):
        start = datetime.now()
        x = prime_count(i)
        end = datetime.now()
        print(f"{i}/{x}: {end - start}")
