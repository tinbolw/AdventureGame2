user_name = input("What is your characters name? ")

print("You, " + user_name + ", spawn in a hellish biome reminiscent of the Nether.")
option1 = input("Choose an option: \n1.Scout around the area\n2.Attack the nearest object\n3.Jump into the lava\n")

if option1 == str(1):
    print("As you take a look around, you realize that you spawned on an island with a lone bridge leading off.")
elif option1 == str(2):
    print("You slam your fist into the ground and the ground shakes! The ground splits where you punched it and "
          "crumbles into the lava under it. You died! Relaunch the game to play again")
    quit()
elif option1 == str(3):
    print("You died! Relaunch the game to try again")
    quit()
else:
    print("Invalid option")
    quit()
