user_name = input("What is your characters name? ")
import random

import time

mob_killed = 0

total_gold = 0


def view_stats():
    print("You killed " + str(mob_killed) + " mobs!")
    print("You earned " + str(total_gold) + " gold!")
    view_continue = input("type quit to quit.")
    if view_continue == str("quit"):
        time.sleep(2)
        quit()
    else:
        print("invalid option, quitting anyways");
        time.sleep(2)
        quit()


health = 10
money = 0
inventory = [""]





def last_option():
    end_option = input("You died!\nType Stats to see your stats and Quit to quit\n")
    if end_option == str("Stats"):
        view_stats()
    elif end_option == str("Quit"):
        print("Goodbye.")
        time.sleep(2)
        quit()
    else:
        print("Invalid option")
        last_option()


def run_option_fort_attack():
    option_fort2 = input("Choose an option:\n1. Scout around the area\n2. Open the nearest chest\n3. Attack the "
                         "nearest mob\n")
    if option_fort2 == str(1):
        print("You arrived at a fortress, with multiple paths in different directions, and a chest in front of you. "
              "On closer inspection, you realize the chest is trapped.")
    elif option_fort2 == str(2):
        print("You open the chest and find a black bone and some dust inside.")
        time.sleep(3)
        print("The ground starts rumbling and the ground beneath you gives way. You fall into the lava.")
        last_option()
    else:
        print("Invalid option")
        run_option_fort_attack()


def run_option_fort():
    option_fort = input("Choose an option:\n1. Scout around the area\n2. Open the nearest chest\n3. Attack the "
                        "nearest mob\n")
    if option_fort == str(1):
        print("You arrived at a fortress, with multiple paths in different directions, and a chest in front of you. "
              "On closer inspection, you realize the chest is trapped.")
        run_option_fort()
    elif option_fort == str(2):
        print("You open the chest and find a black bone and some dust inside.")
        time.sleep(3)
        print("The ground starts rumbling and the ground beneath you gives way. You fall into the lava.")
        last_option()
    elif option_fort == str(3):
        if inventory.index("Gold Sword"):
            print("You walk up to the nearest mob and slash with your sword.\nThe mob runs away.")
            run_option_fort()
    else:
        print("Invalid option")
        run_option_fort()


def run_option4():
    option4 = input(
        "Choose an option:\n1. Dig up the nearest plant\n2. Scout around "
        "this area\n")
    if option4 == str(1):
        print("You walk over to the nearest plant, a strange tree, and punch it multiple times until it breaks.")
        print("You got Strange Wood!")
        inventory.append("Strange Wood")
        run_option4w()
    elif option4 == str(2):
        print(
            "You scout around the area and find that there is a fortress a hundred blocks away from you.\n It is "
            "across the lava though...")
        run_option4a()
    else:
        print("Invalid option")
        run_option4()



def run_option4w():
    option4w = input("Choose an option:\n1. Build a boat and sail to the fortress\n2. Do nothing\n")
    if option4w == str(1):
        print("You craft a boat and sail to the fortress. Luckily, the wood can withstand the heat of the lava.")
        run_option_fort()
    elif option4w == str(2):
        print("You do nothing.")
        run_option4w()
    else:
        print("Invalid option")
        run_option4w()


def run_option4a():
    option4a = input("Choose an option:\n1. Try to find some useful materials nearby\n2. Do nothing\n3. Swim across "
                     "the lava\n")
    if option4a == str(1):
        def run_option3a():
            option3a = input(
                "Choose an option:\n1. Attack the nearest creature\n2. Dig up the nearest plant\n3. Scout around "
                "this area\n")
            if option3a == str(1):
                print(
                    "You run up to the nearest pigman and punch him!\nHe oinks and stabs you with his sword.\nYou "
                    "punch him "
                    "another 19 times in quick sucession somehow and he dies.\n Luckily there are no other pigmen "
                    "nearby to "
                    "witness this event.")
                health -= 2
                mob_killed += 1
                print("You got a gold sword!")
                inventory.append("Gold Sword")
                print("Your health is: " + str(health))
                print("You have " + str(money) + " gold coins.")
                run_option4()
            elif option3a == str(2):
                print(
                    "You walk over to the nearest plant, a strange tree, and punch it multiple times until it breaks.")
                print("You got Strange Wood!")
                inventory.append("Strange Wood")
                run_option4w()
                if option4a == str(2):
                    print("You do nothing.")
                    run_option4a()
                elif option4a == str(3):
                    print("You leap into the lava and immediately start burning.")
                    last_option()


def run_option3():
    option3 = input("Choose an option:\n1. Attack the nearest creature\n2. Dig up the nearest plant\n3. Scout around "
                    "this area\n")
    if option3 == str(1):
        print("You run up to the nearest pigman and punch him!\nHe oinks and stabs you with his sword.\nYou punch him "
              "another 19 times in quick sucession somehow and he dies.\n Luckily there are no other pigmen nearby to "
              "witness this event.")
        health = 10
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
        print(
            "You scout around the area and find that there is a fortress a hundred blocks away from you.\n It is "
            "across the lava though...")
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
        print("You jump into the lava, and within seconds, you get burnt to a crisp.")
        last_option()
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
              "crumbles into the lava under it.")
        last_option()
    elif option1 == str(3):
        last_option()
    else:
        print("Invalid option")
        run_option1()


run_option1()
quit()
