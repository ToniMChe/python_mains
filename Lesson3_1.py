def division(x, y):
    return x / y


first_number = float(input("Введите первое число: "))
second_number = 0

while second_number == 0:
    second_number = float(input("Введите второе число: "))
    if second_number == 0:
        print("Недьзя делить на ноль")

division_result = division(first_number, second_number)
print("Результат деления: {}".format(division_result))
