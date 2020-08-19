def data(name, surname, year, town, email, phone):
    print("""    имя: {}
    фамилия: {}
    год рождения: {}
    родной город: {}
    email: {}
    телефон: {}""".format(name, surname, year, town, email, phone))


user_name = input("имя: ")
user_surname = input("фамилия: ")
user_year = input("год рождения: ")
user_town = input("гогрод проживания: ")
user_email = input("email: ")
user_phone = input("телефон: ")

data(user_name, user_surname, user_year, user_town, user_email, user_phone)
