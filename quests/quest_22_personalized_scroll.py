#!/usr/bin/python3

def personalized_greeting(name, quest):
    """Prints a message using the provided name and quest."""
    print(f"Greetings, {name}! Your journey for the {quest} begins now.")

# Step 1: Ask the user for their name
user_name = input("Enter your name: ")

# Step 2: Ask the user for their quest
user_quest = input("Enter your quest: ")

# Step 3: Call the function with the user's answers
personalized_greeting(user_name, user_quest)
