

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be longer than 12 characters.")
#elif not username.find(" ") == -1:
    #print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username can't contain numbers or spaces.")
else:
    print(f"Hello {username}!")