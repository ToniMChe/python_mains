quantity = int(input("Введите количество наименований товаров: "))
goods = []

for index in range(1, quantity + 1):
    print()
    print("Характеристики товара №{}:".format(index))
    name_of_goods = input("Название: ")
    price_of_goods = input("Цена: ")
    count_of_goods = input("Количество: ")
    measure_of_goods = input("Единица измерения: ")

    chars = {"название": name_of_goods,
             "цена": price_of_goods,
             "количество": count_of_goods,
             "ед": measure_of_goods
             }

    goods.append((index, chars))

print(goods)

analytics = {}

for element in goods:
    chars = element[1]

    for key, item in chars.items():
        current_analytic = analytics.get(key)
        if current_analytic is None:
            analytics[key] = []
        analytics[key].append(item)

print(analytics)
