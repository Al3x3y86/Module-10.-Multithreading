import threading
import time

def printnumbers():
    for number in range(1, 11):
        print(f'Поток 1 запущен {number}')
        time.sleep(1)

def printletters():
    for letter in 'abcdefghij':
        print(f'Поток 2 запущен {letter}')
        time.sleep(1)

thread1 = threading.Thread(target=printnumbers)
thread2 = threading.Thread(target=printletters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Оба потока завершены")