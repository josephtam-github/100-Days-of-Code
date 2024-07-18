#!/usr/bin/python

"""
Prime Generator

Solution to day 8 challenge: Design a generator that produces 
prime numbers up to a given limit.
"""

from typing import Iterator

def prime_generator(limit: int = 10)-> Iterator[int]:
    """Generates prime numbers up to a given limit
    
    Keyword arguments
    limit -- the number of prime numbers to generate (default 10)
    """
    try:
        int(limit)
        if limit < 0:
            print("Please enter a positive number")
        else:
            n = 0
            count = 0
        while True:
            if n % 2 != 0:
                yield n
                count += 1
                if count >= limit:
                    break
            n += 1
    except ValueError:
        print("Error: Input must be a number")


def main():
    primes = prime_generator(5)
    print(next(primes))
    print(next(primes))
    print(next(primes))
    print(next(primes))
    print(next(primes))


if __name__ == "__main__":
    main()
