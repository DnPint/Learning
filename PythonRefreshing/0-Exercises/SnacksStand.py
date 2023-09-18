menu = {"chips": 3.50, "cola": 2.00, "water": 1.50, "sandwich": 9.00, "chocolate": 2.00}

cart = []
total = 0

print("Welcome to the Snacks Stand!")
print()
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print()

while True:
    choice = input("What would you like to buy? (q to quit) ").lower()
    if choice == "q":
        break
    elif choice in menu: # elif menu.get(choice) != None:
        cart.append(choice)
        total += menu[choice] # total += menu.get(choice)
        print(f"{choice} added to cart.")
    else:
        print("Sorry, we don't have that.")
    print()

print()
print("Your cart:")
for item in cart:
    print(item, end=" ")
print()
print(f"Total: ${total:.2f}")