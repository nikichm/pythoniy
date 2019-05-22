import easy5
import os
def change_dir (path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))

def start ():
    answer =''
    while answer != '5':
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть файлы в текущей папке\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer =='5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(change_dir(path_name))
        elif answer == '2':
            easy5.file_name()
        elif answer == '3':
            easy5.es2_del()
        elif answer == '4':
            easy5.es1_create()

