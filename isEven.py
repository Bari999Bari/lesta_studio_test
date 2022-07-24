import timeit


# ваш алгоритм самый очевидный, который я всегда использовал
def isEven(number: int):
    return number % 2 == 0  # неизвестно что внутри логики этого оператора и как быстро он работает


# много что наверное можно сделать костыльно, но это первое что пришло в голову
def myIsEven(value: str):
    check_symbs = ['0', '2', '4', '6', '8']  # тратим немного памяти на создание массива,
    # но так как это происходит один раз некритично
    return value[-1] in check_symbs  # достаем последний символ за O(1)


num = input('Введите число ')
num_2 = int(num)  # преобразуем заранее чтобы время на эту операцию не учитывалось при оценке скорости

start_time = timeit.default_timer()
for i in range(100000):
    isEven(num_2)
time_1 = timeit.default_timer() - start_time
print('Ваша функция', time_1)

start_time = timeit.default_timer()
for x in range(100000):
    myIsEven(num)
time_2 = timeit.default_timer() - start_time
print('Моя функция', time_2)

if time_1 <= time_2:
    print('Победила классика!')
else:
    print('Победил авангардизм!')