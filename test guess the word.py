
# Your Name
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORDS,
    choose_word,
    check_guess,
    display_word
)

# Test that the random word comes from the list
def test_choose_word():
    word = choose_word()
    assert word in WORDS

# Test a correct letter guess
def test_correct_guess():
    assert check_guess("apple", "a") is True

# Test an incorrect letter guess
def test_incorrect_guess():
    assert check_guess("apple", "z") is False

# Test that repeated letters are revealed
def test_repeated_letters():
    guessed = {"p"}
    assert display_word("apple", guessed) == "_ p p _ _"

# Test that unknown letters stay hidden
def test_hidden_letters():
    guessed = {"a"}
    assert display_word("apple", guessed) == "a _ _ _ _"

# Test that all letters appear when guessed
def test_complete_word():
    guessed = {"a", "p", "l", "e"}
    assert display_word("apple", guessed) == "a p p l e"
