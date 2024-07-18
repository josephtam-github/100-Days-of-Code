# Day 9: Advanced Object Oriented Project (OOP) in Python

## Intro
Day 9 of my __#100DaysofCode__ focuses on advanced features in object oriented programming.

## Advacnced Concepts

There are a lot of functional features in object oriented programming than just classes and there methods. I will be discussing some below and giving examples to buttress my point

### The  @property

Python programming provides us with a built-in `@property` decorator which makes usage of `getter` and `setters` much easier in Object-Oriented Programming.

#### Example
```python
class Square:
	def __init__(self, height=0, width=0):
		self.hieght = hieght
		self.width = width

@property
def hieght(self)
	print("retrieving hieght") #This code runs when the hieght property is initialized
	return self.__hieght #The double underscore makes the attribute/variable private

#The @attr.setter property is used to do checks on the value of an attribute during initialization
@hieght.setter
def hieght(self, value)
	if value.isdigit():
		self.__hieght = value
	else:
		print("Please enter a digit")
```

### Static methods
A static method in Python is a method that belongs to a class, not its instances. It does not require an instance of the class to be called, nor does it have access to an instance. Static methods in Python are declared using the  `@staticmethod` decorator. This decorator tells the Python interpreter that the method is static and should be called on the class, not on an instance of the class.

#### Example
```python
class MathUtils:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathUtils.factorial(n-1)

>>> print(MathUtils.factorial(5))

>>> 120
```

### Magic methods
Magic methods are predefined class methods that have different functionality when called on instances. They start and end with two underscores.


#### Example
Here's a table of Python magic methods and their actions:

| Magic Method | Action |
|--------------|--------|
| `__init__(self, ...)` | Constructor, initializes a new instance |
| `__del__(self)` | Destructor, called when an object is garbage collected |
| `__str__(self)` | Returns a string representation of the object |
| `__repr__(self)` | Returns a detailed string representation of the object |
| `__len__(self)` | Returns the length of the object |
| `__getitem__(self, key)` | Allows indexing of the object |
| `__setitem__(self, key, value)` | Allows setting values using indexing |
| `__iter__(self)` | Makes the object iterable |
| `__contains__(self, item)` | Implements the `in` operator |
| `__call__(self, ...)` | Makes the object callable like a function |
| `__add__(self, other)` | Implements addition (`+`) |
| `__sub__(self, other)` | Implements subtraction (`-`) |
| `__mul__(self, other)` | Implements multiplication (`*`) |
| `__truediv__(self, other)` | Implements true division (`/`) |
| `__floordiv__(self, other)` | Implements floor division (`//`) |
| `__mod__(self, other)` | Implements modulo operation (`%`) |
| `__pow__(self, other)` | Implements exponentiation (`**`) |
| `__eq__(self, other)` | Implements equality comparison (`==`) |
| `__ne__(self, other)` | Implements inequality comparison (`!=`) |
| `__lt__(self, other)` | Implements less than comparison (`<`) |
| `__le__(self, other)` | Implements less than or equal to comparison (`<=`) |
| `__gt__(self, other)` | Implements greater than comparison (`>`) |
| `__ge__(self, other)` | Implements greater than or equal to comparison (`>=`) |
| `__enter__(self)` | Enters a context manager |
| `__exit__(self, exc_type, exc_value, traceback)` | Exits a context manager |


## Challenge
Create a system to model a smart home with various devices. Implement the following:

1. An abstract base class SmartDevice with:

- Abstract methods: turn_on(), turn_off(), status()
- A class method to track the total number of devices


2. Two concrete classes inheriting from SmartDevice:

- SmartLight: Has brightness level and color
- SmartThermostat: Has temperature setting


3. A SmartHome class that:

- Can add and remove devices
- Implements a context manager protocol to power all devices on/off
- Uses a custom iterator to cycle through all devices


4. Implement property decorators for appropriate attributes
5. Use at least one dunder (magic) method in each class
6. Create a simple command-line interface to interact with the smart home system
