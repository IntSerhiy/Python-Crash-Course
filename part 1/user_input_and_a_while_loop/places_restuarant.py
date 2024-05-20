places = input("Enter how many seats you want to reserve a table for: ")
places = int(places)

if places >= 8:
    print("\nI'm sorry, but you will have to wait for a table.")
else:
    print("\nYour table is ready.")