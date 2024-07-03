# является ли число нечётным
def is_odd(number):
    return number % 2 != 0

# квадрат числа
def square(number):
    return number ** 2


input_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Применение функций map и filter
result = list(map(square, filter(is_odd, input_list)))


print(result)
