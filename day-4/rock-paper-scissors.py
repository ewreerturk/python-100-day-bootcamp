import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("What Do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors")

choise = int(input())

if choise == 0:
    print ("Your choise:", rock)
elif choise ==1:
    print ("Your choise:", paper)
else:
    print("Your choise:", scissors)


my_list = [rock, paper, scissors]

my_list_index = random.randint(0, len(my_list) -1 )

computer_choise = my_list[my_list_index]

print ("Computer choise:", computer_choise)

if computer_choise == my_list[0] and choise == 0:
    print("No-one win, it's equal")
elif computer_choise == my_list[0] and choise == 1:
    print("You are  win, Computer Lose")
elif computer_choise == my_list[0] and choise == 2:
    print("You are  lose, Computer win")


elif computer_choise == my_list[1] and choise == 1:
    print("No-one win, it's equal")
elif computer_choise == my_list[1] and choise == 0:
    print("You are  lose, Computer win")
elif computer_choise == my_list[1] and choise == 2:
    print("You are  win, Computer Lose")


elif computer_choise == my_list[2] and choise == 1:
    print("You are  lose, Computer win")
elif computer_choise == my_list[2] and choise == 0:
    print("You are  win, Computer Lose")
elif computer_choise == my_list[2] and choise == 2:
    print("No-one win, it's equal")

else:
    print("Oyunu bastan baslat bi yerde hata yaptin.")





