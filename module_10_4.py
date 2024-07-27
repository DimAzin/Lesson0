import threading
import time
import queue


def excepthook(arg):
    print("Конец работы!")
class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()

class Cafe:
    Work_day = True
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()
        self.customer_id = 0

    def customer_arrival(self):
        while True:
            self.customer_id += 1
            if self.customer_id > 20:
                self.Work_day = False
                print("Последний клиент!")
                return
            else:
                print(f"Посетитель номер {self.customer_id} прибыл.")
                self.serve_customer(self.customer_id)
                time.sleep(1)  # промежуток между клиентами

    def serve_customer(self, customer_id):
        for table in self.tables:
            if not table.is_busy:
                # занимаем свободный столик
                customer = Customer(customer_id, table)
                customer.start()
                return
        # свободных столиков нет, клиент идет в очередь
        print(f"Посетитель номер {customer_id} ожидает свободный стол.")
        self.queue.put(customer_id)

    def process_queue(self):
        while self.Work_day:
            if not self.queue.empty():
                customer_id = self.queue.get()
                self.serve_customer(customer_id)
        raise Exception

class Customer(threading.Thread):
    def __init__(self, customer_id, table):
        threading.Thread.__init__(self)
        self.customer_id = customer_id
        self.table = table

    def run(self):
        with self.table.lock:
            self.table.is_busy = True
            print(f"Посетитель номер {self.customer_id} сел за стол {self.table.number}.")
            time.sleep(2)  # Время обслуживания 5 секунд
            self.table.is_busy = False
            print(f"Посетитель номер {self.customer_id} покушал и ушёл.")

# Инициализируем столики
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

threading.excepthook = excepthook

# потоки для клиентов и очереди
arrival_thread = threading.Thread(target=cafe.customer_arrival)
queue_thread = threading.Thread(target=cafe.process_queue)

arrival_thread.start()
queue_thread.start()

arrival_thread.join()
queue_thread.join()

print("Конец обслуживания.")