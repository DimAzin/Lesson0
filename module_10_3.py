import threading


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Помещаем {amount} на счет")
            new_balance = self.balance + amount
            self.balance = new_balance
            print(f"Новый баланс счета: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Списываем {amount} со счета")
                new_balance = self.balance - amount
                self.balance = new_balance
                print(f"Новый баланс счета: {self.balance}")
            else:
                print("Не достаточно средств на счету")


def deposit_task(account, amount):
    for _ in range(10):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(10):
        account.withdraw(amount)



account = BankAccount(100)
deposit_thread = threading.Thread(target=deposit_task, args=(account, 10))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 5))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(f"Окончательный баланс: {account.balance}")
