#Imprts
import math
import random
import time
import os
import shutil

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
print()

#Functions
print("Functions:")

def happy_birthday(nom,age):
    print(f"Happy birthday {nom}!")
    print(f"You are {age} years old.")

happy_birthday(name,20)
print() 

def display_invoice(username, amount, due_date):
    print(f"Hello {username},")
    print(f"Your invoice of ${amount:.2f} is due on {due_date}.")
    print("Thank you for your business.")

display_invoice("John", 100.00, "01/01/2022")
print()

def add(x,y,z):
    res = x+y+z
    return res 
    #return x+y+z

xyz = add(1,2,3)
print(f"xyz={xyz}")
print()

#default arguments
print("Default arguments:")
def add(x=0,y=0,z=0):
    res = x+y+z
    return res

xyz = add(1,2)
print(f"xyz={xyz}")
print()

"""def count(end,start=1):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Done!")"""
#count(5)

#keyword arguments
print("Keyword arguments:")
def hello(greeting, title, first, last):
    print(f"{greeting}, {title} {first} {last}.")
    print()

hello(title="Mr",first="John",greeting="Hello",last="Smith")
print()

#arbitrary arguments
print("Arbitrary arguments:")
def add(*args):
    res = 0
    for i in args:
        res += i
    return res

print(add(1,2,3,4,5,6,7,8,9,10))
print()

#arbitrary keyword arguments
print("Arbitrary keyword arguments:")
def hello(**kwargs):
    print(f"Hello {kwargs['title']} {kwargs['first']} {kwargs['last']}.")
    for value in kwargs.values():
        print(value)
    print()

hello(first="John",title="Mr",last="Smith")
print()

#modules
print("Modules:")
import FirstModule

print(FirstModule.pi)
print(FirstModule.square(5))
print()

#exception handling
print("Exception handling:")
try:
    #result = 10/0
    #result = 10/"pizza"
    result = 10/2
except ZeroDivisionError as e:
    print("Can't divide by zero.")
except TypeError as e:
    print("Can't divide by a string.")
except Exception as e:
    print("Something went wrong.")
else:
    print(result)
finally:
    print("Always executed.")
print()

#file detection
print("Files:")
path = "PythonRefreshing\\4-Files"

if os.path.exists(path):
    print("Location exists.")
    if os.path.isfile(path):
        print("There is a file.")
    elif os.path.isdir(path):
        print("There is a directory.")
else:
    print("Location does not exist.")
print()

#file reading
print("File reading:")
path = "PythonRefreshing\\4-Files\\Test.txt"
try:
    with open(path,"r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print("Something went wrong.")
print()

#file writing
print("File writing:")
path = "PythonRefreshing\\4-Files\\TestAgain.txt"
try:
    with open(path,"a") as file:
        file.write("Hello World!")
        file.write("\n")
except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print("Something went wrong.")
#Rading changes
try:
    with open(path,"r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print("Something went wrong.")
print()

#Copying files with shutil
print("Copying files:")
#copyfile = copies the contents of the file, no appending
#copy = copies the file and permissions
#copy2 = copies the file and metadata

path = "PythonRefreshing\\4-Files\\TestAgain.txt"
shutil.copyfile(path,"PythonRefreshing\\4-Files\\TestAgain2.txt")

try:
    with open("PythonRefreshing\\4-Files\\TestAgain2.txt","r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print("Something went wrong.")
print()

#Move files
print("Moving files:")
source = "PythonRefreshing\\4-Files\\TestAgain2.txt"
destination = "PythonRefreshing\\2-GeneralStuff\\TestAgain2.txt"

try:
    if os.path.exists(destination):
        print("File already exists.")
    else:
        os.replace(source,destination)
        #shutil.move(source,destination)
        print("File moved.")
except Exception as e:
    print("Something went wrong.")
print()

#Delete files
print("Deleting files:")

try:
    os.remove(destination)
    #os.rmdir("PythonRefreshing\\4-Files\\TestAgain2.txt") #removes the directory
    #shutil.rmtree("PythonRefreshing\\4-Files\\TestAgain2.txt") #removes the directory and all its contents
    print("File deleted.")
except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print("Something went wrong.")
print()

#Classes
from cars import Car
print("Classes:")
car_1 = Car("Ford","Mustang",1969,"red")
car_2 = Car("Porsche","911",2021,"blue")

print(car_1.make+" "+car_1.model)
car_1.drive()
print()

#Inheritance
from Animals import Animal, Fish, Hawk, Rabbit
print("Inheritance:")
animal_1= Hawk()
animal_2= Rabbit()
animal_1.eat()
animal_2.run()
print()

#Multilevel inheritance
from MultyInheritance import Dog
print("Multilevel inheritance:")
dog_1 = Dog()
dog_1.eat()
dog_1.bark()
print()

#Multiple inheritance
print("Multiple inheritance:")
animal_1.hunt()
animal_3 = Fish()
animal_3.flee()
animal_3.hunt()
