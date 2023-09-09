#Imprts
import math

#Variables
age = 25
name = "John"
online=True
note = 5.5
Student = True

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
print(math.sqrt(9)) #returns the square root of 9
