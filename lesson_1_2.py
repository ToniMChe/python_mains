seconds = int(input('Введите время в секундах: '))

time_hour = seconds // 3600
time_minute = seconds % 3600 // 60
time_second = seconds - (time_minute * 60 + time_hour * 3600)

print("Время: "f'{time_hour:02}:{time_minute:02}:{time_second:02}')
