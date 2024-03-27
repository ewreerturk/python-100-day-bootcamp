import random

word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)

print(f"psst, thee soultion is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
guess = str(input("Guess a letter. ")).lower()
#chosen_list = "_ " *len(chosen_word) --- i tried to sometinhg



for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)