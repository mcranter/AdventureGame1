import time
import random
import sys
items = []
weapons = ["Sword!", "Knife!", "Machete!", "Katana!"]
player_weapon = random.choice(weapons)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1.5)


def play_again(y,n):
    while True:
        again = input("Would you like to play again? (y/n)").lower()
        if again == 'y':
            items.remove(player_weapon)
            items.remove('Fish')
            intro()
            option_1()
        if again == 'n':
            print_pause("Thanks for playing!\n")
            exit()
        else:
            input("Would you like to play again? (y/n)").lower()


def intro():
    print_pause("You find yourself in a dark forest.")
    print_pause("In front of you is a crossroads.\n")


def fish(y, n):
    while True:
        fish = input("Would you like to try catch it? (y/n)").lower()
        if (player_weapon) in items:
            if fish == 'y':
                print_pause("You use your weapon to spear the fish.\n")
                print_pause("It's a salmon! This will be delicious.\n")
                print_pause("Now we need somewhere to cook it..\n")
                items.append('Fish')
                print_pause("You leave and head back to the crossroads.")
                option_1()
        if fish == 'n':
            print_pause("Killing animals is wrong!\n")
            print_pause("You bid Salmon Rushdie adieu")
            print_pause("and return to the crossroads.\n")
            intro()
            option_1()

        else:
            print_pause("You watch the fish for a while,")
            print_pause("but with no weapon there's little point.")
            print_pause("With a last longing glance, you head back")
            print_pause("to the crossroads\n")
            option_1()


def option_1():
    print_pause("1. Right lies a clear, well-trodden walkway\n"
                "2. Left lies an overgrown trail\n"
                "3. Ahead lies a stream\n")
    way = input("Which way will you go?\n"
                "Choose 1, 2 or 3:\n")

    if way == '1':
        print_pause("You turn right and start walking.")
        print_pause("Soon, you come to a market stall.")
        if (player_weapon) in items:
            print_pause("Looks like the merchant's on lunch.\n")
            print_pause("There's nothing for you here.\n")

        else:
            print_pause("A merchant appears.")
            print_pause("He offers you a weapon!")
            print_pause("..IF you'll sing him a song by Coldplay")
            print_pause("You hate them, but a weapon would be useful..")
            print_pause("You grudgingly sing 'Yellow'.\n")
            print_pause("The merchant wipes away a tear and gives\n"
                        "you a: ",)
            print_pause(random.choice(weapons))

        items.append(player_weapon)
        print_pause("You return to the crossroads\n")

        option_1()

    if way == '2':
        print_pause("After fighting your way through the undergrowth")
        print_pause("you come to a cave.")
        print_pause("Night approaches - a cave would provide shelter.")
        print_pause("You enter the cave, but it isn't empty!")
        print_pause("Crouched in a corner is Chris Martin from Coldplay")
        if ('Fish') in items:
            print_pause("He looks like he could use a good meal.\n")
            print_pause("You give him the fish you caught and")
            print_pause("he fries it up with some garlic butter")
            print_pause("for you both. Delcious!\n")
            print_pause("He gratefully offers you sleeping bag and\n")
            print_pause("You settle in for a comfy night\n")
            print_pause("..zzzzZZZ...\n")
            print_pause("THE END\n")
            play_again('y', 'n').lower()
        elif (player_weapon) in items:
            print_pause("You take out your weapon,") 
            print_pause("chop him into pieces")
            print_pause("and feast on his remains.\n")
            print_pause("He tastes better than than he sounds!\n")
            print_pause("THE END\n")
            play_again('y', 'n')

        else:
            print_pause("You begin to slowly back away but he spots you!")
            print_pause("He starts singing and soon you fall")
            print_pause("into an unconsciousness from which you")
            print_pause("never awaken.")
            print_pause("You perish soon after.")
            print_pause("THE END\n")
            play_again('y', 'n')

    if way == '3':
        print_pause("You come to a peaceful stream.\n")
        print_pause("But wait! You spot a fish\n")
        if (player_weapon) in items:
            fish('y', 'n').lower()
        else:
            print_pause("You watch it for a while, your tummy rumbling")
            print_pause("If only you had a way to catch a fish\n")
            print_pause("Reluctantly, you return to the crossroads\n")
            option_1()

    else:
        option_1()


intro()
option_1()
play_again()

