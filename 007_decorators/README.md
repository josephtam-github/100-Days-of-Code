# Day 7: Decorators in Python

## Intro
Day 7 of my __#100DaysofCode__ focuses on python Decorators.

## What is Decoration?

Decoration is a way of modifying functions using other functions. We use decorators to extend the functionality of other functions without altering it's code.

### Example
```python
def decor(func):
	print("=====")
	func()
	print("=====")

def print_text():
	print("Hello World")

>>>
>>> decor(print_text())
>>> =====Hello World=====
```

### The Pie Syntax for Decorators
We can use the same decoration anytime in our source code, with different functions by putting `@` symbol and the decorator name before defining another function this is called Pie Syntax. In our example above tis would take away the need for the `decor(print_text())` statement saving us a line of code.

### Example with Pie Syntax
```python
def decor(func):
	print("=====")
	func()
	print("=====")
@decor
def print_text():
	print("Hello World")

>>> =====Hello World=====
```

## Challenge
1. Create a decorator that will retry a function a specified number of times if it raises an exception.
