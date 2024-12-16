import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

possible_password=""

random_index = 0

while(nr_letters > 0):
    random_index = random.randint(0, len(letters))
    possible_password += letters[random_index]
    nr_letters-= 1


while(nr_symbols > 0):
    random_index = random.randint(0, len(symbols))
    possible_password += str(symbols[random_index])
    nr_symbols-=1

while(nr_numbers > 0):
    random_index = random.randint(0, len(numbers))
    possible_password += str(numbers[random_index])
    nr_numbers-=1

#password in the same given order
print(str.lower(possible_password))

#hard version:
#Convert the string to a list of characters
char_list = list(possible_password)
#Shuffle the list
random.shuffle(char_list)
#Convert the shuffled list back to a string
shuffled_password = ''.join(char_list)
print("shuffled version = " + shuffled_password)