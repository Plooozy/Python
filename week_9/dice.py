import random
import time

dice = [1, 2, 3, 4, 5, 6]

def roll_dice():
    side_1 = random.choice(dice)
    side_2 = random.choice(dice)
    return side_1, side_2

def calculate(side_1, side_2):
    return side_1 + side_2

def main():
    print("Welcome to Dice game")
    n = int(input("How many rolls? "))
    for i in range(n):
        print("Rolling Dice...")
        time.sleep(2)
        s1, s2 = roll_dice()
        print(f"Dice rolled: {s1} and {s2}")
        print(f"Sum: {calculate(s1, s2)}")

main()
