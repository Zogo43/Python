import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

def random_number() :
    return random.randint(0, 15)

player = False

while player == False:
    consent = input("Do you want to generate a hexcolor? (y/n) ")
    if consent == "y":
        hex_color = "#"
        for x in range(6):
            hex_color += str(numbers[random_number()])
        print(hex_color)
    else:
        player = True