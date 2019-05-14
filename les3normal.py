def zadacha (list1, list2):
    i = dict(zip(list1, list2))
    file = open('salary.txt', 'a+', encoding='utf-8')
    file.seek(0)
    for keys, value in i.items():
        file.write(f'{keys.upper()} - {value}\n')
        if value < 500000.0:
            print(f'{keys} {value}')
    file.close()

a = ["Ivan1", "Ivan2", "Ivan3", "Ivan4"]
b = [345000.0, 123000.0, 650000.0, 78900.0]
zadacha(a,b)


