print('''you entered a dark room with two doors.
do you enter door 1 or door 2''')

door = input('>>> ')

if door == '1':
    print('there is a giant bear here eating a cheesecake')
    print('what do you do')
    print('1. take the cake')
    print('2. scream at the bear')

    bear = input('>>> ')

    if bear == '1':
        print('the bear fucked you up. good job')
    elif bear == '2':
        print('the bear eats your legs off. good job')
    else:
        print(f'well doing {bear} is probably better')
        print('bear runs away')

elif door == '2':
    print('you stare into the endless abyss of cthulu\'s eyes')
    print('1. blueberries')
    print('2. yellow jacket clothesspin')
    print('3. understanding revolvers ...')

    insanity = input('>>> ')

    if insanity == '1' or insanity == '2':
        print('your body survives power by a mind of jello')
        print('good job')
    else:
        print('the insanity kills you')
        print('good job')

else:
    print('you stumble around and die. good job')