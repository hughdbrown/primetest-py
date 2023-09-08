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
                s = slice(i*i, count, i)
                x = (count - i*i + i - 1) // i
                values[s] = [False] * x
        return values

def prime_count(count):
    prime_mask = sieve_of_eratosthenes(count)
    return sum(prime_mask)

if __name__ == '__main__':
    for i in (10, 100, 1000, 10000, 100000, 1000*1000, 10*1000*1000, 100*1000*1000):
        start = datetime.now()
        prime_count(i)
        end = datetime.now()
        print(f"{i}: {end - start}")
