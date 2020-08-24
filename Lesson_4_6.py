import itertools
from sys import argv

first_number = int(argv[1])
last_number = 10
input_numbers = [1, 2, 3, 4, 5]
replay = 0

for number in itertools.count(first_number):
    if number == last_number:
        break
    else:
        print(number)

print('')

for number in itertools.cycle(input_numbers):
    if replay > 4:
        break
    print(number)
    replay = replay + 1
