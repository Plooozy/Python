import random
import time


def main():
    print("Welcome to the Dice game!")
    n = int(input("How many rolls? : "))
    for i in range(n):
        print("Rolling Dice...")
        time.sleep(2)
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        score = dice_1 + dice_2
        print(f"Side of dice rolled: {dice_1} and {dice_2}")
        print(f"Sum of a throw: {score}")

main()