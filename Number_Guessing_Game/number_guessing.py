import random

randam_number = random.randint(1, 10)

max_attempts = 5
attempts = 0

print("Welcom to the nunber guessing game")
print("Guess a number between 1 and 100")
print(f"You have max_attempts are {max_attempts}")

while attempts < max_attempts:
    guess = int(input("Enter you guess number:"))
    attempts += 1

    if guess > randam_number:
        print("Too high! Try again.")
    elif guess < randam_number:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {randam_number} in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all your attempts. The correct number was {randam_number}.")

    