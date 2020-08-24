def my_func(x, y):
    x_in_degree = x ** y
    return x_in_degree


number = int(input("Введите действительное положительное число: "))
degree = int(input("Введите целое отрицательное число: "))

result = my_func(number, degree)

print("{} в степени {} = {}".format(number, degree, result))
