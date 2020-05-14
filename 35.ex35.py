from sys import exit

def gold_room():
    print('this room is full of gold. how much can you take')

    choice = input(">>> ")
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('man learn to type a number')

    if how_much < 50:
        print('nice u r not greedy')
        exit(0)
    else:
        dead('you gready bastard')


def bear_room():
    print('there is a bear in the room')
    print('the bear has a bunch of honey')
    print('the bear is in front of the other door')
    print('how are u going to move the bear')
    bear_moved = False

    while True:
        choice = input(">>> ")

        if choice == 'take honey':
            dead('bear slaps your face off')
        elif choice == 'taunt bear' and not bear_moved:
            print('the bear has moved from the door')
            print('you can go through now')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('the bear gets angry and shews your legs off')
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print('i got no idea what is going on')


def cthulu_room():
    print('here you see the great cthulu')
    print('he stares at u and u go insane')
    print('do u flee or eat you head')

    choice = input('>>> ')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('well that was nasty')
    else:
        cthulu_room()


def dead(why):
    print(why, 'good job')
    exit(0)

def start():
    print('you are in a dark room')
    print('there is a door to your right and left')
    print('which one do u take')

    choice = input('>>> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulu_room()
    else:
        dead("you stumble around the room until u starve")


start()