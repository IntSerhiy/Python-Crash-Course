# massage = input("Tell me something, and I will repeat it back to you: ")
# print(massage)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# massage = ""
# while massage != 'quit':
#     massage = input(prompt)
#
#     if massage != 'quit':
#         print(massage)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    massage = input(prompt)

    if massage == 'quit':
        active = False
    else:
        print(massage)