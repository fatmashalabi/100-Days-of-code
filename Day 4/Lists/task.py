import random
states_of_germany = ["Hessen", "Bayern"]
print(states_of_germany)
print(states_of_germany[0])
states_of_germany.append("Berlin")
print(states_of_germany)
states_of_germany.extend(["Badenwürttemberg","Nordrhein-Westfalen"])
print(states_of_germany)


friends = ["Amitav", "Reem", "Fatema", "Hadil", "Fatma", "Ravi", "Nihal", "KC", "Wiwin", "Zihao", "Doruk", "Ronja","Kristina", "Ivan"]
# 1 Option
random_index = random.randint(0, len(friends)-1)
print(friends[random_index])
#2nd Option
print(random.choice(friends))
