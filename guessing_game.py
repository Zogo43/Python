import random
import math

player = True

name = input("Hello, What's your name? ")
input("In this game you have to guess my number")

while player == True:
    print(name + ", please give me an intervall of numbers")
    min_intervall = int(input())
    max_intervall = int(input())
    rng = random.randint(min_intervall, max_intervall)
    difference = max_intervall - min_intervall
    tries = math.floor(difference * 0.4)
    count = 0
    print("Okay! " + name + ", you have " + str(tries) + " tries")
    while count < tries:
        count = count + 1
        guess = int(input())
        if guess < rng:
            print("Your guess is too low")
        elif guess > rng:
            print("Your guess is too high")
        else:
            break
    if guess == rng:
        print("You guessed the number in " + str(count) + " tries!")
    else:
        print("The number was " + str(rng) + ". Better Luck next time! ")
    choice = input("Do you want to play again? (y/n) ")
    if choice != "y":
        player = False