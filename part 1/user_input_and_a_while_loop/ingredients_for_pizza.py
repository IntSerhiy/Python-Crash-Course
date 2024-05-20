prompt = "Enter the pizza ingredients you want to add."
prompt += "\nIf you want to finish adding ingredients, write 'quit'. "
massage = ""

while massage != 'quit':
    massage = input(prompt)

    if massage != 'quit':
        print(f"Add {massage}")
