
# how to use range() function

for i in range(4):
    print(i);

print(range(4));        # range(4) == range(0,4)
print(range(0,4));      # range() will not return a list but a range type
print(list(range(0,4)));# use list() to make range(0,4) into a list/array
print([0,1,2,3]);       # [0,1,2,3] == range(4) == range(0,4)


print(list(range(0, 100, 2)));  # create a list with range [0, 100) by +2 for each item


# in general, use range(len(someList)) to iterate the for-loop

supplies = ["pens", "staplers", "flame-throwers", "binders"];
for i in range(len(supplies)):  
    print("Index " + str(i) + " in supplies is: " + supplies[i]);


# multiple assignment in python

cat = ["fat", "orange", "loud"];
size = cat[0];
color = cat[1];
disposition = cat[2];

print(size);
print(color);
print(disposition);

size, color, disposition = cat;
print(size);
print(color);
print(disposition);

size, color, disposition = "skinny", "black", "quiet";
print(size);
print(color);
print(disposition);


# in general, we use multiple assignment to swap variable values

a = "AAA";
b = "BBB";
print(a);
print(b);
a, b = b, a;    
print(a);
print(b);


# augmented assignment
spam = 42;
spam = spam + 1;   # +=1
spam += 15;        # +=15 => this kind of use is called "augmented assignment"
print(spam);       # +=, -=, *=, /=, %= they are all called "augmented assignment"


"""output:
0                                        # for-loop iteration with range(x)
1
2
3
range(0, 4)                              # range(4) == range(0,4), range() will not return a list but a range type
range(0, 4)
[0, 1, 2, 3]                             # use list() to make range(0,4) into a list/array
[0, 1, 2, 3]                             # [0,1,2,3] == range(4) == range(0,4)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98] # create a list with range [0, 100) by +2 for each item
Index 0 in supplies is: pens             # in general, use range(len(someList)) to iterate the for-loop
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
fat                                      # multiple assignment in python
orange
loud
fat
orange
loud
skinny
black
quiet
AAA                                      # in general, we use multiple assignment to swap variable values
BBB
BBB
AAA
58                                       # +=16 => it's called augmented assignment


"""
