
# hello function
"""
def hello():
    print("Howdy!");
    print("Howdy!!!");
    print("Hello there.");

hello();
hello();
hello();
"""
"""output: Howdy!\n Howdy!!!\n Hello there.\n (*3)"""


# hello function with parameter
"""
def hello(name):
    print("Hello " + name);

hello("Alice");
hello("Bob");
"""
"""output: Hello Alice\n Hello Bob"""


# return value of function
"""
def plusOne(number):
    return number + 1;

newNumber = plusOne(5);
print(newNumber);
"""
"""output:6 """


# Introduce 'None' value
# Every function has a return value in python
#  and the default return value is 'None'
"""
spam = print();         # print function returns None, see below proof
print(spam == None);    #output: True
print(_spam);           #output: NameError: name '_spam' is not defined

"""


# Use keyword argument (optional argument) feature of python function

print("Hello");
print("World");

print("Hello", end=""); # won't print \n which is used in default
print("World");

print("cat", "dog", "mouse");            # print formatted strings and separate them with " " 
print("cat", "dog", "mouse", sep="ABC"); # change the default separator " " to "ABC"

"""output:
Hello
World
HelloWorld
cat dog mouse
catABCdogABCmouse
"""


