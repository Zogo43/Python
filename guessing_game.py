import random

player = True

name = input("Hello, What's your name? ")
input("In this game you have to guess my number. You have a max of 5 tries")

while player == True:
    rng = random.randint(0, 10)
    count = 0
    print("Okay! " + name + ", i am thinking of a number between 0 and 10")
    while count < 5:
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