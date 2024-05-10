guests = ['сергій жадан', 'василь стус', 'в\'ячеслав чорновіл']

print(f"{guests[0].title()} запрошую вас до себе на вечерю!")
print(f"{guests[1].title()} запрошую вас до себе на вечерю!")
print(f"{guests[2].title()} запрошую вас до себе на вечерю!")

print("")
print(f"{guests[-1].title()} не зможе прийти на вечерю.")
guests[-1] = 'ліна костенко'

print("")
print(f"{guests[0].title()} запрошую вас до себе на вечерю!")
print(f"{guests[1].title()} запрошую вас до себе на вечерю!")
print(f"{guests[2].title()} запрошую вас до себе на вечерю!")

print("")
print("Дорогі друзі! Я знайшов більший стіл, ому зможу запросити більше гостей.")

guests.insert(0, 'микола хвильовий')
guests.insert(3, 'сергій параджанов')
guests.append('василь симоненко')

print("")
print(f"{guests[0].title()} запрошую вас до себе на вечерю!")
print(f"{guests[1].title()} запрошую вас до себе на вечерю!")
print(f"{guests[2].title()} запрошую вас до себе на вечерю!")
print(f"{guests[3].title()} запрошую вас до себе на вечерю!")
print(f"{guests[4].title()} запрошую вас до себе на вечерю!")
print(f"{guests[-1].title()} запрошую вас до себе на вечерю!")

print("")
print("Дорогі друзі! В мене є прикра новина, що мені не встигнуть доставити вчасно стіл, тому я зможу запросити лише двох гостей"
      "")
print("")
dell_guest = guests.pop()
print(f"{dell_guest.title()}, мені шкода, але я не зможу тебе запросити.")
dell_guest = guests.pop()
print(f"{dell_guest.title()}, мені шкода, але я не зможу тебе запросити.")
dell_guest = guests.pop()
print(f"{dell_guest.title()}, мені шкода, але я не зможу тебе запросити.")
dell_guest = guests.pop()
print(f"{dell_guest.title()}, мені шкода, але я не зможу тебе запросити.")

print(f"\n{guests[0].title()} ви вже ще запрошені.")
print(f"{guests[1].title()} ви вже ще запрошені.")

del guests[0]
del guests[0]
print(guests)