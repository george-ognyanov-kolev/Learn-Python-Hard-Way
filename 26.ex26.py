#Sorting and fixing someone else's code
#Mark the errors with comments the line above the error

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
#Missing closing parenthesis
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filenme)

print("Here's your file {filename}:")
print(tx.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again_read())

#Missing backwards slash to escape the apostrophe
print('Let\'s practice everything.')
#Print statement was on two lines 
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#Missing " in the end of print statement
print("--------------")
print(poem)
#Missing " at the beginning of print statement"
print("--------------")

#Missing a digit
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}"

#Missing : after the def statement



def secret_formula(started):

    jelly_beans = started*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs
    print("People are less than or equal to dogs.)


if people = dogs:
    print("People are dogs.")
