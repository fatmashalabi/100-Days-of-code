print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
        bill +=1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else: #L:= large pizza
    bill = 25
    if pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
print("Your final bill is: $" + str(bill) + ".")







