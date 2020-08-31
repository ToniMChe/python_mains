from pathlib import Path

file_path = Path(__file__).parent.joinpath('Lesson5_5')

with open(file_path, 'w', encoding='UTF-8') as file:
    user_data = input("Введите ряд чисел через пробел:")
    file.write(user_data)

with open(file_path, 'r', encoding='UTF-8') as file:
    user_numbers = file.readlines()
    user_numbers = user_numbers[0].split(" ")
    user_numbers = list(map(int, user_numbers))
    user_summation = sum(user_numbers)
    print(user_summation)
