import random

choice = {
    1: "SNAKE",
    2: "WATER",
    3: "GUN"
}

print("**** SNAKE WATER GUN GAME ****")

while True:
    a = int(input("""
ENTER 1 : SNAKE
ENTER 2 : WATER
ENTER 3 : GUN
ENTER 4 : EXIT
: """))

    if a == 4:
        print("Thanks for playing!")
        break

    if a not in choice:
        print("Invalid Choice!\n")
        continue

    b = random.randint(1, 3)

    print("YOU CHOOSE :", choice[a])
    print("COMPUTER CHOOSE :", choice[b])

    if a == b:
        print("IT'S A DRAW!")
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print("YOU WON!")
    else:
        print("YOU LOST!")

    print("-" * 30)