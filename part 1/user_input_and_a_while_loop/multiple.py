number = input("Enter a number and I'll tell you if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10")