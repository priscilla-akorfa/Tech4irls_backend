# The SWhile loop

current_number = 0

"""while current_number <= 10:
    if current_number == 5:
       print('Skipping 5')
       current_number += 1
       continue
    else:
       print(current_number)
       current_number += 1"""
"""while True:
    print(current_number)
    current_number += 1"""

prompt = "Tell me something and I will repeat it back to you\n It can be your name or anything you like\n Type 'quit' when you are done: " 

"""while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(f'Your message was: {message}')"""
# OR

"""message = ""
while message != 'quit': 
    message = input(prompt)
    if message != 'quit':
        print(f'Your message was: {message}')"""

prompt = "Please add your prefered pizza toppings\n Type quit when you are done: "
while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(f'the {message} will be added to your pzza')