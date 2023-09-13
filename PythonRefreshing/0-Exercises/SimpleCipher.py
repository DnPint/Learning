import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

message = input("Enter a message: ")
cipher = ""

for letter in message:
    if letter in chars:
        cipher += key[chars.index(letter)]
    else:
        cipher += letter

print(cipher)

cipher = input("Enter the cipher: ")
message = ""

for letter in cipher:
    if letter in key:
        message += chars[key.index(letter)]
    else:
        message += letter

print(message)