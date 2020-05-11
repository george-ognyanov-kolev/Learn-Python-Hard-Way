from sys import argv

script, user_name = argv
prompt = '>>>>>> '

print(f'Hello {user_name}, I am the {script}')
print('I\'d like to ask you a question')
print(f'do you like me {user_name}')
likes = input(prompt)

print(f'where do you live {user_name}')
lives = input(prompt)

print(f'what kind of computer do you have {user_name}')
computer = input(prompt)

print(f'''
alright so you said {likes} about liking me
you live in {lives}. not sure where that is
and you have a {computer} computer. nice
''')