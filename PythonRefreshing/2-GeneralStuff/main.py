#Imprts
import math
import random

#Variables
age = 25
name = "John"
online=True
note = 5.5
Student = True
credit_number = "1234-5678-9012-3456"
money = 10000.00
response =""

#multiple assignments
x,y,z = 1,-2,3.14
a=b=c=4.0

#Print the age in different ways
#print("You are "+str(age)+" years old.")
#print("You are",age,"years old.")
#print(f"You are {age} years old.")

#mess around with print statements
#print(f"Hello {name}! You are {age} years old.")
print(f"Hello {name}! You are {age} years old. Are you online? {online}")
print(x,y,z,a,b,c)
print()

#Type casting
print("Type casting:")
print(float(age)) #25 becomes 25.0
print(int(note)) #5.5 becomes 5
print(bool(age)) #25 becomes True (ANY number except 0 is True)
print(bool(name)) #John becomes True (ANY string is True)
print()

#Math
print("Math:")
print(round(z)) #rounds to nearest integer 
print(round(z,1)) #rounds to 1 decimal place
print(abs(y)) #absolute value
print(pow(y,3)) #y to the power of 3
print(max(x,y,z)) #returns the largest number
print(math.pi) #returns pi
print(math.sqrt(9)) #returns the square root of 9 as a float
print(math.floor(3.9)) #rounds down to the nearest integer
print(math.ceil(3.1)) #rounds up to the nearest integer
print()

#If Else
#Attention to the order of the if statements, the first one that is true will be executed
print("If Else:")
if age > 18: 
    print("You are an adult.")  
elif age < 0:
    print("You are not born yet.")
elif age >= 100:
    print("You are very old.")
else:
    print("You are not an adult.")

if not online:
    print("You are touching grass.")
else:
    print("You are online.")

if note >= 5.5 and Student:
    print("You are a good student.")
print()


#String methods
print("String methods:")
print(len(name)) #returns the length of the string
print(name.upper()) #returns the string in uppercase
print(name.lower()) #returns the string in lowercase
print(name.rfind("o")) #returns the index of the last occurence of the character
print(name.find("o")) #returns the index of the first occurence of the character
print(name.replace("J","K")) #replaces the first character with the second character
print("John" in name) #returns True if the string is in the string
print("John" not in name) #returns True if the string is not in the string
print(credit_number[0:4]) #returns the first 4 characters of the string
print(credit_number[5:]) #returns the characters from the 6th character onwards
print(credit_number[::2]) #returns every second character
print()

#Format specifier
print("Format specifier:")
print(f"{age:.2f}") #prints the age with 2 decimal places
print(f"{age:04}") #prints the age with 4 digits, if the number is smaller than 4 digits, it will be filled with 0s
print(f"{money:,.2f}") #prints the money with commas
print()

#Loops
print("Loops:")
"""while response == "":
    response = input("Enter something: ")
print(f"You entered {response}.")"""

for i in reversed(range(0,3)):
    print(i, end=" ")
print()
for i in credit_number:
    print(i,end="")

print()

#Lists, Tuples, Sets
print("Lists, Tuples, Sets:")
my_list = [1,2,3,4,5]
my_list2 = ["a","b","c","d","e"]
print(my_list)
print(my_list[0])
my_set = {1,2,3,4,5} #sets are unordered and don't allow duplicates, can add and remove items
my_tuple = (1,2,3,4,5) #tuples are ordered and allow duplicates, can't add or remove items. Tuples are faster
print()

# 2D lists
print("2D lists:")
my_2d_list = [[1,2,3],[4,5,6],[7,8,9]] #works with tuples and sets as well

for i in my_2d_list:
    for j in i:
        print(j, end=" ")
    print()
print()

#Dictionary
print("Dictionary:")
my_dict = {"name":"John","age":25,"online":True}
print(my_dict.get("name")) #returns the value of the key
my_dict.update({"name":"Jack"}) #updates the value of the key
my_dict.update({"height":1.80}) #adds a new key and value
print(my_dict.keys()) #returns the keys
print(my_dict.values()) #returns the values

for key in my_dict.keys():
    print(key, end="/")
    print(my_dict.get(key), end=" | ")
print() 

for key, value in my_dict.items():
    print(f"{key}:{value}", end=" | ")
print()
print()

#random numbers
print("Random numbers:")
print(random.random()) #returns a random float between 0 and 1
print(random.randint(1,10)) #returns a random integer between 1 and 10
print(random.choice(my_list)) #returns a random item from the list
random.shuffle(my_list) #shuffles the list
print(my_list)
