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
    underscore = ['_ '] * word_length

    print(chosen_word)
    print(f'Your word has {word_length} letters.')
    print(underscore)

    # making a new list to catch wrong guesses
    guesses = []
    # starting a wrong guesses talley
    guess_count = 0
    # function for guesses
    while guess_count < 8:
        user_guess = input("Guess a letter: ")
        print('Guess: ', user_guess)
        if len(user_guess) > 1:
            print("thats a no-no")
        elif user_guess not in chosen_word and user_guess not in guesses:
            guess_count += 1
            guesses.append(user_guess)
            print('Wrong guesses: ', guess_count)
            print('Guesses: ', guesses)
        elif user_guess in chosen_word:
            for letter in range(len(chosen_word)):
                if user_guess == chosen_word[letter]:
                    underscore[letter] = chosen_word[letter]
                    guesses.append(user_guess)
            print("".join(underscore))
            if '_ ' not in underscore:
                print("winner winner chicken dinner")
                play_again = input("Do you want to play again Y/N?\n")
                if play_again == 'Y':
                    play_game()
                elif play_again == 'y':
                    play_game()
                else:
                    exit()
    else:
        guess_count == 8
        print("The word was:", chosen_word)
    play_again = input("You lost, try again?  Y/N?\n")
    if play_again == 'Y':
        play_game()
    elif play_again == 'y':
        play_game()
    else:
        exit()


if __name__ == "__main__":
    play_game()

# python mystery_word.py
