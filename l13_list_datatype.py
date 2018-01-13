
# usage of every kind of list (array) type and work with some operators and functions

spam = ["cat", "bat", "rat", "elephant"];
print(spam);
print(spam[0]);
print(spam[-1]);    # index: -1 means the last item in the list
print(spam[-2]);    # index: -2 means the 2nd last item in the list
print(spam[1:3]);   # get list items from index of range [1, 3) to a list

spam[1] = 30;       # set value to index 1 item of the list (without caring of array/list type)
print(spam);

spam[1:3] = [20, 30, 40];   # replace list items of index range [1, 3) and insert 40 to the list after index 2
print(spam);

spam[2:3] = ["A", "B", "c"];# replace list items of index 2 to 3 and insert item "c" to index 4
print(spam);

print("RESET spam list");
spam = ["cat", "bat", "rat", "elephant"];
print(spam[:2]);    # get list items from index range [0, 2)
print(spam[1:]);    # get list items starting from index 1

del spam[-1];
print(spam);

print(len("Hello"));# length of a string
print(len(spam));   # length of an array/list

print([1,2,3] + [4,5,6]);   # array/list concatenation with "+" operator

print("Hello" *3);  # string concatenation with "*" operator
print([1,2,3] *3);  # array/list concatenation with "*" operator

print(list("Hello"));   # make the string into a char array/list (list(): int type is not allowed, only for string type)
print("cat" in spam);   # use "in" keyword to check if "cat" string is contained inside of an array/list
print("howdy" in spam);
print("howdy" not in spam); # use "not in" keyword to check if "howdy" string is contained inside of an array/list

"""output:
['cat', 'bat', 'rat', 'elephant']          # spam
cat                                        # spam[0]
elephant                                   # spam[-1]
rat                                        # spam[-2]
['bat', 'rat']                             # spam[1:3]
['cat', 30, 'rat', 'elephant']             # spam[1] = 30;
['cat', 20, 30, 40, 'elephant']            # spam[1:3] = [20, 30, 40];
['cat', 20, 'A', 'B', 'c', 40, 'elephant'] # spam[2:3] = ["A", "B", "c"];
RESET spam list
['cat', 'bat']                             # spam[:2]
['bat', 'rat', 'elephant'                  # spam[1:]
['cat', 'bat', 'rat']                      # del spam[-1]
5                                          # len("Hello")
3                                          # len(spam)
[1, 2, 3, 4, 5, 6]                         # [1,2,3] + [4,5,6]
HelloHelloHello                            # "Hello" *3
[1, 2, 3, 1, 2, 3, 1, 2, 3]                # [1,2,3] *3
['H', 'e', 'l', 'l', 'o']                  # list("Hello")
True                                       # "cat" in spam
False                                      # "howdy" in spam
True                                       # "howdy" not in spam
"""


# list in a list - nested list (array)
"""
spam = [["cat", "bat"], [10, 20, 30, 40, 50]];
print(spam);
print(spam[0]);
print(spam[0][1]);
"""
"""output:
[['cat', 'bat'], [10, 20, 30, 40, 50]]
['cat', 'bat']
bat
"""


