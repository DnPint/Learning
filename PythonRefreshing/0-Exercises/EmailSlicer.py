
email = input("Enter your email: ")

index = email.find("@")

username = email[:index]
domain = email[index+1:]

if index == -1:
    print("Invalid email.")
else:
    print(f"Your username is {username} and your domain is {domain}.")

