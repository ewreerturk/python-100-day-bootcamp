print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
         print("Child tickets are 5 dollar.")
         bill += 5
    elif age <= 18:
         print("Youth tickets are 7 dollar.")
         bill += 7
    else:
         print("Adult tickets are 12 dollar.")
         bill += 12
    wants_photo=input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        bill += 3
        print(f"You should pay {bill} dollar")
    else:
         print(f"You should pay {bill} dollar")
else:
     print("Sorry, you have to grow taller before you can ride...")
