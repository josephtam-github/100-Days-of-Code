# Day 2: Control Flow and Functions in Python

## Intro
For Day 2 of my __#100DaysofCode__ focuses on two fundamental concepts: Control Flow and Functions. These concepts are crucial for writing structured, efficient, and reusable code.

## What is Control Flow?

Control flow refers to the order in which individual statements, instructions, or function calls are executed in a program. Python provides several control flow statements:

### Conditional Statements
- `if` statement: Executes a block of code if a specified condition is true.
- `elif` statement: Checks additional conditions if the previous `if` or `elif` conditions were false.
- `else` statement: Executes when all previous conditions are false.

### Loops
- `for` loop: Iterates over a sequence (list, tuple, string, etc.) or other iterable objects.
- `while` loop: Repeats a block of code as long as a condition is true.

### Control Statements
- `break`: Exits the current loop prematurely.
- `continue`: Skips the rest of the current loop iteration and continues with the next iteration.
- `pass`: Does nothing. It's used as a placeholder where syntactically some code is required.

## What are Functions?

Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing redundancy.

### Defining and Calling Functions
We define a function using the `def` keyword. For example

```python
def function_name(parameters):
    # function code
    return result

# Calling the function
result = function_name(arguments)
```

### Parameters and Arguments
Parameters are variables listed in the function definition.
Arguments are the actual values passed to the function when calling it.

### Return Values
We use the `return` statement to send values back from a function.

### Default Arguments
Setting default values for function parameters allows use to call the function without providing any argument. For example

``` python
def greet(name="World"):
    print(f"Hello, {name}!")
```
### Variable-length Arguments
`*args`: Allowing a function to accept any number of positional arguments. `**kwargs`: Allowing a function to accept any number of keyword arguments.
For example
```python
def function(*args, **kwargs):
    # args is a tuple of positional arguments
    # kwargs is a dictionary of keyword arguments
```

### Local vs Global variables
Local variables are only accessible within their function while global variables are accessible throughout the program.

## Challenge
1. Write a function that uses a `for` loop to print the first n numbers of the Fibonacci sequence.
2. Create a function that uses conditional statements to classify a given number as positive, negative, or zero.
3. Implement a simple calculator function that takes two numbers and an operator as arguments.
4. Write a function with default arguments that calculates the area of a rectangle.

