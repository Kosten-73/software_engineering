# Пузырьковая сортировка
from random import randint


def sort_bubble(listik):
    for i in range(len(listik) - 1):
        for j in range(len(listik) - i - 1):
            if listik[j] > listik[j + 1]:
                temp = listik[j]
                listik[j] = listik[j + 1]
                listik[j + 1] = temp


mas = [randint(0, 1000) for now in range(100)]
print(f"Случайный массив => {mas}")
sort_bubble(mas)
print(f"Отсортированный массив => {mas}")
