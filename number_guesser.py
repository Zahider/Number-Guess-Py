import random #importing module

print("Welcome to Random number guesser!")
print("Number is between 0 and 10")

guess = input("Make a guess: ")

if guess.isdigit(): #isdigit() checks if variable  is an integer
    guess = int(guess) #if variable is an integer then we convert it to an integer from a string

    if 0 > guess > 10:
         print("Please enter a number between 0 and 10, Goodbye")
    else:
         print("Please type a number next time, Goodbye")

number = random.randrange(0, 11) #generates a random number between 0 and 11 not including 11
guesses = 0#variable to hold number of guesses

while True:
        guesses += 1#add 1 to the number of guesses after each iteration of the loop
        guess = input("Make another guess: ")
        if guess.isdigit(): #isdigit() checks if variable  is an integer
            guess = int(guess)
        else: 
            print("Please type a number next time.")
            continue

        if guess == number:
             print("Correct, the number was ", number, "!")
             break
        elif guess > number:
             print("You guessed too high!")
        else:
             print("You guessed too low!")

print("You got it in ", guesses, " guesses!")