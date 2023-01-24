# Run this to play the game!

# NOTE: to run this, click "Shell" in the bottom left,
# and run the command:
#
# python play.py

from main import wordle_feedback
# Import list of English words
import nltk
from nltk.corpus import words
import random

nltk.download('words')  # This can be commented out after it has run once
all_english_words = words.words()


def just_words_of_one_length(all_words, length):
    '''Only get words of a specific length.'''
    words_with_x_letters = [
        word.lower() for word in all_words if len(word) == length
    ]
    return words_with_x_letters


def get_random_word(length):
    '''Returns a random word of a given length.'''
    list_of_words = just_words_of_one_length(all_english_words, length)
    random_index = random.randint(0, len(list_of_words) - 1)
    random_word = list_of_words[random_index]
    return random_word


# Play the game
secret = get_random_word(3)
print(f'Guess a {len(secret)}-letter word!\n')
while True:
    guess = input('Guess the word: ')

    if guess == secret:
        print(f'YOU WIN! The secret was "{secret}."')
        break
    else:
        wordle_feedback(guess, secret)
