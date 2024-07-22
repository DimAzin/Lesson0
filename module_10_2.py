import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            day_enemies = enemies - self.power
            if day_enemies < 0:
                enemies = 0
            else:
                enemies = day_enemies
            print(f"{self.name} сражается {days} дней, осталось {enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней!")


knight1 = Knight("Рыцарь 1", 10)
knight2 = Knight("Рыцарь 2", 15)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Битва окончена!")
