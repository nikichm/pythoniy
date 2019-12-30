import random




def sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


array = [random.randint(-100, 99) for i in range(10)]
print(array)
sort(array)
print(array)
