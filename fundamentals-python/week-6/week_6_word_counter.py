# Simple Word Counter. 
# Write a program that asks the user for a sentence. 
# The program should then count the occurrences of each word in the sentence and display the result as a dictionary.

print("Please enter your sentence.")
user_input = input()

words = user_input.split()
word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)
