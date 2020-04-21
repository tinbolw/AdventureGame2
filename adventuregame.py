world_selection = input("What world do you want to play? \n1.Hell World \n2.Grassy World \n3.Ice World\n")

if world_selection == str(1):
    print("loading hellworld...")
    import hellworld as hw
elif world_selection == str(2):
    print("loading grassy world...")
    import grassyworld as gw
elif world_selection == str(3):
    print("loading ice world...")
    import iceworld as iw
else:
    print("Invalid selection")
    quit()


