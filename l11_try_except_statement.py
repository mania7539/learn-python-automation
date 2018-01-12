
# kind of function will cause exception
"""
def div42by(num):
    return 42 / num;

print(div42by(2));
print(div42by(12));
print(div42by(0));  # this line cause 'ZeroDivisionError' exception and return 'None' value
print(div42by(1));
"""
"""output:

21.0
3.5
Traceback (most recent call last):
  File "D:/git/python/learn-python-automation/l11_try_except_statement.py", line 9, in <module>
    print(div42by(0));  # this line cause
  File "D:/git/python/learn-python-automation/l11_try_except_statement.py", line 5, in div42by
    return 42 / num;
ZeroDivisionError: division by zero

"""


# try and exception version of the function
"""
def div42by(num):
    try:
        return 42 / num;
    except ZeroDivisionError:
        print("Error: You tried to divide by zero.");
    except:
        print("Error: You got an exception.");
        # this except without specific exception type will catch all type of exception
        
print(div42by(2));
print(div42by(12));
print(div42by(0));  # this line cause 'ZeroDivisionError' exception and return 'None' value
print(div42by(1));
"""
"""output:
21.0
3.5
Error: You tried to divide by zero.
None
42.0

"""


# exception in Input Validation scenario
"""
print("How many cats do you have?");
numCats = input();
if int(numCats) >= 4:
    print("That is a lot of cats.");
else:
    print("That is not that many cats.");
"""
"""
intput: 0
output: That is not that many cats.
"""

"""
intput: six
output:
Traceback (most recent call last):
  File "D:/git/python/learn-python-automation/l11_try_except_statement.py", line 56, in <module>
    if int(numCats) >= 4:
ValueError: invalid literal for int() with base 10: 'six'

"""


# use try and except in Input Validation scenario
try:
    print("How many cats do you have?");
    numCats = input();
    if int(numCats) >= 4:
        print("That is a lot of cats.");
    else:
        print("That is not that many cats.");
except ValueError:
    print("You didn't enter a number.");
"""
intput: 0
output: That is not that many cats.
"""

"""
intput: six
output: You didn't enter a number.
"""

