# Day 8: Generators in Python

## Intro

For Day 8 of my *#100DaysOfCode* Challenge we focus on generators, a powerful feature in Python for creating iterators. Generators allow you to declare a function that behaves like an iterator, providing a more memory-efficient way to work with sequences of data.

## What are Generators?

Generators are functions that return an iterator. They use the `yield` keyword to produce a series of values over time, rather than computing them all at once and storing them in memory.

## Key Concepts

### 1. Basic Generator Function

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)  # Outputs: 5, 4, 3, 2, 1
```

Explanation: This generator yields numbers in a countdown sequence.

### 2. Generator Expressions

Generator expressions are similar to list comprehensions, but use parentheses instead of square brackets:

```python
squares = (x**2 for x in range(10))
```

### 3. Infinite Generators

Generators can create infinite sequences without storing them in memory:

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

### 4. Sending Values to Generators

Generators can receive values using the `send()` method:

```python
def echo_generator():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")  # Prints: Received: Hello
```

### 5. Generator Methods

- `next()`: Retrieves the next value from the generator
- `send()`: Sends a value to the generator
- `throw()`: Raises an exception inside the generator
- `close()`: Closes the generator

## Benefits of Generators

1. Memory Efficiency: Only one item is produced at a time.
2. Lazy Evaluation: Values are computed on-demand.
3. Represent Infinite Sequences: Can model streams of data.
4. Composability: Can be easily piped together.

## Practice Exercises

1. Create a generator that yields Fibonacci numbers.
3. Design a generator that produces prime numbers up to a given limit.

## Additional Resources

- Python Documentation on Generators: [Link](https://docs.python.org/3/tutorial/classes.html#generators)
- Real Python's Guide to Generators: [Link](https://realpython.com/introduction-to-python-generators/)
- PEP 255 – Simple Generators: [Link](https://www.python.org/dev/peps/pep-0255/)
