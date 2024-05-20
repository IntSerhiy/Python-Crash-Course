sandwich_orders = ['blt', 'pastarmi', 'club', 'grilled cheese', 'pastarmi', 'peanut butter', 'tuna salad', 'pastarmi']
finished_sandwiches = []

while sandwich_orders:
    print("Our cafe has run out of pastormi, because of this we will not be able to prepare pastormi sandwiches\n")
    while 'pastarmi' in sandwich_orders:
        sandwich_orders.remove('pastarmi')



    sandwich = sandwich_orders.pop()

    if sandwich == 'blt':
        print(f"I made your {sandwich.upper()} sandwich.")
    else:
        print(f"I made your {sandwich.title()} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nReady sandwiches:")
for sandwich in finished_sandwiches:
    if sandwich == 'blt':
        print("\t" + sandwich.upper())
    else:
        print("\t" + sandwich.title())