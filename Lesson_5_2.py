from pathlib import Path

file_path = Path(__file__).parent.joinpath('Lesson5_2')
counter_words = 0
counter_lines = 0

with open(file_path, 'rt', encoding='UTF-8') as file:
    file_lines = file.readlines()
    for element in file_lines:
        counter_lines += 1
        words_in_line = 0
        chain = 0
        if element != "\n":
            for elem in element:
                if elem != " " and chain == 0:
                    counter_words += 1
                    chain = 1
                elif elem == " ":
                    chain = 0

counter_lines += 1

print("Количество строк: {}".format(counter_lines))
print("Количество слов: {}".format(counter_words))
