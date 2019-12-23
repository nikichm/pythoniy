# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий,чья прибыль выше среднего и ниже среднего.

factories = {}

sumsum = 0

ch = []

factories_summ = int(input('Введите количество предприятий: '))

for _ in range(factories_summ):

    Names = input('Введите название предприятия:')

    ch1 = int(input('Введите прибыль за 1-й квартал: '))
    ch.append(ch1)
    ch2 = int(input('Введите прибыль за 2-й квартал: '))
    ch.append(ch2)
    ch3 = int(input('Введите прибыль за 3-й квартал: '))
    ch.append(ch3)
    ch4 = int(input('Введите прибыль за 4-й квартал: '))
    ch.append(ch4)
    sum = (ch1 + ch2 + ch3 + ch4) / 4
    ch.append(sum)

    factories[Names] = ch.copy()

    sumsum += (sum)/factories_summ

    ch.clear()


for k,v in factories.items():
    if v[4] > sumsum :
        print(f'Прибыль имеет значение выше среднего у фирмы: {k}')
    elif v[4] == sumsum :
        print(f'Прибыль имеет  среднее значение  у фирмы: {k}')
    else :
        print(f'Прибыль имеет значение ниже среднего у фирмы: {k}')





print(sumsum)
