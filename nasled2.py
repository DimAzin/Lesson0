# Создайте родительский(базовый) класс Vehicle,
# который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car,
# который имеет свойство price = 1000000 и
# функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan
# и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle():

    def __init__(self):
        self.vehicle_type = None

class Car():

    def __init__(self, powers):
        self.price = 1000000
        self.powers = powers

    def horse_powers(self):
        return self.powers

class Nissan(Car, Vehicle):

    def __init__(self, powers):
        super().__init__(powers)
        self.price = 2000000
        self.vehicle_type = None

    def horse_powers(self):
        print("power Nissan")
        return self.powers



car1 = Nissan(300)

print(car1.horse_powers(), car1.vehicle_type, car1.price)
