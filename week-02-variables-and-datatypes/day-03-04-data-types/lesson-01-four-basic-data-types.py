# PCEP Training
# Week 2 - Variables and Data Types

# Date: Monday, Sept 29, 2025

# Lesson: Day 3-4: Python's Four Basic Data Types

# ******************************************************

"""
Every piece of data in Python has a type. Think of data types as different categories of information, each with its own rules and capabilities.
"""

# 1. Integers (int) - Whole Numbers -- Integers are whole numbers with no decimal points:

# Creating integer variables
age = 25
year = 2025
temp = -10
large_number = 100000
zero = 0

print("Use a Print statement for call the one of the integer variables")
print()                  # empty space for readability 
print(age)               # Calls the 'age' variable, then the print function outputs it's assigned value, which is '25'
print(type(age))         # Output: <class 'int'>. The type() function in Python returns the data type (class) of a value or variable.

# ******************************************************

# 2. Floats (float) - Decimal Numbers -- Floats are numbers with decimal points:

# Creating float variables
price = 19.99
height = 5.75
pi = 3.14159
negative_decimal = -2.5
whole_as_float = 10.0  # Still a float because of the decimal

print(price)         # Output: 19.99
print(type(price))   # Output: <class 'float'>

"""
Some exmaples of float data types include:
3.14
99.99
0.5
-12.34

Any number with a decimal point
"""

# ******************************************************

# 3. Strings (str) - Text Data -- Strings are text, always enclosed in quotes:

#  Creating string variables
first_name = "John"          # Double quotes
last_name = 'Smith'              # Single quotes
message = "Hello World"
empty_string = " "             # Empty string

print(first_name)              # Output: John
print(type(first_name))        # Output: <class 'str'>

"""
String rules:

Must be enclosed in quotes (single ' or double ")
Can contain letters, numbers, spaces, symbols
Can be empty: ""
"""

# ******************************************************
print()

# 4. Booleans (bool) - True/False Values -- Booleans represent truth values - either 'True' or 'False':

# Creating boolean variables
is_student = True
is_raining = False
has_license = True
is_finished = False

print(is_student)
print(type(is_student))

"""
Boolean rules:

Only two possible values: True or False
Must be capitalized exactly like that
No quotes needed (quotes would make them strings)
"""

# ******************************************************
print()

# Using the type() Function -- The 'type()' function tells you what data type something is:

# Checking the 'type()' for different values
print(type(42))                        # <class 'int'>
print(type(3.42))                      # <class 'float'>
print(type("Learning Python"))         # <class 'str'>
print(type(True))                      # <class 'bool'>
print()

# Checking the 'type' for different variables
name = "Alice"
age = 30
height = 5.6
is_adult = True

print(type(name))                     # <class 'str'>
print(type(age))                      # <class 'int'>
print(type(height))                   # <class 'float'>
print(type(is_adult))                 # <class 'bool'>



