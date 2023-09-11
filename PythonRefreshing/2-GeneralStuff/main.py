#Imprts
import math

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
while response == "":
    response = input("Enter something: ")
print(f"You entered {response}.")

for i in range(0,3):
    print(i)

print()



