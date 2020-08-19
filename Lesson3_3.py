def my_func(a, b, c):
    if b > a and c > a:
        summation = b + c
    elif c > b and a > b:
        summation = c + a
    else:
        summation = a + b
    return summation


first_number = int(input("Введите число 1: "))
second_number = int(input("Введите число 2: "))
third_number = int(input("Введите число 3: "))

user_summation = my_func(first_number, second_number, third_number)
print("сумма двух больших чисел: {}".format(user_summation))
