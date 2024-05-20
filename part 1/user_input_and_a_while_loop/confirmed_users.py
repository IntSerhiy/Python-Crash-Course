unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()

    print(f"Verifying user: {user.title()}")
    confirmed_users.append(user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("\t" + confirmed_user.title())