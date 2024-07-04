
def personal_sum(numbers):
    """
    numbers: коллекция чисел
    return: кортеж (result, incorrect_data)
    """
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    """
    numbers: коллекция чисел
    return: среднее арифметическое всех чисел, либо None при ошибке
    """
    result = None
    try:
        total, error_count = personal_sum(numbers)
        count = len(numbers) - error_count
        if count == 0:
            return 0
        result = total / count
        if error_count > 0:
            raise TypeError
        return result

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return result



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать