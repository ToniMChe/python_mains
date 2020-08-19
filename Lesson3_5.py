def sum_of_numbers(numbers, word):
    summation = 0
    for el in numbers:
        if el == word:
            break
        summation = summation + float(el)
    return summation


total_sum = 0
stop_word = "stop"

print("""Чтоб остановиться введите stop.
Если хотите остановиться после текущей строки, введите стоп после цифр.""")

while True:
    user_numbers = input("Введите ряд чисел: ").split(" ")
    total_sum = total_sum + sum_of_numbers(user_numbers, stop_word)

    print("Сумма: {}".format(total_sum))
    if stop_word in user_numbers:
        break
