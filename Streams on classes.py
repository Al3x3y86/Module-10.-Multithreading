import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)  # 1 секунда = 1 день
            days += 1
            enemies -= self.skill
            if enemies < 0:
                enemies = 0
            print(f"{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней!")

knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Все битвы закончились!")
