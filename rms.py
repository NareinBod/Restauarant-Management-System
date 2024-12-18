#Ask user for name
name = input("Please enter your name: ")
#Welcome message
print(f"Welcome to our restaurant {name}! Here's the menu:")

#Dictionary to store the items and their price
Menu = {
    "Biryani": 100,
    "Sandwich": 25,
    "Pizza" : 40,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad": 70,
    "Coffee": 80,
    "Chocolate Chip Cookie": 40,
    "Brownie": 30,
}

#A for loop to print the menu 
for key, value in Menu.items():
    print(f"{key}: Rs{value}")

#Initialize a list for user to add items to cart
Cart = []
#Initialize price variable to 0
price = 0

#Error handling for when the user enters an item not present on the menu.
try:
    #Ask user to enter the first add he wants to add to cart 
    choice = input("Enter the first item you want to order = ")

    print(f"Order of {choice} has been added to your order. ")
    price += Menu[choice] 
    Cart.append(choice)
except KeyError:
    print("Sorry we do not have this item in our menu.")

while True:
    add_more = input('Do you want to order anything else? ')
    if (add_more == "yes" or add_more == "Yes"):
        try:
            choice = input("Enter item to add = ")
            Cart.append(choice)
            price += Menu[f"{choice}"]
            print(f"Order of {choice} has been added to your cart.")
            print(f"The total price to pay is {price}")
        except KeyError:
            print("Sorry we do not have this item in our menu.")
    elif (add_more == "no" or add_more == "No"):
        break
    else:
        print("Enter a valid word. Enter yes or no.")

print("\n")

if len(Cart) == 0:
    print("You have not added any item to your cart.")
else:
    print(f"Final order is : ")
    for i in Cart:
        print(i)
    print(f"Price to pay is = Rs {price}")

    