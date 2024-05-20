sandwich_orders = ['blt', 'club', 'grilled cheese', 'peanut butter', 'tuna salad']
finished_sandwiches = []

while sandwich_orders:
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