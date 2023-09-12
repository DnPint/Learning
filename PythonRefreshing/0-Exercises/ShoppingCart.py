
foods= []
prices= []
total = 0

while True:
    food = input("Enter a food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("Your shopping cart:")
for i in range(len(foods)):
    print(f"{foods[i]}: {prices[i]}")
    total += prices[i]

print(f"Total: {total}")
