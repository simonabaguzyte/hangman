from importlib.resources import contents
import random

misspelled_letters = ""
guessed_letters = ""
failure_count = 7


def print_options():
    print("\nChoose one of the options below:")
    print("1 - guess the word")
    print("2 - exit the game")

def pick_random_word():
    temp = open('words.txt', "r")
    content = temp.read()
    content_list = content.split(",")
    temp.close()
    random_word = random.choice(content_list)
    return(random_word)

def gives_length_of_the_word():
    length = len(word)
    print("-------------------------------------------------------------------------------")
    print(f"Length of the word is {length} letters:")
    count = 1
    while count <= length:
        print("_ ", end=" ")
        count = count + 1

def message_for_the_winner():
    print("\n********************************************************************************")
    print("BRAVO!!! You have guessed the word!")
    print(f"The word was '{word}'.")
    print("_____")
    print("|    |")
    print("|")
    print("|")
    print("|   \O/")
    print("|    | ")
    print("|   / \ ")
    print("********************************************************************************\n")

def game_over_message():
    print("\n********************************************************************************")
    print("*GAME OVER*")
    print("You have not guessed the word.")
    print(f"The word was '{word}'.")
    print("_____")
    print("|    |")
    print("|    O")
    print("|   /|\ ")
    print("|   / \ ")
    print("|")
    print("|")
    print("\nBetter luck next time!")
    print("********************************************************************************")

if __name__ == "__main__":
    print("\n***WELCOME TO HANGMAN - GUESS THE WORD GAME!***")
    print_options()
    
    continue_game = True  
    while continue_game:
        try:
            choice = int(input("\nEnter your choice (1-2): \n"))
            if choice == 1:
                word = pick_random_word()
                gives_length_of_the_word()
                print("\n\n*You can guess 7 letters, after that you will have to guess the whole word*")

                while failure_count > 0:
                    print("-------------------------------------------------------------------------------")
                    print(f"\n*Misspelled letters: {misspelled_letters} ")
                    print(f"*Correctly guessed letters: {guessed_letters} ")
                    
                    try:
                        users_guess_on_the_letter = str(input("\nEnter the letter: ")).upper()
                        failure_count = failure_count - 1

                        if users_guess_on_the_letter in word:
                            print(f"*Correct! There is one or more '{users_guess_on_the_letter}' in the word*")
                            guessed_letters = guessed_letters + users_guess_on_the_letter
                        
                        elif users_guess_on_the_letter not in word:
                            print(f"*Incorrect! There is not '{users_guess_on_the_letter}' in the word*")
                            misspelled_letters = misspelled_letters + users_guess_on_the_letter
                        else:
                            print("*ERROR. Check your input and try again*")

                        continue

                    except ValueError:
                        print("*ERROR. Check your input and try again*")
                        continue

                if failure_count == 0:
                    print("\n-------------------------------------------------------------------------------")
                    print("\n***IT IS TIME TO GUESS THE WORD***")
                    print(f"\n*Misspelled letters: {misspelled_letters} ")
                    print(f"*Correctly guessed letters: {guessed_letters} ")
                    users_guess_on_the_word = str(input("\nEnter the word: ")).upper()

                    if users_guess_on_the_word != word:
                        game_over_message()
                        continue_game = False
                    elif users_guess_on_the_word == word:
                        message_for_the_winner()
                    break

            elif choice == 2:
                print("\nThank you for using my program!\nI hope to see you next time.")
                break
            elif choice < 1 or choice > 2:
                print("*There was no such choice. Check your input and try again*")
                continue
        except ValueError:
            print("*There was no such choice. Check your input and try again*")
            continue







