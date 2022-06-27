from importlib.resources import contents
import random

guesses_for_letters_left = 7

def game_over_message():
    print("\n\n*GAME OVER*")
    print("You have not guessed the word.\nBetter luck next time!")
    print("_____")
    print("|    |")
    print("|    O")
    print("|   /^\ ")
    print("|    |")
    print("|   /^\ ")
    print("|")
    print("|")

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

# def start_guessing():


if __name__ == "__main__":
    print("\n***WELCOME TO HANGMAN - GUESS THE WORD GAME!***")
    print_options()

    while True:
        choice = int(input("\nEnter your choice (1-2): "))
        try:
            if choice == 1:
                word = pick_random_word()
                print("\n-----------------------------------")
                print(word)
                print("-----------------------------------\n")
                
                # start_guessing()
                print("*You can guess 7 letters, after that you will have to guess the whole word*")
                while guesses_for_letters_left >=1 and guesses_for_letters_left <= 7:
                    users_guess_on_the_letter = str(input("Enter the letter: "))
                    print(users_guess_on_the_letter)
                    guesses_for_letters_left = guesses_for_letters_left - 1
                    print(guesses_for_letters_left)

                if guesses_for_letters_left == 0:
                    print("\n*It is time to guess the whole word*")
                    users_guess_on_the_word = str(input("Enter your guess: "))
                    print(users_guess_on_the_word)
                    if users_guess_on_the_word != word:
                        game_over_message()
                        break

            elif choice == 2:
                print("\nThank you for using my program!\nI hope to see you next time.")
                break
        except ValueError:
            print("*There was no such choice. Try again*")


        




