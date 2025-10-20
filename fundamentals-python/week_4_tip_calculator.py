# Basic Tip Calculator. Write a program that asks for the total bill amount and the tip percentage. It should then calculate and
# display the tip amount and the total bill including the tip.
# Advanced: You can also ask for a name (using input()) and print the total amount with that name in it.


# Upgrade: Advanced Tip Calculator. Modify last week's Tip Calculator. 
# Add a feature that asks how many people are splitting the bill and their names.
# The program should then calculate and display how much each person needs to pay.
# Add a condition: if the tip percentage is over 20%, print a "Thank you for your generosity!" message.


print("Hello! Let's calculate your tip. How many people are splitting the bill?")
num_people = int(input())
names = []

print("Please enter names of each person. One by one")
for i in range(num_people):
    print("Name for person %d: " %(i+1))
    name = input()
    names.append(name)

print("Please enter total bill amount.")
bill = float(input())

print("Great! Now enter the tip percentage (format: 0.05 for 5%)")
tip_percent = float(input())

total_bill_after_tip = bill * (1 + tip_percent)
bill_per_person = total_bill_after_tip / num_people

for name in names:
    print(name, end = ", ")

print("each of you should pay: %0.2f" %bill_per_person)

if tip_percent > 0.2: 
    print("thanks for your generosity!")