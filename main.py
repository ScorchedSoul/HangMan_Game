import random

from wordList import easy_words
from wordList import medium_words
from wordList import hard_words

def choose_word(words_set):
    return random.choice(list(words_set))

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.upper() in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter as your guess: ").strip().upper()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        else:
            print("Invalid guess. Please enter a single letter that you haven't guessed before.")

def update_guessed_letters(guessed_letters, guess):
    guessed_letters.add(guess)

def check_guess(word, guessed_letters, guess):
    return guess in word.upper()

def is_word_guessed(word, guessed_letters):
    return all(letter.upper() in guessed_letters for letter in word)

def hangman():
    print("Welcome to Hangman!")
    difficulty = input("Choose the difficulty level (Easy, Medium, or Hard): ").strip().lower()

    if difficulty == "easy":
        words_set = easy_words
    elif difficulty == "medium":
        words_set = medium_words
    elif difficulty == "hard":
        words_set = hard_words
    else:
        print("Invalid difficulty level. Please choose Easy, Medium, or Hard.")
        return

    word_to_guess = choose_word(words_set)
    guessed_letters = set()
    attempts_left = 6

    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        print("Word to guess:", display_word(word_to_guess, guessed_letters))

        if is_word_guessed(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        guess = get_guess(guessed_letters)

        if check_guess(word_to_guess, guessed_letters, guess):
            update_guessed_letters(guessed_letters, guess)
            print("Good guess!")
        else:
            update_guessed_letters(guessed_letters, guess)
            attempts_left -= 1
            print("Incorrect guess!")

    if attempts_left == 0:
        print("\nYou ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
