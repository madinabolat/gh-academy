import random 

def create_random_number(start, finish):
    i = random.randint(start,finish)
    return i


start = 1
finish = 100
secret_number = create_random_number(start, finish)
print("guess a number from %d to %d" %(start, finish))

num_attempts = 5
while (num_attempts > 0):
    guess = int(input())
    if guess == secret_number:
        print("correct.")
        print("Game is over! Congratulations.")
        break
    elif guess < secret_number:
        print("too low.")
    else:
        print("too high.")
    num_attempts -= 1

if num_attempts == 0:
    print("You've had too many attempts. The secret number is %d. Game over." %secret_number)
