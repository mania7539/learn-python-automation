
# A variable can't be both local and global
# Scope is a container of variables:
#   A local variable CANNOT be used in global scope
#   A global variable CAN be used in local scope, if there's no variable assignment with the same name
#   Different functions CANNOT use variables inside each others.
"""
spam = 42;      # global variable
                # A global scope is created when the program starts
                #   and destroyed when the program terminates.
def eggs():
    spam = 33;  # local variable
    print("spam: " + str(spam));
                        # A local scope is created whenever a function is called
                        #   and all the variables just assigned during the function call exists
                        #   within that local scope.
                        #   When the function returns, the local scope is destroyed
                        #   and these variables in local scope are forgotten.
eggs();
print("spam: " + str(spam));
"""
"""output:
spam: 33
spam: 42

"""


# A global variable CAN be used in local scope, if there's no variable assignment with the same name
"""
spam = 55;      
def eggs():
    print("spam: " + str(spam));
                        
eggs();
print("spam: " + str(spam));
"""
"""output:
spam: 55
spam: 55

"""


# use 'global' or 'nonlocal' keyword to mark variable to global scope in function
#   we can only used it to distinguish if we want to use global than local scope
# 'nonlocal' keyword can only be used when a local variable is assigned and we want to used it in its nested function
"""
def spam():
    # global eggs;
    eggs = "Hello";
    print(eggs);

eggs = 42;
spam();
print(eggs);
"""
"""output with global eggs:
Hello
Hello
"""

"""output with # global eggs:
42
Hello
"""


# global must be used in the head lines of function
#   so we can can't choose to use both local and global scope with the same variable name
"""
def spam():
    eggs = 55;
    print(eggs);
    global eggs;
    eggs = "Hello";
    print(eggs);

eggs = 42;
spam();
print(eggs);
"""
"""output: ERROR windows: name 'eggs' is used prior to global declaration."""



# 'nonlocal' keyword can only be used when a local variable is assigned and we want to used it in its nested function

def f():
    x = 42; # take out this line will get ERROR: no binding for nonlocal 'x' found => feature of 'nonlocal'
    def g():
        nonlocal x;
        x = 55;
    print("Before calling g: " + str(x));
    print("Now calling g...");
    g();
    print("After calling g: " + str(x));
    
x = 3;
f();
print("x in main: " + str(x));

"""output:
Before calling g: 42
Now calling g...
After calling g: 55
x in main: 3
"""
