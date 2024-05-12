current_users = ['aleks', 'gordon', 'leo', 'silver23', 'vany']
new_users = ['sergio', 'gordon', 'dragon', 'leo', 'silver23']

for user in new_users:
    if user.lower() in current_users:
        print("This name is already taken, so choose another one.")
    else:
        print(f"Вітаю {user.title()}, ви успішно зареєстровані!")