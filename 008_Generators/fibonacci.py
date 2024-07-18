#!/bin/usr/python3

"""
This file is the solution to day 8 of my #100DaysOfCode challenge

Create a generator that yields Fibonacci numbers. 
"""

from typing import Iterator, List

def fibonacci(iterations: int) -> Iterator[int]:
    """
    This function creates a generator for fibonacci numbers

    param:
        iterations: This is the number of fibonacci values the function
        should generate

    return: Return an iteration of the fibonacci sequence
    """

    n = 0
    previous_num = 0
    current_num = 1
    
    try:
        int(iterations)
        if iterations < 0:
            print("Please enter a number greater than 0")
        else:
            while n < (iterations):
                temp = current_num
                current_num += previous_num
                previous_num = temp
                if n == 0:
                    current_num = 0
                else:
                    current_num = current_num
                yield current_num
                n += 1
    except ValueError:
        print("Error: Input must be an integer")
 

def main():
    for numbers in fibonacci('8'):
        print(numbers)


if __name__ == "__main__":
    main()
