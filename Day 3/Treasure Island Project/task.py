from nis import match

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = str(input("left or right? ")).lower().strip() #strip for spaces and tabs
if(left_or_right != "left"):
    print("Fall into a hole. Game Over")
elif(left_or_right == "left"): #in := gives true for all the substrings in "left"
    swim_or_wait = str(input("Would you like to swim or wait? ")).lower().strip()
    if(swim_or_wait != "wait"):
        print("You are attacked by trout. Game Over.")
    elif(swim_or_wait == "wait"):
        door = str(input("Which door would you like to go, red, blue or yellow ? ")).lower().strip()
        if(door == "red"):
            print("Burned by fire. Game Over.")
        elif(door == "blue"):
            print("Eaten by beasts. Game Over.")
        elif(door == "yellow"):
            print("You Win!")
        else:
            print("Game Over.")





