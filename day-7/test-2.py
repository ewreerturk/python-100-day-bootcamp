import random



word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)

print(f"psst, thee soultion is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

#chosen_list = "_ " *len(chosen_word) --- i tried to sometinhg
end_of_game = False

while not end_of_game:
    guess = str(input("Guess a letter. ")).lower()


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print ("You win")