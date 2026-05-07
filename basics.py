# Some Examples
spam = 1
text = '# This is a comment inside quotes'

# n  # try to access an undefined variable throws a NameError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined

# Data types
# 1. Numbers (int, float)
# 2. Strings (str)

# # Strings
# - Need special characters use \. Example print('line 1 \n line2')
# - Don't need special characters use r'' Example print(r'line 1 \n line2')
# - String literals can span multiple lines, use ''' or """. To avoid new lines use \ Example print(''' ABC\ DEF ''')
# - Strings can be indexed Example: text = 'abc' text[0] = a, 1 = b, 2 = c
# - Addition to indexing they can be sliced as well. Example text[0:2]
# - Strings are immutable in python Example: text[0] = 'V' throws error (TypeError)
# - Built in len() function returns length of the string Example len(text) => 3
# - Lots of built in string manipulation functions str.format(), str.lower() e.t.c.

# Data Structures
# 1. Lists
# 2. Tuples (immutable version of list)
# 3. Sets {unordered collection with no duplicate elements}
# 2. Dictionaries (stores items and each item has a key and a value)

# # Lists
# - Compound data structure Example list = ['a', 2, 3.8]
# - Lists are mutable Example list[0] = 5 works
# - Lists also support concatenation [1, 2, 3] + [4] = [1,2,3,4]
# - Lists in python supports push (append) and pop and many other functions
# - Lists as Stack: append(), pop()
# - Lists as Queues: from collections import deque; queue = deque(["E", "J", "M"]); queue.append("T"); queue.popleft()
# - List comprehension: A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# - Example of list comprehension: [x**2 for x in range(5) if x%2 != 0] => Easier and concise to read
# - Remove elements Example: del list[0]

# Control flow
# 1. if, else, else if, for, range, match (case statements)
# 1. Conditionals: and, or, not
# 2. functions Example: def function():
# 3. function annotations Example: def function(a: str, b: num)
# 4. Lambda expressions, short functions lambda a, b: a+b

# Coding Style (PEP 8)
# 1. Use 4-space indentation, and no tabs.
# 2. Wrap lines so that they don’t exceed 79 characters.
# 3. Use blank lines to separate functions and classes, and larger blocks of code inside functions.
# 4. When possible, put comments on a line of their own.
# 5. Use docstrings.
# 6. Use spaces around operators and after commas: a = f(1, 2) + g(3, 4).
# 7. Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument.

# Modules
# - Modules help to manager longer python programs by splitting them into files
# - Write couple of functions and save as .py and import them using import statement

# Standard Python Modules
# 1. sys module: Helps manage python modules. sys.path() sets default module path
# 2. dir() lists the functions available for that structure

# Packages
# - Packages in python follow a simple structure PackageName / __init__.py, module1.py, module2.py. import module1 from PackageName

# Inputs and Outputs
# - open() returns a file object. Example: f = open('abc.txt', 'w')
# - It's always better to use with keyword to open files as it facilitates automatic closing
# - Methods on file object, f.read(), f.readline(), f.write()
# - Working with files is always difficult as it returns everything as a string and we need to maintain conversions that is where json helps
# - import json; x=[1,2,3]; json.dumps(x), json.dump(x, f) => write to file; json.load(f)

# Errors and Exceptions
# - Exceptions can be handled using the except keyword. except ValueError:
# - Exceptions can be raised by using the raise keyword. raise ValueError
# - Users can create custom exceptions as well.

# Classes
# - Classes provide a way to bundle data and functionality together.
# - Classes have attributes that help to maintain state
# - Classes have methods to modify the state
# - Namespaces are nothing but where the object lives and it's lifetime
# - Class definition: class ClassName
# - class Abc: a=5 def __init__(self): def method1(self):
# - No concept of private variables but represented using __
# - There is a new concept that i am not aware of called dataclass. It is similar to typescript definition. from dataclasses import dataclass @dataclass class Emp: name:str

# Standard Library
# - import os => Interact with the operating system
# - import re => string pattern matching
# - import math
# - import urllib => for accessing the internet
# - import datetime
# - import timeit => to measure performance
# - import unittest
# - import logging => for flexible logging
