"""
Ты разрабатываешь программное обеспечение для сети магазинов.
Каждый магазин в этой сети имеет свои особенности, но также
существуют общие характеристики, такие как адрес, название
и ассортимент товаров. Ваша задача — создать класс Store,
который можно будет использовать для создания различных магазинов.
"""


# Шаблон магазина
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # метод для добавления товара в ассортимент магазина
    def add_item(self, product, price):
        self.items[product] = price

    # метод для удаления товара из ассортимента.
    def remove_item(self, product):
        self.items.pop(product)

    # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None
    def get_price(self, product):
        return self.items.get(product)

    # метод для изменения цены товара по его названию.
    def set_price(self, product, new_price):
        if self.items.get(product):
            self.items[product] = new_price


store1 = Store('"Магнит"', "ул.Красная 1")
store2 = Store('"Еда"', "ул.Красная 12")
store3 = Store('"Хозмаг"', "ул.Красная 123")
print(f"""
У нас есть три магазина:
{store1.name} по адресу: {store1.address}
{store2.name} по адресу: {store2.address}
{store3.name} по адресу: {store3.address}
""")

store3.add_item('Швабра', 349.99)
store3.add_item('Тряпка', 49.99)
store3.add_item('Ведро', 239.99)

print(f"В магазине {store3.name} по адресу: {store3.address} в продаже:\n {store3.items}")

print(f"Цена товара Ведро = {store3.get_price('Ведро')}\n")
store3.set_price('Ведро', 280)
print(f"Ведро стало дороже!\nЦена товара Ведро = {store3.get_price('Ведро')}")

store3.remove_item("Тряпка")
print("Тяпок больше нет!")
print(f"В магазине {store3.name} по адресу: {store3.address} в продаже:\n {store3.items}")

