import math

# Про данный вид сортировки
# я знаю из книги, которую недавно прочел
# работает за O(n*log(n)), что довольно быстро

def merging(left, right):
    """Объединение двух отсортированных списков в один."""
    new = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            to_insert = right.pop(0)
            new.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            new.append(to_insert)
    if len(left) > 0:
        for i in left:
            new.append(i)
    if len(right) > 0:
        for i in right:
            new.append(i)
    return new


def mergesort(data):
    """Рекурсивная сортировка слиянием."""
    new = []
    if len(data) == 1:
        new = data
    else:
        left = mergesort(data[:math.floor(len(data) / 2)])
        right = mergesort(data[math.floor(len(data) / 2):])
        new = merging(left, right)
    return new
