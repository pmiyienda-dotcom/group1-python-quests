secret_number = 7

guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    
    if guess == secret_number:
        print("Correct! You guessed it!")
    else:
        print("❌ Wrong! Try again...")

