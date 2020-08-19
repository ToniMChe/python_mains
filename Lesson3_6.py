def int_func(word):
    division_word = word
    division_word = division_word.title()
    return division_word


user_word = input("Введите слово: ")
user_word = str(user_word)
print(int_func(user_word))
