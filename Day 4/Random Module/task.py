import random
import my_module

#random_integer = random.randint(1,9)
#print(random_integer)
#print(my_module.my_favorite_number)
#random_number_0_to_1 = random.random()
#print(random_number_0_to_1)

#Create a coin flip program using what you have learnt about randomisation in Python.
# It should randomly print "Heads" or "Tails" everytime it is run.

random_number = random.random()*10
if(random_number <=5):
    print("Heads")
else:
    print("Tails")