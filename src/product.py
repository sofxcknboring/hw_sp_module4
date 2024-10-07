class Product:
    """
    Класс для представления продуктов
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if price < self.__price:
            user_answer = input("Цена ниже прошлой, продолжить?(y/n): ")
            if user_answer.lower() != "y":
                return

        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * other.quantity
