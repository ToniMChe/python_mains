from functools import reduce

even_numbers = [number for number in range(100, 1001) if number % 2 == 0]

composition = reduce(lambda x, y: x*y, even_numbers)

print(composition)
