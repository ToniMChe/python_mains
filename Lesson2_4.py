message = input("Введите сообщение: ").split()

for index, element in enumerate(message):
    print("{}. {}".format(index + 1, element[:10]))
