#Get user input and print it out
#Input is always a string

"""name = input("What is your name? ")
age = int(input("How old are you? "))+1

print(f"Hello {name}! You are {age} years old.")"""


#Exercise 1
"""
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print()
print("--------------------")
print(f"Today I went to a {adjective} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}.")
print(f"I was {adjective3}.")
"""

#Exercise 2
"""
lenght = float(input("Enter the lenght of the cube: "))
width = float(input("Enter the width of the cube: "))
height = float(input("Enter the height of the cube: "))

volume = lenght*width*height

print(f"The area of the rectangle is {volume}.")
"""

#Exercise 3
item = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter how many items you want: "))
total = round(price*quantity,2) #Compensate for floating point errors

print(f"The total price of {quantity} {item} is {total}.")
