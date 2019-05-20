# # Задача-1 измененная под normal
import os
import shutil

def es1_create(x) :
    x = input("Введите название папки ")
    i = 0
    while i+1 < 2:
        os.mkdir(x)
        i+=1

def es2_del(x):
    x = input("Введите название папки ")
    i = 0
    while i + 1 < 2:
        os.rmdir(x)
        i += 1

if __name__ == '__main__':
    es1_create(10)
    es2_del(10)

# Задача-2
def file_name ():
    a = input("Введите название папки ")
    f = []
    for (dirpath, dirnames, filenames) in os.walk(a):
        f.extend(filenames)
        print(f)
        break

if __name__ == '__main__':
    file_name()


# Задача-3
def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    current_file_copy()
