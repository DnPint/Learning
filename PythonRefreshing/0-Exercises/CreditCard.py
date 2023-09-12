
sum_odd_digits = 0
sum_even_digits = 0
total = 0

credit_number = input("Enter a credit card number: ")
credit_number = credit_number.replace("-","")
credit_number = credit_number.replace(" ","")
credit_number = credit_number[::-1]

if credit_number.isnumeric() == False:
    print("This is not a valid credit card number, must not be giberish.")
    exit()

for x in credit_number[::2]:
    sum_odd_digits += int(x)

for x in credit_number[1::2]:
    x=int(x)*2
    if x > 9:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("This is a valid credit card number.")
else:
    print("This is not a valid credit card number.")
