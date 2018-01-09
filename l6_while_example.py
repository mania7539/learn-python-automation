
# while loop
"""
spam = 0;
while spam < 5:
    print("Hello world!");
    spam = spam + 1;
"""
"""output: Hello world! Hello world! Hello world! Hello world! Hello world!""" 


# infinite loop
"""
while True:
    print("Hello world!");

"""
"""output: Hello world! Hello world! Hello world! ..."""


# check input forever with while loop
"""
name = "";
while True:
    print("Please type in your name: ");
    name = input();
    if name == "your name":
        break;
print("Thank you!");

"""


# while loop with continue

spam = 0;
while spam < 5:
    spam = spam + 1;
    if spam == 3:
        continue;
    print("spam is " + str(spam));

"""output: 1 2 4 5"""    
    
