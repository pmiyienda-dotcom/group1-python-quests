#!/usr/bin/python3

def number_wizard():
    secret_number = 42
    guess = int(input("Guess the secret number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct! You are a Number Wizard.")

number_wizard()
