while True:
    user_number = int(input("Введите целое положительное число "))
    if user_number > 0:
        break

biggest_number = 0
current_number = user_number

while current_number > 0:
    digit_for_sample = current_number % 10
    if digit_for_sample > biggest_number:
        biggest_number = digit_for_sample
    current_number = current_number // 10

print("Самая большая цифра: {}".format(biggest_number))