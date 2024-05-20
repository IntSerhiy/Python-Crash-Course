favorite_places = {
    'sergiy': ['lviv', 'home'],
    'svyatoslav': ['leshniv'],
    'lesya': ['nyklovichi', 'lviv', 'house']
    }

for name, places in favorite_places.items():
    if 1 <= len(places):
        print(f"{name.title()} favorite places are:")
        for place in places:
            print("\t" + place.title())
        print("")
    else:
        print(f"{name.title()} favorite place is:")
        print("\t" + places[0].title() + "\n")