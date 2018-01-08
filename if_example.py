# introduce if code block
name = "Alice";
if name == "Alice":
    print("Hi Alice");
print("Done");


# if, else
print("Please enter your password: ");
password = input();

if password == "swordfish":
    print("Access granted.");
else:
    print("Wront password.");


# if, elif
name = "Bob";
age = 3000;
if name == "Alice":
    print("Hi Alice");
elif age < 12:
    print("You are not Alice, kiddo.");
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.");
elif age > 1000:
    print("You are not Alice, grannie.");


# Truthy and Falsey condition
print("Enter a name.");
name = input();
if name:    # this is what we call truthy and falsey conditioning
    print("Thank you for entering a name.");
else:
    print("You did not enter a name.");


