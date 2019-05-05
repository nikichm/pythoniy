import math
import random

my_list = [-6, -9, 0, 81, -16, 4, 0.5, 25]
new_list = []
for element in my_list:
    if (element > 0) and (int(math.sqrt(element)) == math.sqrt(element)):
        new_list.append(int(math.sqrt(element)))
print(new_list)


dana_data = '01.01.2000'
data_list = dana_data.split('.')
dict_months = {
'01': 'января',
'02': 'феврал',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря',
}
dict_days = {
'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
'06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
'11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
}
for key in dict_days:
    if data_list[0] == key:
        data_list[0] = dict_days[key]

for key in dict_months:
    if data_list[1] == key:
        data_list[1] = dict_months[key]

answer_data = data_list[0] + ' ' + data_list[1] + ' ' + data_list[2] + ' ' "года"
print(answer_data)


n = int(input('введите количество случайных элементов в списке: '))
my_list = []
i = 0
while  i < n:
    my_list.append(random.randint(-100, 100))
    i += 1
print(my_list)


my_list = [1, 2, 3, 4, 5, 5, 4, 5, 6, 7, 8, 10, 10, -1, -2, -1]
new_list = set(my_list)
print(new_list)

list = []
for op in my_list:
    if my_list.count(op) == 1:
        list.append(op)
print(list)


