import random


# FUNCTION FOR OPENING FILE AND READING IT
def open_file(file):
    # opening the file in read mode and will auto close it too
    with open(file) as my_file:
        # reading the file on the right then in data (on left) it makes it readable for humans
        data = my_file.read()
        # formatting words into a list
        format_data = data.split()
        # catching formatted data
        return format_data


# RANDOM WORD CHOICE FUNCTION
def random_word(list):
    # selecting a random word from a blank list
    word = random.choice(list)
    # catching the random word
    return word


def play_game():
    # links random word choice function to the file in question
    chosen_word = random_word(open_file('words.txt'))
    # defining random word length
    word_length = len(chosen_word)
    # attributing underscores to the length
    underscore = '_ ' * word_length

    print(chosen_word)
    print(f'Your word has {word_length} letters.')
    print(underscore)


# 8 wrong guesses loop
# count = 0
# while wrong_guesses <= 8:
#     play_game()
#     if wrong_guesses == 8:
#         display random_word
#         print("womp womp")
#         break
#     else:
#         display random_word
#         print("Winner winner chicken dinner")
# PLAY AGAIN LOOP
# play_again = input("Do you want to play again Y/N?\n")
# if play_again == 'Y':
#     play_game()
if __name__ == "__main__":
    play_game()

# python mystery_word.py
