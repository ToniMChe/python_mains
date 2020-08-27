from pathlib import Path

file_path = Path(__file__).parent.joinpath('Lesson5_3')
salary_under_twenty = 20

print("Зарплата меньше 20 тыс.: ")

with open(file_path, 'r', encoding='UTF-8') as file:
    workers_data = file.readlines()
    for line in workers_data:
        key, item = line.split("-")
        item = int(item[:2])
        if item < salary_under_twenty:
            print(key)
