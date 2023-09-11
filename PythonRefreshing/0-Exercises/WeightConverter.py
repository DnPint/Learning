
weight = float(input("Enter your weight: "))
unit = input("Enter the unit (L)bs or (K)g: ")

if unit.upper() == "L":
    print(f"You are {round(weight/2.205,1)} kilograms.")
elif unit.upper() == "K":
    print(f"You are {round(weight*2.205,1)} pounds.")
else:
    print("Invalid unit.")
