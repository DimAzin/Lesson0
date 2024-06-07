# Создайте родительский(базовый) класс Car,
# который имеет свойство price = 1000000
# и метод def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car
# - класс Nissan и переопределите свойство price, а также переопределите метод horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car
# и переопределите также свойство price,
# а также переопределите метод horse_powers

class Car():
    price = 1000000

    def __init__(self, powers):
        self.powers = powers

    def horse_powers(self):
        return self.powers

class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        print("power Nissan")
        return self.powers

class Kia(Car):
    price = 1500000

    def horse_powers(self):
        print("power Kia")
        return self.powers

car1 = Car(150)
car2 = Nissan(300)
car3 = Kia(250)

print(car1.horse_powers())
print(car2.horse_powers())
print(car3.horse_powers())
