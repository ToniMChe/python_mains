swap = []

len_of_array = int(input("Введите длину массива: "))

for index in range(len_of_array):
    element_of_swap = input("Введите элемент массива: ")
    swap.append(element_of_swap)

for index in range(0, len_of_array - 1, 2):
    swap[index], swap[index + 1] = swap[index + 1], swap[index]

print("Итоговый массив: {}".format(swap))
