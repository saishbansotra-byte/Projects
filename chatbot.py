import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess == number:
        print("AI: Correct!")
        break
    elif guess < number:
        print("AI: Too Low")
    else:
        print("AI: Too High")