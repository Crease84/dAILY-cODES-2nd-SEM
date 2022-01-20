import random


room = 1
choice = 1


print("The Light blinds your eyes")
print("Youre laying down on the ground")
print("You try to move your arms and legs but you feel and see nothing moving")
print("-Enter 'q' to exit and any point")
print("GAME START")
print()
x = 1

while choice != 'q':
    if room == 1:
        print()
        print("Youre placed halfway under a table with two chairs")
        print("A beautiful crystle chandalare hangs above you, behind the table")
        print("The warm white light bathes the room in an off white light")
        print("Theres a door that leads to the East")
        choice = input()
        
        print()
        print()
        print()

        if choice == 'East'or 'east':
            room = 2
            print("A Huge hand picks you up and drags you through the door")
            
        else:
            print("WOWWW CANT YOU READ!?!?!?!?")  
        
    elif room == 2:
        print()
        print("Youre placed on a bright pink couch")
        print("A coffe table to the right accents the tv the room")
        print("Youre staring at a TV with a static image of a dog")
        print("you can see a door to the West and a exit to the south")
        
        numb = random.randrange(1, 101)
        if numb <= 30:
            print ("The hand folds your hands neatly on your lap")
        elif numb <= 50:
            print("Your hair us brushed back behind your head by the hand")
        else:
            print("YOu see the hand messing with something else just out of view")
         
        print("Soooo, Where do you go next?")
         
        choice = input()
        
        print()
        print()
        print()
        
        if choice == 'South'or'south':
            room = 3
            print("The hand lifts you over the buildings walls")
        elif choice == 'West'or'west':
            room = 1
            print("Youre pushed back under the table")
        else:
            print("Bruh, thats not a DIRECTION")
            
    elif room == 4:
        print()
        print("The room is a pastel purple")
        print("You can tell that theres a marble bathtub and a sink")
        print("A mirror far off in the distance vaugly shows you sitting agaisnt the wall with your head faced up")
        print("Theres a door theres a door just ajar to the West")
        choice = input()
        
        print()
        print()
        print()
        
        if choice == 'West' or 'west':
            room = 3
            print('Youre placed in the next adjacent room')
        else:
            print("Error - 404")
            
            
    elif room == 3:
        print()
        print("A big bed takes up most of the room")
        print("The window seems to peel off the walls")
        print("a green desk sits at the end of the bed")
        print("Your exits are to the North and East")
        choice = input()
        
        print()
        print()
        print()
        
        if choice == 'North' or 'north':
            room = 2
            print("A Huge hand picks you up and drags you through the door")
             
        elif choice == 'East' or 'east':
            room = 4
            print("The hand lifts you over the buildings walls")
             
        else:
            print("WHERE??")
