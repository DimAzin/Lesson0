# 1) * Вам нужно самостоятельно познакомиться с модулем Rich,
# и написать код, который в терминале будет отображать вашу кассу (с различными действиями)
#
# Импорт для задачи:
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns
from rich.table import Table
from rich.prompt import Prompt
#
#

console = Console()
menu_text = """
Выберите одну из операций:
1. Добавить товар
2. Что в корзине
3. Очистить корзину
4. Создать чек
5. Завершить работу
"""
# Создание панели с заголовком
panel = Panel(Text(menu_text, justify="Left") , title="Касса", border_style="blue")
#console.print(panel)

# Создание таблицы для отображения продуктов
table = Table(title="Список продуктов")
table.add_column("Код", style="cyan", no_wrap=True)
table.add_column("Наименование", style="magenta")
table.add_column("Цена", justify="right", style="green")
#console.print(table)

products = []

def add_product(code, name, price):
    products.append({"code": code, "name": name, "price": price})
    table.add_row(str(code), name, f"{price:.2f} руб.")
    console.print(table)

def display_total():
    total = sum(product["price"] for product in products)
    console.print(f"[bold magenta]Итоговая сумма: {total:.2f}[/bold magenta] руб.")

def check():
    sum_check = sum(product["price"] for product in products)
    check_text = """
    Большое спасибо за покупку!
    Будем ждать Вас снова!
    --------------------------
    """
    check_text = check_text + '\n Количество товаров: ' + str(len(products)) + '\n Общая стоимость: ' + str(sum_check) + ' руб. \n Покупатель: Dmitry Azin \n \n Адрес магазина "Ромашка": ул. Березовая, 17'
    # Создание панели с заголовком
    panel_check = Panel(Text(check_text, justify="center"), title="Чек", border_style="blue")
    console.print(panel_check)

while True:
    console.print(panel)
    action = Prompt.ask("Выберите действие", choices=["1", "2", "3", "4", "5"], default="1")

    if action == "1":
        code = int(Prompt.ask("Введите код продукта"))
        name = Prompt.ask("Введите наименование продукта")
        price = float(Prompt.ask("Введите цену продукта"))
        add_product(code, name, price)
    elif action == "2":
        console.print(table)
        display_total()
    elif action == "3":
        table = Table(title="Список продуктов")
        table.add_column("Код", style="cyan", no_wrap=True)
        table.add_column("Наименование", style="magenta")
        table.add_column("Цена", justify="right", style="green")
        console.print(table)
        products = []
        display_total()
    elif action == "4":
        check()
    elif action == "5":
        break

console.print("[bold green]Работа завершена![/bold green]")


