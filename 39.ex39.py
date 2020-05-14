#create a mapping of states to abbreviation
states = {'Oregon':'OR', 'Florida':"FL", 'California':'CA', 'New York':'NY', 'Michigan':'MI'}

#create a basic set of states and some cities in them
cities = {'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print('NY state has', cities['NY'])
print('OR state has', cities['OR'])

#print some more states
print('-' * 10)
print('Michigans abbreviation is: ', states['Michigan'])
print('Floridas abbreviation is: ', states['Florida'])

#do it by using the state and then cities
print('#do it by using the state and then cities')
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city} in it')

#now do both at the same time
print('#now do both at the same time')
for state, abbrev in list(states.items()):
    print(f'{state} state is abbreviated {abbrev}')
    print(f'and has city {cities[abbrev]}')

print('-' * 10)
state = states.get('Texas')

if not state:
    print('sorry no Texas')

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f'the city for state "TX" is: {city}')