print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
         print("You should pay 5 dollar.")
    elif age <= 18:
         print("You should pay 7 dollar.")
    else:
         print("Please pay 12 dollar.")
else:
     print("Sorry, you have to grow taller before you can ride...")



