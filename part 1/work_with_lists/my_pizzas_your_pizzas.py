my_pizzas = ['papperoni', 'cheese', 'hawaiian']
friend_pizzas = my_pizzas[:]

my_pizzas.append('meaty')
friend_pizzas.append('mushroom')

print("My favorite pizzas:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas:")
for pizza in friend_pizzas:
    print(pizza.title())