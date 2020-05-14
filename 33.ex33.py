i = 0
numbers = []

while i<6:
    print(f"at the top i is {i} \n")
    numbers.append(i)

    i += 1
    print('numbers row: ', numbers)
    print(f'at the bottom i is {i} \n')

print('the numbers: ')

for num in numbers:
    print(num)