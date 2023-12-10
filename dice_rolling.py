import random

def roll_dice():
    return random.randint(1, 6)

play = input("Roll the dice? (yes/no): ").lower()

while play == "yes":
    result = roll_dice()
    print(f"You rolled: {result}")
    play = input("Roll again? (yes/no): ").lower()

print("Thanks for playing!")