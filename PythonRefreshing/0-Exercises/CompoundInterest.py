

principle = 0
rate = 0
years = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("The principal amount must be positive.")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("The rate must be positive.")

while years <= 0:
    years = int(input("Enter the number of years (only whole years): "))
    if years <= 0:
        print("The number of years must be positive.")

print()
print()
print(f"Principle amount: {principle}")
print(f"Interest rate: {rate}")
print(f"Number of years: {years}")

total = principle * (1 + rate/100)**years
print(f"Balance after {years} years: CHF {round(total,2)}")