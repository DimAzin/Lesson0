# На числовой прямой даны два отрезка: [𝑎1; 𝑏1] и[𝑎2; 𝑏2].
# Напишите программу, которая находит их пересечение.
#
# Гарантируется, что 𝑎1 < 𝑏1 и 𝑎2 < 𝑏2.
# Пересечением двух отрезков может быть.:
# •отрезок;
# •точка;
# •пустое множество.
#
# a, b, c, d = 1, 3, 2, 4 result — > 2 3
# a, b, c, d = 1, 2, 3, 4 result — > пустое множество

def get_otrezki():
    result = None
    list_values = [['*', '*'], ['*', '*']]
    for i in(1, 2):
        print(f'Введите 2 числа для отрезка {i}')
        a = int(input('Начало: '))
        b = int(input('Конец: '))
        list_values[i-1][0] = a
        list_values[i-1][1] = b
    result = list_values
    return result


otrezki = get_otrezki()
print(f'Вычисляю пересечение для отрезков: {otrezki}')

a1 = otrezki[0][0]
b1 = otrezki[0][1]
a2 = otrezki[1][0]
b2 = otrezki[1][1]

outcome = ''
if a1 > b2 or a2 > b1:
    outcome = 'Пустое множество'
elif a1 == b2:
    outcome = 'Точка: '+ a1
elif a2 == b1:
    outcome = 'Точка: '+ a2
elif a1 < a2 and a2 < b1:
    outcome = f'Отрезок: {a2}, {min(b1, b2)}'
elif a2 < a1 and a1 < b2:
    outcome = f'Отрезок: {a1}, {min(b1, b2)}'


print(outcome)