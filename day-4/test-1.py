import random
import my_module

random_integer = random.randint(1,10)
print(random_integer)
random_float = random.random() * 5
#random() always between 0,1 # *5 beetween [0,4)


print (random_float)
print (my_module.pi)

love_score = random.randint(1,100)
print (f"Your love score is {love_score}")