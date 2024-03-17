print("Welcome to Treasure Island.  Your mission is to find the treasure. ")

user_actions = str(input("Please select left or right. "))

if user_actions == 'left':
    swim_wait = str(input("Please take a action swim or wait. "))
    if swim_wait == 'wait':
        which_door = str(input("Please select door. "))
        if which_door == 'red':
            print("Burned by fire GAME OVER ")
        elif which_door == 'blue':
            print ("Easten by beasts GAME OVER ")
        elif which_door == 'yellow':
            print("You WIN!!! ")
        else:
            print ("GAME OVER ")
    else:
        print ("GAME OVER ")
else:
    print ("GAME OVER ")