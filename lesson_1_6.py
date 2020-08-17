distance_a = float(input("Введите дистанцию за первый день "))
distance_b = float(input("Введите целевую дистанцию "))

day_number = 1
print("{0}-й день: {1}".format(day_number, distance_a))

while distance_a <= distance_b:
    day_number = day_number + 1
    distance_a = distance_a * 1.1
    distance_a = round(distance_a, 2)
    print("{0}-й день: {1}".format(day_number, distance_a))
