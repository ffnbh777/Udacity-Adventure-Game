import time
import random
import sys


def print_pause(message_to_print):

    print(message_to_print)
    time.sleep(2)


def intro():

    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are two passageways.")
    print_pause("Which way do you want to go right or left?")


def play_again():

    user_input = input("Would you like to play again? (y/n)").lower()

    if user_input == 'y':

        print_pause("Excellent! Restarting the game ...")

        choice()

    elif user_input == 'n':

        print_pause("Thanks for playing... Goodbye, until we meet again!")

        sys.exit()

    else:

        play_again()


def passageways():
    monsters = ["Dragon", "Goliath", "Goblin", "Grendel"]
    print_pause(f"Standing in the cave is  {random.choice(monsters)}")

    fight_or_run = input("Would you like to (1) fight or (2) run away?")

    if fight_or_run == '1':

        print_pause("As the Monster moves to attack it saw your sword.")

        print_pause(
            "You hold Sword in your hand ready for the attack.")

        print_pause("Monster saw your Sword and runs away.")

        print_pause("You have taken care of the Monster. You WON!")

        play_again()

    elif fight_or_run == '2':

        print_pause("You run back into the dungeon.")

        choice()

    else:

        error_input()


def passageways2():

    print_pause("You have found the treasure!")
    print_pause("You walk back out to the dungeon.")
    monsters = ["Dragon", "Goliath", "Goblin", "Grendel"]
    print_pause(f"Standing in the cave is {random.choice(monsters)}")
    print_pause("Monster tries to stop you.")
    print_pause("You outrun the Monster.")
    print_pause("You took the Monster's treasure")
    print_pause("You WON!")

    play_again()

    choice()


def choice():

    intro()

    print_pause("Enter R to go Right.")

    print_pause("Enter L to go Left.")

    user_choice = input("What would you like to do?(R/L)").upper()

    if user_choice == 'R':

        passageways()

    elif user_choice == 'L':

        passageways2()

    else:

        error_input()


def error_input():

    user_choice = input("(Please enter R or L)\n").upper()

    while True:

        if user_choice == 'R':

            choice()

        elif user_choice == 'L':

            choice()

        else:

            user_choice = input("(Please enter R or L)\n").upper()


def error_answer():

    user_input = input("Please enter y or n:").lower()

    while True:

        while user_input != 'y' or user_input != 'n':

            user_input = input("Please enter y or n:").lower()


def game():

    choice()


game()
