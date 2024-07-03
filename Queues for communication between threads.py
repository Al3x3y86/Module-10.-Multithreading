import threading
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables
        self.customer_count = 1

    def customer_arrival(self):
        while self.customer_count <= 20:
            self.serve_customer(self.customer_count)
            self.customer_count += 1
            time.sleep(1)  # Новый посетитель приходит каждую секунду

    def serve_customer(self, customer_id):
        print(f"Посетитель номер {customer_id} прибыл.")

        # Проверяем наличие свободных столов
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer_id} сел за стол {table.number}.")

                # Запускаем поток для обслуживания посетителя
                customer_thread = threading.Thread(target=self.serve_customer_thread, args=(customer_id, table))
                customer_thread.start()
                return

        # Если нет свободных столов, помещаем посетителя в очередь
        self.queue.append(customer_id)
        print(f"Посетитель номер {customer_id} ожидает свободный стол.")

    def serve_customer_thread(self, customer_id, table):
        # Имитация времени обслуживания (5 секунд)
        time.sleep(3)

        # Освобождаем стол
        table.is_busy = False

        # Если в очереди есть посетители, обслуживаем следующего
        if self.queue:
            next_customer = self.queue.pop(0)
            for t in self.tables:
                if not t.is_busy:
                    t.is_busy = True
                    print(f"Посетитель номер {next_customer} сел за стол {t.number}.")

                    next_customer_thread = threading.Thread(target=self.serve_customer_thread, args=(next_customer, t))
                    next_customer_thread.start()
                    break

        print(f"Посетитель номер {customer_id} покушал и ушёл.")


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()