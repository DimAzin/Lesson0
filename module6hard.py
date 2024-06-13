# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированы и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод set_sides принимает неограниченное кол-во сторон, проверяет корректность переданных данных, если данные корректны, то меняет __sides на новый список, если нет, то оставляет прежние.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод __len__ должен возвращать периметр фигуры.
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Figure: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
# Метод get_square возращает площадь треугольника.
# Атрибуты класса Figure: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
#
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]


import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides
    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = sides

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self):
        return sum(self.__sides)

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides[0] \
            if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False
        self.__radius = self.__sides / (2 * math.pi)

    def __is_valid_sides(self, *sides):
        return len(sides) >= self.sides_count and isinstance(sides[0], int) and sides[0] > 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        s = len(self) / 2
        self.__height = 2 * math.sqrt(s * (s - self._Figure__sides[0]) *
                                      (s - self._Figure__sides[1]) * (s - self._Figure__sides[2])) / self._Figure__sides[0]

    def get_square(self):
        s = len(self) / 2
        return math.sqrt(s * (s - self._Figure__sides[0]) *
                         (s - self._Figure__sides[1]) * (s - self._Figure__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * 12
        super().__init__(color, *sides)
        self.__side_length = self._Figure__sides[0]

    def get_volume(self):
        return self.__side_length ** 3

# Примеры создания объектов для проверки:
circle = Circle((200, 200, 100), 10, 15, 6)
print(circle.get_color())

triangle = Triangle((200, 200, 100), 10, 6)
print(triangle.get_color())

cube = Cube((200, 200, 100), 9)
print(cube.get_color())

cube_invalid = Cube((200, 200, 100), 9, 12)
print(cube_invalid.get_color())


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())