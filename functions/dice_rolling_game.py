import random

def roll():
    return random.randint(1, 6)

def main():
    player_1 = input("Plesae enter your name\n")
    player_2 = input("Please enter your name\n")

    roll_1 = roll()
    print(player_1, "rolls", roll_1)
    roll_2 = roll()
    print(player_2, "rolls", roll_2)

    if(roll_1 > roll_2):
        print(player_1, "wins")
    elif(roll_1 < roll_2):
        print(player_2, "wins")
    else:
        print("Equality")

main()