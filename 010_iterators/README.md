# Day 10: Iterators in Python

## Intro

For day 10 of my __#100DaysOfCode__ Challenge I will be talking about iterators, a fundamental concept in Python that allows for efficient and pythonic traversal of collections and other iterable objects.

## What are Iterators?

An iterator is an object that represents a stream of data. It implements two methods:

1. `__iter__()`: Returns the iterator object itself.
2. `__next__()`: Returns the next value in the iteration.

Iterators are the mechanism behind for loops and many other Python features.

## Key Concepts

### 1. Basic Iterator Protocol

```python
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        raise StopIteration

# Usage
for item in SimpleIterator(5):
    print(item)  # Outputs: 1, 2, 3, 4, 5
```

### 2. Built-in Iterators

Python provides many built-in objects that are iterators:

- `iter()` function: Converts an iterable into an iterator
- File objects: Iterate over lines in a file
- `enumerate()`: Iterate with index and value pairs
- `zip()`: Iterate over multiple iterables in parallel

### 3. Infinite Iterators

Iterators can represent infinite sequences:

```python
from itertools import count

for i in count(start=1):
    print(i)  # Prints numbers indefinitely, starting from 1
    if i == 5:
        break
```

### 4. Iterator vs Iterable

- Iterable: An object capable of returning its members one at a time (e.g., lists, strings)
- Iterator: The object that actually performs the iteration

```python
my_list = [1, 2, 3]  # Iterable
my_iterator = iter(my_list)  # Iterator
```

### 5. Custom Iterators

You can create custom iterators for your own objects:

```python
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Usage
for char in Reverse("hello"):
    print(char)  # Outputs: o, l, l, e, h
```

## Benefits of Iterators

1. Memory Efficiency: Process one item at a time instead of loading entire collection
2. Simplicity: Provide a uniform interface for traversing different data structures
3. Lazy Evaluation: Generate values on-demand

## Practice Exercises

1. Create an iterator that generates prime numbers up to a specified limit

## Additional Resources

- Python Documentation on Iterators: [Link](https://docs.python.org/3/tutorial/classes.html#iterators)
- Real Python's Guide to Iterators: [Link](https://realpython.com/python-iterators-iterables/)
- PEP 234 – Iterators: [Link](https://www.python.org/dev/peps/pep-0234/)
