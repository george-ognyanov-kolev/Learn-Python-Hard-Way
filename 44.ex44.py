#inheritance vs composition

print('1. Actions on the child imply an action on the parent.\n')

class Parent1(object):
    
    def implicit(self):
        print('PARENT implicit()')

class Child1(Parent1):
    pass

dad1 = Parent1()
son1 = Child1()

dad1.implicit()
son1.implicit()

print('2. Actions on the child override the action on the parent.\n')

class Parent2(object):
    
    def override(self):
        print('PARENT override()')

class Child2(Parent2):
    def override(self):
        print('CHILD override()')

dad2 = Parent2()
son2 = Child2()

dad2.override()
son2.override()


print('3. Actions on the child alter the action on the parent.\n')


class Parent3(object):

    def altered(self):
        print('PARENT3 altered()')

class Child3(Parent3):

    def altered(self):
        print('CHILD BEFORE PARENT altered()')
        super(Child3, self).altered()
        print('CHILD AFTER altered()')

dad3 = Parent3()
son3 = Child3()

dad3.altered()
son3.altered()
