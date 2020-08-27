from pathlib import Path

new_lines = []
translation = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

file_path1 = Path(__file__).parent.joinpath('Lesson5_4_1.txt')
file_path2 = Path(__file__).parent.joinpath('Lesson5_4_2.txt')

with open(file_path1, 'r', encoding='UTF-8') as file:
    path1_data = file.readlines()
    for new_line in path1_data:
        for key, volume in translation.items():
            new_line = new_line.lower().replace(key, volume.title())
        new_lines.append(new_line)

print(new_lines)

with open(file_path2, 'w', encoding='UTF-8') as file:
    file.writelines(line for line in new_lines)
