from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'copying {from_file} to {to_file}')

#print in one line
in_file = open(from_file); in_data = in_file.read()

print(f'the input file is {len(in_data)} bytes long')

print(f'does the output file {exists(to_file)} exist?')
print('ready to work, enter continue ctrl-c exit')
input()

out_file = open(to_file, 'w'); out_file.write(in_data)

print("alright, all done")

out_file.close()
in_file.close()