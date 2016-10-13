forestOrLake = input("Would you like to..." +
                      "\n 1. Walk through the forest" +
                      "\n 2. Swim across the lake")

if forestOrLake == "1":
    forestAnswer = input("Would you like to walk during the day or night ?")
    if forestAnswer == "day":
        forestAnsweragain = input("Do you walk with friends or alone?")
        if forestAnsweragain == "with friends":
                print("Your friends save you from dying. You continue the journey.")
        else:
                print("No one is around to protect you from the hungry bear approaching you. End of the journey.")
    else:
        print("You get eaten and cannot continue your journey.")
else:
    lake = input("Would you like to swim on the deep end of the shallow end?")
    if lake == "shallow end":
        lakeAnswer = input("Do you want to swim on the shallow end with piranha or sharks?")
        if lakeAnswer == "piranha":
            print("They don't eat you. You continue your journey!")
        else:
            print("You are eaten by the sharks. You cannot continue your journey.")
    else:
        anotherlakeAn
        swer = input("Do you use a floating device or do you use no assistance?")
        if anotherlakeAnswer == "floating device":
                print("You stay alive. You continue your journey!")
        else:
                print("You drown. End of the journey for you.")
            
    
        
