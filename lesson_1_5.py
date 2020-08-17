revenue = int(input("Введите выручку "))
costs = int(input("Введите издержки "))

if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print("у вас прибыль, рентабельность выручки {}".format(profitability))
    workers = int(input("введите кол-во ваших работников "))
    profit_to_workers = profit / workers
    print("прибыль в расчете на одного сотрудника {} ".format(profit_to_workers))
else:
    print("У вас убытки")
