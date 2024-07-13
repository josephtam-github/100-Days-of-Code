# Day 6: Context Managers in Python

## Intro
For day 6 of my #100DaysOfCode challenge, I will be focusing on Context Managers.

## What are context managers?

Context managers in Python provide a clean and efficient way to manage resources, ensuring proper acquisition and release of resources like file handles, network connections, or locks. They help in writing cleaner, more readable, and error-resistant code.

## Key Concepts

### 1. The `with` Statement

The `with` statement is the primary way to use context managers in Python.

```python
with open('file.txt', 'r') as file:
    content = file.read()
```

Explanation: This code opens a file, reads its content, and automatically closes the file when the block is exited, even if an exception occurs.

### 2. How Context Managers Work

Context managers implement two methods:
- `__enter__()`: Called when entering the `with` block
- `__exit__()`: Called when exiting the `with` block

### 3. Creating Custom Context Managers

#### Using a Class

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        return False  # Propagate exceptions
```

#### Using the `contextlib` Module

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    yield
    print("Exiting the context")
```

### 4. Multiple Context Managers

You can use multiple context managers in a single `with` statement:

```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
```

### 5. Exception Handling in Context Managers

Context managers can handle exceptions that occur within the `with` block:

```python
class DatabaseConnection:
    def __enter__(self):
        # Connect to the database
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection
        if exc_type is not None:
            # Handle the exception (e.g., rollback transaction)
        return False  # Propagate the exception
```

## Benefits of Context Managers

1. Automatic resource management
2. Cleaner, more readable code
3. Better error handling
4. Reduced boilerplate code

## Practice Exercises

1. Create a custom context manager for a simple database connection simulation.

## Additional Resources

- Python's official documentation on context managers: [With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
