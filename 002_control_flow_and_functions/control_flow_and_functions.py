#!bin/usr/python3

"""Write a function that uses a `for` loop
to print the first n numbers of the Fibonacci sequence.
"""


def fibonacci(n):
    """Prints the first n numbers of the Fibonacci sequence
    using a for loop."""
    if n <= 0:
        print("n must be positive number")
        return

    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Test the function
fibonacci(8)


"""Create a function that uses conditional statements
to classify a given number as positive, negative, or zero.
"""


def number_classifier(number):
    """Classifies a given number as positive, negative, or zero."""

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


# Test the function
number_classifier(5)
number_classifier(-2)
number_classifier(0)


"""Implement a simple calculator function that takes
two numbers and an operator as arguments.
"""


def calculator(num1, num2, operator):
    """Performs a simple calculation based on the provided operator."""

    operators = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b, "*": lambda a, b: a * b,
                "/": lambda a, b: a / b
                }

    if operator not in operators:
        print("Invalid operator. Please use +, -, *, or /.")
        return

        try:
            result = operators[operator](num1, num2)
            print(f"The result of {num1} {operator} {num2}\
                    is: {result}")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")


# Test the function
calculator(10, 5, "+")


"""Write a function with default arguments
that calculates the area of a rectangle.
"""


def rectangle_area(length=1, width=1):
    """Calculates the area of a rectangle with optional
    length and width arguments."""

    return length * width


# Test the function
rectangle_area()  # Uses default arguments
rectangle_area(5, 3)  # Specifying length and width
