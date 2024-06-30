class InvalidDataException(Exception):
    """Исключение, возникающее при недопустимых данных"""
    pass


class ProcessingException(Exception):
    """Исключение, возникающее при ошибках в процессе обработки"""
    pass

def generate_exceptions(data):
    if not isinstance(data, str):
        raise InvalidDataException("Данные должны быть строкой!")
    if len(data) == 0:
        raise InvalidDataException("Данные не должны быть пустыми!")
    if data == "Ошибка процедуры обработки":
        raise ProcessingException("Ошибка обработки данных!")

    return f"Данные '{data}' обработаны успешно."


# Функция, вызывающая generate_exceptions и обрабатывающая исключения
def process_data(data):
    try:
        result = generate_exceptions(data)
        return result
    except InvalidDataException as e:
        print(f"Возникло исключение InvalidDataException: {e}")
        raise
    except ProcessingException as e:
        print(f"Возникло исключение ProcessingException: {e}")
        raise



test_data = ["Корректные данные", 42, "", "Ошибка процедуры обработки"]
print(f'Тестовые данные: {test_data}')
for data in test_data:
    try:
        result = process_data(data)
        print(result)
    except Exception as e:
        print(f"Обработка исключения: {e}")




