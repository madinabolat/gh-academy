# Basic Tip Calculator. Write a program that asks for the total bill amount and the tip percentage. It should then calculate and
# display the tip amount and the total bill including the tip.
# Advanced: You can also ask for a name (using input()) and print the total amount with that name in it.

print("Hello! Let's calculate your tip. Please enter your name.")
name = input()
print("Hello, %s! Please enter total bill amount." %name)
bill = float(input())
print("Great! Now enter the tip percentage (format: 0.05 for 5%)")
tip_percent = float(input())
tip = bill * tip_percent
print("%s, your tip amount is %0.2f" %(name, tip))