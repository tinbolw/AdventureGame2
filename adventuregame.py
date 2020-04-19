
world_selection = input("What world do you want to play? \n1.Hell World \n2.Grassy World \n3.Ice World\n")

if world_selection == str("Hell World"):
    print("loading hellworld...")
    import hellworld as hw
elif world_selection == str("Grassy World"):
    print("loading grassy world...")
    import grassyworld as gw
elif world_selection == str("Ice World"):
    print("loading ice world...")
    import iceworld as iw
else:
    print("Invalid selection")
    quit()





end_game_screen = input("Type Quit to quit, type Stats to see your stats")
if end_game_screen == str("Quit"):
    quit()
elif end_game_screen == str("Stats"):
    print("Wip")
else:
    print("Invalid option")
    quit()



