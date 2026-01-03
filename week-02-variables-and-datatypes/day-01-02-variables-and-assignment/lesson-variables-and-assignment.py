# PCEP Training
# Week 2 - Variables and Data Types

# Date: Friday, Sept 26, 2025

# Lesson: Day 1-2: Variables and Assignment

# ******************************************************

# Variables

print("What are Variables?")
print("Think of variables as labeled storage boxes in your computer's memory. Each box has a name (the variable name) and can hold one piece of information.")
print()

print("=======================================================")
print()

#Creating Variables examples
name = "Sarah"         # A box labeled "name" containing "Sarah"
age = 22               # A box labeled "age" containing 22
is_happy = True        # A box labeled "is_happy" containing True

# ******************************************************

# Assignments

# The Assignment Operator (=)
# The = symbol doesn't mean 'equals' like in math. It means 'assign' or 'store'.")

# Read this as: "assign the value 25 to the variable called: age"
age = 25

# Read this as: "assign the text 'Python' to the variable called language"
language = "Python"

# ******************************************************

# Create some variables
student_name = "Alex"
current_grade = 87
course_title = "Intro to Python"
is_enrolled = True       # boolean value: Is it on/off? True/False? - Be sure to use a capital T for True or capital F for False when assigning a boolean value

# Using the variables
print(student_name)      # Output: Alex
print(current_grade)     # Output: 87
print(course_title)      # Output: Introduction to Python
print(is_enrolled)       # Output: True

# Variable Naming Rules (IMPORTANT!) - These are VALID variables names
name = "John"           # Letters
first_name = "John"     # Letters and underscore
age2 = 25               # Letters and numbers
_private = "secret"     # Starting with underscore
studentCount = 30       # camelCase (though not preferred in Python)
MAXIMUM = 100           # All caps (usually for constants)

# These are INVALID variable names
"""
2name = "error"        # Can't start with a number
first-name = "error"   # Can't use hyphens
my name = "error"      # Can't have spaces
class = "error"        # Can't use Python keywords
print = "error"        # Don't overwrite built-in functions
"""

# ====================================================================================================

# Python Naming Conventions
# Python programmers follow specific naming styles:

# Variables and functions: use snake_case (lowercase with underscores)
first_name = "Maria"
total_score = 95
user_input = "hello world"

# Constants: use ALL_CAPS
MAX_ATTEMPTS = 3
PI = 3.14159
DEFAULT_MESSAGE = "Welcome!"

# ====================================================================================================

# Variables Are Case Sensitive
print()        # spacing

name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)    # Alice
print(Name)    # Bob  
print(NAME)    # Charlie
print()


# These are three completely different variables!

# ====================================================================================================

# Variable Reassignment

score = 85
print("Intial score: ", score)     # Output: 85, from the original assigned value

# Variable reassignment #1
score = 92
print("New score: ", score)        # Output: 92, the updated value of the variable "score" is updated from 85 to 92

# Variable reassignment #2
score = 95
print("Final score: ", score)      # Output: 95, the updated value of the variable "score" is updated from 92 to 95



