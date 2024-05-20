people = {
    'yuriy': {
        'first': 'yuriy',
        'last': 'suryak',
        'location': 'dmitrovichi',
        },
    'svyato': {
        'first': 'svyatoslav',
        'last': 'dutka',
        'location': 'leshniv',
        },
    'aleks': {
        'first': 'oleksiy',
        'last': 'gruzevych',
        'location': 'busk'
        }
    }

for name, person_info in people.items():
    print(f"Username: {name}")
    full_name = f"{person_info['first']} {person_info['last']}"
    location = person_info['location']

    print(f"\tName and surname: {full_name.title()}")
    print(f"\tLocation: {location.title()}\n")