two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
x = ( str(two_digit_number)[0])
y = ( str(two_digit_number)[1]) 
print (int(x)+int(y))



####################################
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height =float(height)
weight =float(weight)
bim = (weight/height**2)
print (int(bim))


#######################################
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")

#######################################

print ("Welcome to the tip calculat!")
total_bill = float(input("What was the total bill"))
tip = int(input("How much tip would you like to give ?,10 12, or 15?"))
peoples = int(input("How many poeople to split the bill?"))
each_person_should_pay = (total_bill - tip) / peoples
print("Each person should pay",each_person_should_pay )