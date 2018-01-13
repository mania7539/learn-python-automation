
# This is a guess number game

import random;
print("Hello. What is your name?");
name = input();
secretNumber = random.randint(1,20);

# print("DEBUG: Secret number is " + str(secretNumber));

print("Well, " + name + ", I am thinking of a number between 1 and 20.");

# Ask the player to guess 6 times.
for guessesTaken in range(0, 6):
    print("Take a guess.");
    guess = int(input());   # type conversion: string converts to int
    if guess < secretNumber:
        print("Your guess is too low.");
    elif guess > secretNumber:
        print("Your guess it too high.");
    else:
        break; # This condition is the correct guess!

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in 1 and 20.");
else:
    print("Nope. The number I was thinking of was: " + str(secretNumber));
