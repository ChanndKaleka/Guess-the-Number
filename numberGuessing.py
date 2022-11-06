import random

# Intro
print("Welcome to the number guessing game! \nI am thinking of a number between 0 and 10!")

# Generating the random number to be guessed
numberToGuess=random.randrange(0,11)

# Initialize the number of attempts and the boolean value for state of game
attempts=5
gameOver=False

while attempts>0:
    userGuess=int(input("Guess a number: "))
    if(userGuess<numberToGuess):
        print("Too low \n Guess again!")
        attempts -=1
        print(f"Attempts remaining: {attempts}")
    elif(userGuess>numberToGuess):
        print("Too high \n Guess again!")
        attempts -=1
        print(f"Attempts remaining: {attempts}")
    else:
        print("You have guessed correctly!")
        break