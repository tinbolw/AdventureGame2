user_name = input("What is your characters name? ")
import random

health = 10
money = 0
inventory = [""]

def run_option4():
    print("you have reached the end of the game! (for now")

def run_option4w():
    print("you have reached the end of the game! (for now")

def run_option4a():
    print("you have reached the end of the game! (for now")


def run_option3():
    option3 = input("Choose an option:\n1. Attack the nearest creature\n2. Dig up the nearest plant\n3. Scout around "
                    "this area\n")
    if option3 == str(1):
        print("You run up to the nearest pigman and punch him!\nHe oinks and stabs you with his sword.\nYou punch him "
              "another 19 times in quick sucession somehow and he dies.\n Luckily there are no other pigmen nearby to "
              "witness this event.")
        health -= 2
        print("You got a gold sword!")
        inventory.append("Gold Sword")
        print("Your health is: " + str(health))
        print("You have " + str(money) + " gold coins.")
        run_option4()
    elif option3 == str(2):
        print("You walk over to the nearest plant, a strange tree, and punch it multiple times until it breaks.")
        print("You got Strange Wood!")
        inventory.append("Strange Wood")
        run_option4w()
    elif option3 == str(3):
        print("You scout around the area and find that there is a fortress a hundred blocks away from you.\n It is across the lava though...")
        run_option4a()
    else:
        print("Invalid option")
        run_option3()


def run_option2():
    option2 = input("Choose an option:\n1. Walk across the bridge\n2. Jump into the lava\n3. Do nothing\n")
    if option2 == str(1):
        print("You walk across the bridge and reach a part of the mainland that is filled with strange plants, "
              "and mean-looking creatures.")
        print("Your health is: " + str(health))
        print("You have " + str(money) + " gold coins.")
        run_option3()
    elif option2 == str(2):
        print("You jump into the lava, and within seconds, you get burnt to a crisp.\nYou died! Relaunch the game to "
              "play again")
        quit()
    elif option2 == str(3):
        print("You do nothing.")
        run_option2()
    else:
        print("Invalid option")
        run_option2()


print("You, " + user_name + ", spawn in a hellish biome reminiscent of the Nether.")


def run_option1():
    option1 = input("Choose an option: \n1.Scout around the area\n2.Attack the nearest object\n3.Jump into the lava\n")

    if option1 == str(1):
        print("As you take a look around, you realize that you spawned on an island with a lone bridge leading off.")
        print("Your health is: " + str(health))
        print("You have " + str(money) + " gold coins.")
        run_option2()
    elif option1 == str(2):
        print("You slam your fist into the ground and the ground shakes! The ground splits where you punched it and "
              "crumbles into the lava under it. You died! Relaunch the game to play again")
        quit()
    elif option1 == str(3):
        print("You died! Relaunch the game to try again")
        quit()
    else:
        print("Invalid option")
        run_option1()


run_option1()
quit()
