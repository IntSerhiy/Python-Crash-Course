users = ['serhiy', 'jack', 'admin', 'maks', 'soul']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for loggin in again.")
else:
    print("We need to find some users!")


print("")
users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for loggin in again.")
else:
    print("We need to find some users!")