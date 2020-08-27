import sys

if len(sys.argv) == 4:
    output_per_hour, bid_per_hour, prize = map(int, sys.argv[1:])
    salary = (output_per_hour * bid_per_hour) + prize

    print("Заработная плата содрудника: {}".format(salary))
else:
    print("Введите выработка в час, ставку в час, премию.")
