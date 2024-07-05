# Day One - Basic Data Types and Structures

## Intro
So today I will be learning the basic data types in Python.  
I assume you already know the concept of programming and you have some basic to intermediate knowledge of python.  
In case you don't, here's a [link](https://www.youtube.com/watch?v=tyv4IcqG2OA "What is Programmming by blondiebytes") to a Youtube Video explaining the concept of programming and another [link](https://www.youtube.com/watch?v=kqtD5dpn9C8 "Learn Python in 1 hour") explaining the basic concepts of python.  
So consider the first three days a warm up.


## Basic Data Types
- Integers, floats, and complex numbers
- Strings and string manipulation
- Booleans
- None type


### What are data types?
Well we know data is unused information or information without meaning.
So data types in programming are the various forms of data that determing how the programming language manipulates it to give information.  
The various data types are assigned to varaibles, this is like a box with a label on it to make retrieval or manipulation of that data easier.  
Let's say we wanted to perform a calculation using the value of Pi to it's 60th place.  
It won't make sense to type all sixty digits every time we want to add or substract from it,  
so we can store that data into a variable named `Pi` and whenever we want to subtract a number from it, we can just go: `Pi - 2`.  
So below are the data types used in Python.


### Intergers
These are whole numbers basically. Can be either negative or positive e.g 1, -3, 400, 0, -32 etc.


### Floats
Floats are numbers with decimal points. e.g 2.5, -4.0, 3.142, 99.99 etc.


### Complex numbers
Python can also handle complex numbers using a functoin in the cmath library called `complex`.


### Strings and string manipulatons
Strings are basically texts (alphabets, numbers and even symbols) so how do you differentiate between a string of numbers and an actual number?  
well strings must be wrapped in quotes, either a single quote like `'string'` or double quote like `"string"` or back-ticks like ``string``.


### Booleans
Booleans are use in programming conditions. We have two types of Booleans which are `True` and `False`.


### None type
This is kind of confusing but None type (with Python syntax as `None`) represents nothing. It is different from `null` which represents emptiness.  
For example lets say we have a box, if that box where to have 2 items in it we'd say the number of contents in the box is 2,  
if there wher no items we'd  would assign `null` to that box. But if there was no box to begin with then that is `None`.  
Its a very abstract concept but I will show you its application.


### Challenge
- Play around with all the data types listed


## Data Structures
- List
- Tuples
- Sets
- Dictionaries


### What are data structures?
Data structures are the various way which we group or store our data. It helps us in manipulating (iterate, map, slice, etc.) our data and it also makes retrieval easy.


### Lists
Lists are used to store items using square brackets `[]` seperated with commas `,`. For example
```python
planets = ['Earth', 'Mars', 'Jupiter', 'Venus']
```
Lists items can be accessed using the square brackets and the index number of the list (starting from zero). For example typing
```python
planets[2]
```
Retruns `Jupiter`. List can contain any data type, even other data structures.


### Tuples
Tuples are immutable lists (you can't re-assign a tuple) they are also stored in curved braces `()` and are seperated with a comma.  
Tuples can contain any data type even other data structures.


### Sets
Set is a data type which is immutable (items cannot be re-assigned but you can add and remove items),  
unordered (They can appear in different order anytime you use them, and they do not have indexes or keys for retrieval), and they do not allow duplicate values.  
Sets use curly braces `{}` to store items. For example  
```python
fruits = {"apple", "orange", "banana"}
```
Sets can contain any data type even other data structures.


### Dictionaries
Just like the  normal dictionaries we have were you look for a word and find its defination, python dictionaries apply the same concepts.  
It uses keys-value plairs where you need the use a key (word) to access a value (definition) attached to it. Dictionaries use the format  
`{key:value}`, the value can be any data type even other data structures. For example  
```python
my_car = {"brand" : "Ford", "model" : "mustang", "year": 1964}
```


### Challenge
- Create and manipulate different data types
- Implement common operations on data structures
