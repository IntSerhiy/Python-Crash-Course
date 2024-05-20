pets = [
    {'owner': 'lesya', 'pet': 'russian cocker spaniel'},
    {'owner': 'vasyl', 'pet': 'scotland cat'},
]

for pet_info in pets:
    print(f"Owner name: {pet_info['owner'].title()}")
    print(f"Pet: {pet_info['pet'].title()}\n")