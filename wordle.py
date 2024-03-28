import random
import sys
import time
from termcolor import colored

#Dagogo Apiafi - 20029184
def print_start():
    print("Let the Wordle begin, you have 40 seconds: ")
    print("May the 6 guesses you have be ever in your favour. ")
    print("After guessing, you may process then by pressing enter")

#   open txt file -> divide words by line gaps -> choose a random word from the list
def read_randomwordle_word():
    with open('wordle_words.txt') as wordleDoc:
        wordle_list = wordleDoc.read().splitlines()
        return random.choice(wordle_list)

def play_game():
    print_start()
    wordle_word = read_randomwordle_word()

    time_limit = 40
    time_start = time.time()
    attempts = 6

    #   6 attempts -> collect user input
    for attempt in range(1, attempts + 1): 
        wordle_guess = input("Enter a 5 letter word: ").lower()

        sys.stdout.write('\x1b[1A') #ansi code to move up one line in terminal
        sys.stdout.write('\x1b[2K') #ansi code to clear current line in terminal
        
        #check time limit
        time_passed = time.time() - time_start
        if time_passed > time_limit:
            print(colored(f"Time's up! You exceeded {time_limit} seconds.", 'red'))
            break

        if len(wordle_guess) != 5:
            print("Please enter a 5 letter word.")
            print(colored(f"Attempts left: {attempts-attempt}", 'cyan'))
            print(colored(f"Time left: {time_limit-time_passed:.2f}", 'cyan'))
            continue

        if wordle_guess == wordle_word:
            print(colored(wordle_guess, 'green'), end="")
            print(colored(f"\nCongrats, you guessed the wordle in {attempt} guess(es)", 'magenta'))
            print(colored(f"Time Taken: {time_passed:.2f} seconds",'blue'))
            break
        
        #after guessing a word wrong, display attempts left and time left
        print(colored(f"Attempts left: {attempts-attempt}", 'cyan'))
        print(colored(f"Time left: {time_limit-time_passed:.2f}", 'cyan'))

    #   error handling - number of letters in a guess -> letters present or absent in wordleword
    #   if letter in the index of the guessed word is the same as in the correct word, print the letter green, etc
        for i in range (len(wordle_guess)):

            if wordle_guess[i] == wordle_word[i]:
             print(colored(wordle_guess[i], 'green'), end="")

            elif wordle_guess[i] in wordle_word:
             print(colored(wordle_guess[i], 'yellow'), end="")

            else:
                print(colored(wordle_guess[i], 'light_grey'), end="")
                
        print()

    if wordle_guess != wordle_word:
        print(f"Sorry, the word was: {wordle_word}")


while True:
    play_game()
    play_again = input("Do you wish to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("That's Game Over. Hope to see you again soon! - Dagogo Apiafi - 20029184")
        break