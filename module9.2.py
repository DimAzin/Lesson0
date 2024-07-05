# Фабрика функций
def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            return x / y if y != 0 else None
        return divide
    elif operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract

my_func_multiply = create_operation("multiply")
print(my_func_multiply(3, 4))

my_func_divide = create_operation("divide")
print(my_func_divide(10, 2))
print(my_func_divide(10, 0))

my_func_add = create_operation("add")
print(my_func_add(25, 7))

my_func_subtract = create_operation("subtract")
print(my_func_subtract(17, 3))

# Лямбда
square_lambda = lambda x: x ** 2
print(square_lambda(5))  # Выводит 25

# Аналог def
def square_def(x):
    return x ** 2
print(square_def(5))  # Выводит 25

# class
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

rect = Rect(4, 5)
print(rect())
