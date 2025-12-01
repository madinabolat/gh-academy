# Dice Rolling Simulator. 
# Use the random module to create a function that simulates rolling two six-sided dice and returns their sum.
# Then, create a program that asks the user how many times to roll the dice and uses a dictionary to track and display the frequency of each sum.
import random

def roll_dice_sum():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1 + die2

print("Enter the number of times you want to roll the dice")
n = int(input())

dice_sum_frequencies = {}

for i in range(n):
    dice_sum = roll_dice_sum()
    dice_sum_frequencies[dice_sum] = dice_sum_frequencies.get(dice_sum,0) + 1

print(dice_sum_frequencies)


