
# Import modules before you can use them
#
# Generate random number between 1 and 10
#   Use "random." at front to tell python to look inside that module for the function
#   since "randint()" is not a builtin function, it only exist inside the random module
"""
import random;

num = random.randint(1, 10);
print(num);

"""
"""output: 2, 10, 8, ..."""


# We can import multiple modules in a single line by separate module names with ","
"""
import random, sys, os, math;
"""


# Since we import everything (*) in random, so it now performs like alias.
#   We can ignore the "random." for later coding
"""
from random import *
num = randint(1, 10);
print(num);
"""
"""output: 2, 10, 8, ..."""


# Use sys.exit() to terminate a python program immediately
"""
import sys;
print("Hello");
sys.exit();
print("Goodbye");
"""
"""output: Hello (Console exits so "Goodbye" not printed)"""


# Using pyperclip module
# pip install pyperclip

import pyperclip;
pyperclip.copy("Hello world!");
pyperclip.paste();


"""output: Hello world! (in your clipboard, so you can paste with CTRl+v"""





