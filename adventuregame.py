
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

print(world_selection + " loaded")


hw.launch()



hellworld.launch()
