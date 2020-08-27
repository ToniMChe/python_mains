from pathlib import Path

file_path = Path(__file__).parent.joinpath('Lesson5_1')

with open(file_path, 'a', encoding='UTF-8') as file:
    while True:
        user_data = input("Введите данные, для остановки ничего не вводите: ")
        if user_data == "":
            break
        file.write(user_data)
