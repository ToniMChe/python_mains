seasons = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}

month_number = int(input("Введите номер месяца: "))

for key, item in seasons.items():
    if month_number in item:
        print(key)
