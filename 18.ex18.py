#this one is like argv and scripts
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1 is {arg1} and arg2 is {arg2}')

#ok that *args is pointless we could have do this
def print_two_again(arg1, arg2):
    print('using .format arg1 is {} and arg2 is {}'.format(arg1, arg2))

#this takes one argument
def take_one(arg1):
    print(f'this is the one argument {arg1}')

#this takes no arguments
def take_none():
    print('i have nothing in this func')


print_two('Georgi', 'Kolev')
print_two_again('Yoneli', "Kitten")
take_one("Python for big data and hadoop")
take_none()