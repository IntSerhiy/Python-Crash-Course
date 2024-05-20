places = {}

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    place = input("If you could only visit one place in the world, where would you go? ")
    if place == 'q':
        break

    places[name] = place

    print("If you want to end the survey, write 'q'\n")

print("Result poll:")
for name, place in places.items():
    print(f"{name} his dream train in the {place}")