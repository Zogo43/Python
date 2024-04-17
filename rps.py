import random

choices = ["Rock", "Paper", "Scissors"]
player = False

while player == False :
    player_input = input("Rock, Paper or Scissors? ")
    rng = random.randint(0, 2)
    enemy = choices[rng]
    if player_input == enemy:
        print("Tie!")
    elif player_input == "Rock" :
        if enemy == "Scissors" :
            print("You win!")
            player = True
        else:
            print("You lose! Try again")
    elif player_input == "Paper" :
        if enemy == "Rock" :
            print("You win!")
            player = True
        else:
            print("You lose! Try again")
    elif player_input == "Scissors" :
        if enemy == "Paper" :
            print("You win!")
            player = True
        else:
            print("You lose! Try again")
    else:
        print("Unvalid input! Try again")
    if player == True :
        restart = input("Do you want to play again? (y/n) ")
        if restart == "y" :
            player = False