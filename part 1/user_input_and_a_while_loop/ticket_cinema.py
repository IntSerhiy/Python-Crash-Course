prompt = "Enter your age to find out the ticket price."
prompt += "\nIf you want to quit, type 'quit'. "

while True:
    age = int(input(prompt))


    if age == 'quit':
        break
    elif age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print(f"\nThe price of the ticket is {price}$")